import os

from app.output_writer import set_output_variables


class TestSetOutputVariables:
    def test_local_execution(self, clean_env, capsys):
        set_output_variables("production", "DEPLOY_ENV", 1)
        captured = capsys.readouterr()
        assert "DEPLOY_ENV=production" in captured.out
        assert "match_count=1" in captured.out

    def test_default_key_variable(self, clean_env, capsys):
        set_output_variables("value", "", 0)
        captured = capsys.readouterr()
        assert "ENVIRONMENT=value" in captured.out

    def test_match_count_display(self, clean_env, capsys):
        set_output_variables("val", "KEY", 5)
        captured = capsys.readouterr()
        assert "Match Count: 5" in captured.out

    def test_github_actions_env(self, monkeypatch, github_output_files):
        env_file, output_file = github_output_files
        monkeypatch.setenv("GITHUB_ENV", env_file)
        monkeypatch.setenv("GITHUB_OUTPUT", output_file)

        set_output_variables("production", "DEPLOY_ENV", 3)

        env_content = open(env_file).read()
        output_content = open(output_file).read()

        assert "value_variable<<EOF_" in env_content
        assert "production" in env_content
        assert "key_variable=DEPLOY_ENV" in env_content
        assert "match_count=3" in env_content

        assert "value_variable<<EOF_" in output_content
        assert "production" in output_content
        assert "key_variable=DEPLOY_ENV" in output_content
        assert "match_count=3" in output_content

    def test_multiline_value(self, monkeypatch, github_output_files):
        env_file, output_file = github_output_files
        monkeypatch.setenv("GITHUB_ENV", env_file)
        monkeypatch.setenv("GITHUB_OUTPUT", output_file)

        set_output_variables("line1\nline2\nline3", "RESULT", 3)

        content = open(output_file).read()
        assert "line1\nline2\nline3" in content
        assert "key_variable=RESULT" in content
        assert "match_count=3" in content
