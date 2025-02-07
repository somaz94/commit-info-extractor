# Extract Commit Action

<!-- [![GitHub Super-Linter](https://github.com/somaz94/commit-info-extractor/actions/workflows/linter.yml/badge.svg)](https://github.com/somaz94/commit-info-extractor) -->
![CI](https://github.com/somaz94/commit-info-extractor/actions/workflows/ci.yml/badge.svg)
[![License](https://img.shields.io/github/license/somaz94/commit-info-extractor)](https://github.com/somaz94/container-action)
![Latest Tag](https://img.shields.io/github/v/tag/somaz94/commit-info-extractor)
![Top Language](https://img.shields.io/github/languages/top/somaz94/commit-info-extractor?color=green&logo=terraform&logoColor=blue)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Commit%20Info%20Extractor-blue?logo=github)](https://github.com/marketplace/actions/extract-commit-action)

## Description

The **Extract Commit Action** extracts information from commit messages. It can
be configured to limit the number of commits analyzed, apply custom extraction
commands, and output the results to a variable. This Action is ideal for
workflows that need to analyze or react based on commit message content.

## Features

- 🔍 Flexible commit message analysis
- 🎯 Customizable extraction patterns
- 📊 Configurable commit depth
- 🔄 Support for pretty formatting
- 🎨 Custom variable naming
- 🛠️ Regex pattern support
- 📝 Detailed output logging


## Inputs

| **Input Name**    | **Description**                                  | **Required** | **Default**   |
| ----------------- | ------------------------------------------------ | ------------ | ------------- |
| `commit_limit`    | Number of commits to retrieve.                   | Yes          | N/A           |
| `pretty`          | Use pretty format for Git logs.                  | No           | `false`       |
| `key_variable`    | Name of the key variable to set.                 | No           | `ENVIRONMENT` |
| `extract_command` | Command to use for extracting info from commits. | No           | N/A           |

## Outputs

| **Output Name**  | **Description**                              |
| ---------------- | -------------------------------------------- |
| `key_variable`   | Extracted key variable used in the action.   |
| `value_variable` | Extracted value variable used in the action. |

## Common Use Cases

### 1. Extract Environment Information

```yaml
steps:
  - name: Checkout
    uses: actions/checkout@v4
    with:
      fetch-depth: 10

  - name: Extract Commit Information
    uses: somaz94/commit-info-extractor@v1
    with:
      commit_limit: 10
      extract_command: "grep -oP 'env:(\\w+)'" # Use regex for values
      pretty: true
      key_variable: 'DEPLOY_ENV' # Key (default ENVIRONMENT)
```

### 2. Find Feature Tags

```yaml
steps:
...
  - name: Extract Commit Information
    uses: somaz94/commit-info-extractor@v1
    with:
      commit_limit: 10
      extract_command: "grep -oP 'feature:(\\w+)'"
      pretty: true
      key_variable: 'FEATURE_TAG'
```

### 3. Extract Version Numbers

```yaml
steps:
...
  - name: Extract Commit Information
    uses: somaz94/commit-info-extractor@v1
    with:
      commit_limit: 10
      extract_command: "grep -oP 'v\\d+\\.\\d+\\.\\d+'"
      pretty: true
      key_variable: 'VERSION'
```


## Extract Command Examples

| Purpose | Command | Example Match |
|---------|---------|---------------|
| Environment | `grep -oP 'env:(\w+)'` | `env:production` |
| Fix IDs | `grep -oP 'fix-\d+'` | `fix-123` |
| Versions | `grep -oP 'v\d+\.\d+\.\d+'` | `v1.2.3` |
| Features | `grep -oP 'feature:(\w+)'` | `feature:login` |
| Jira IDs | `grep -oP 'JIRA-\d+'` | `JIRA-456` |

# Best Practices

1. **Commit Message Format**
   - Use consistent commit message formats
   - Include relevant tags or identifiers
   - Follow conventional commit standards

2. **Extraction Patterns**
   - Use specific regex patterns
   - Test patterns before implementation
   - Consider edge cases

3. **Commit Depth**
   - Set appropriate commit_limit
   - Consider repository size
   - Balance between depth and performance

## Troubleshooting

### Common Issues

1. **No Matches Found**
   - Check if commit messages contain expected patterns
   - Verify regex pattern syntax
   - Ensure sufficient commit depth

2. **Incorrect Matches**
   - Review regex pattern
   - Check for conflicting patterns
   - Verify commit message format

3. **Performance Issues**
   - Reduce commit_limit
   - Optimize regex patterns
   - Check repository size

## License

This project is licensed under the [MIT License](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
