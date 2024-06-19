# Extract Commit Action

[![GitHub Super-Linter](https://github.com/actions/container-action/actions/workflows/linter.yml/badge.svg)](https://github.com/super-linter/super-linter)
![CI](https://github.com/actions/container-action/actions/workflows/ci.yml/badge.svg)

## Description

The **Extract Commit Action** extracts information from commit messages.
It can be configured to limit the number of commits analyzed, apply custom
extraction commands, and output the results to a variable. This Action is ideal
for workflows that need to analyze or react based on commit message content.

## Features

- **Commit Limit**: Define how many recent commits to analyze.
- **Pretty Formatting**: Optional pretty formatting for `git log`.
- **Custom Extraction**: Apply any command to extract data from commit messages.
- **Dynamic Output**: Specify the output variable name dynamically.

## Inputs

| **Input Name**    | **Description**                               | **Required** | **Default**  |
|-------------------|-----------------------------------------------|----------|---------------|
| `commit_limit`    | Number of commits to retrieve.                | Yes      | N/A           |
| `pretty`          | Use pretty format for git logs.               | No       | `false`       |
| `output_variable` | Name of the output variable to set.           | No       | `ENVIRONMENT` |
| `extract_command` | Command to use for extracting info from commits. | No       | N/A           |

## Outputs

| **Output Name**    | **Description**                          |
|--------------------|-------------------------------------------|
| `output_variable`  | Extracted output variable information.    |
| `input_variable`   | Debugging input variable used in the action. |

## Usage

### Setup Action

To integrate this action into your workflow, add the following step to your
`.github/workflows` YAML file:

```yaml
steps:
  - name: Checkout
    uses: actions/checkout@v4
    with:
      fetch-depth: 10

  - name: Extract Commit Information
    uses: your-github-username/commit-info-extractor@v1
    with:
      commit_limit: 10
      extract_command: "grep -oP '\\bfix\\b'" # Use regex for values
      pretty: true
      output_variable: 'CUSTOM_ENV' # Key
```

## Configuration

- **commit_limit**: Set this to limit the number of commits
  the action will consider.
- **pretty**: Set this to true if you want the commit messages
  to be fetched in a pretty format.
- **output_variable**: Define a custom environment variable
  to store the extracted information.
- **extract_command**: Customize the command to extract specific
  information from the commit messages.

## Example Workflow

Here's a full workflow example using the Extract Commit Action:

```yaml
name: Analyze Commit Messages

on: [push]

jobs:
  analyze_commits:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Extract Fixes from Commits
        uses: somaz94/commit-info-extractor@v1
        with:
          commit_limit: 20
          extract_command: "grep -oP '\\bfix\\b'" # Use regex for values
          pretty: false
          output_variable: 'FIXES_FOUND' # Key

      - name: Print Output
        run: |
          echo "Extracted variable: ${{ steps.extract_commit.outputs.input_variable }} = ${{ steps.extract_commit.outputs.output_variable }}"
```

### License

This project is licensed under the [MIT License](LICENSE) file for details.
