import json

from app.formatter import format_output


class TestFormatOutput:
    def test_text_format(self):
        result = format_output("value1\nvalue2\nvalue3", "text")
        assert result == "value1\nvalue2\nvalue3"

    def test_json_format(self):
        result = format_output("value1\nvalue2\nvalue3", "json")
        parsed = json.loads(result)
        assert parsed == ["value1", "value2", "value3"]

    def test_json_format_single_value(self):
        result = format_output("value1", "json")
        parsed = json.loads(result)
        assert parsed == ["value1"]

    def test_csv_format(self):
        result = format_output("value1\nvalue2\nvalue3", "csv")
        assert result == "value1,value2,value3"

    def test_csv_format_with_commas(self):
        result = format_output("val,ue1\nvalue2", "csv")
        assert result == '"val,ue1",value2'

    def test_csv_format_with_quotes(self):
        result = format_output('val"ue1\nvalue2', "csv")
        assert result == '"val""ue1",value2'

    def test_empty_value_returns_as_is(self):
        assert format_output("", "json") == ""
        assert format_output("  ", "csv") == "  "

    def test_json_filters_empty_lines(self):
        result = format_output("value1\n\nvalue2\n", "json")
        parsed = json.loads(result)
        assert parsed == ["value1", "value2"]

    def test_json_unicode(self):
        result = format_output("hello\nworld", "json")
        parsed = json.loads(result)
        assert parsed == ["hello", "world"]
