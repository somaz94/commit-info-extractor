# Extract Commit Action

![CI](https://github.com/somaz94/commit-info-extractor/actions/workflows/ci.yml/badge.svg)
[![License](https://img.shields.io/github/license/somaz94/commit-info-extractor)](https://github.com/somaz94/commit-info-extractor/blob/main/LICENSE)
![Latest Tag](https://img.shields.io/github/v/tag/somaz94/commit-info-extractor)
![Python](https://img.shields.io/badge/python-3.14-blue?logo=python)
[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Commit%20Info%20Extractor-blue?logo=github)](https://github.com/marketplace/actions/extract-commit-action)

A powerful GitHub Action that extracts and processes information from commit messages using customizable patterns and commands.

<br/>

## Features

- **Flexible Pattern Matching**: Extract information using regex patterns or custom commands
- **Multiple Output Formats**: Support for text, JSON, and CSV outputs
- **Customizable Depth**: Control the number of commits to analyze
- **Fast & Lightweight**: Built with Python 3.14-slim for optimal performance
- **Fail-Safe Options**: Optional validation with `fail_on_empty`
- **Pretty Formatting**: Clean, formatted commit message output
- **Debug Mode**: Verbose output for troubleshooting
- **Timeout Control**: Prevent long-running operations
- **Easy Integration**: Simple YAML configuration in your workflows
<br/>

## Quick Start

```yaml
- name: Extract Environment from Commits
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 10
    extract_command: "grep -oE 'env:(\\w+)'"
    pretty: true
    key_variable: 'DEPLOY_ENV'
```

<br/>

## Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `commit_limit` | Number of commits to retrieve | Yes | N/A |
| `extract_command` | Command to extract info (e.g., grep pattern) | No | N/A |
| `pretty` | Use pretty format for Git logs | No | `false` |
| `key_variable` | Name of the output variable | No | `ENVIRONMENT` |
| `fail_on_empty` | Fail if no information is extracted | No | `false` |
| `output_format` | Output format: `text`, `json`, or `csv` | No | `text` |
| `debug` | Enable debug mode for verbose output | No | `false` |
| `timeout` | Timeout in seconds for git/extract commands | No | `30` |

<br/>

## Outputs

| Output | Description |
|--------|-------------|
| `key_variable` | The name of the variable used |
| `value_variable` | The extracted value(s) from commits |

<br/>

## Common Use Cases

<br/>

### Extract Environment Information

```yaml
- name: Extract Environment
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 10
    extract_command: "grep -oE 'env:(\\w+)'"
    pretty: true
    key_variable: 'DEPLOY_ENV'
```

<br/>

### Find Feature Tags

```yaml
- name: Extract Feature Tags
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 10
    extract_command: "grep -oE 'feature:(\\w+)'"
    key_variable: 'FEATURE_TAG'
```

<br/>

### Extract Version Numbers

```yaml
- name: Extract Version
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 10
    extract_command: "grep -oE 'v[0-9]+\\.[0-9]+\\.[0-9]+'"
    key_variable: 'VERSION'
```

<br/>

### Fail on Empty Results

```yaml
- name: Extract Critical Changes
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 10
    extract_command: "grep -oE 'critical:(\\w+)'"
    key_variable: 'CRITICAL_CHANGES'
    fail_on_empty: true  # Fails if no matches found
```

<br/>

### Extract JIRA Tickets with JSON Output

```yaml
- name: Extract JIRA Tickets
  id: jira
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 20
    extract_command: "grep -oE 'JIRA-[0-9]+'"
    key_variable: 'JIRA_TICKETS'
    output_format: 'json'

- name: Process Tickets
  run: |
    echo '${{ steps.jira.outputs.value_variable }}' | jq -r '.[]'
```

<br/>

### Debug Mode for Troubleshooting

```yaml
- name: Extract with Debug
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 10
    extract_command: "grep -oE 'env:(\\w+)'"
    key_variable: 'ENVIRONMENT'
    debug: true          # Enable verbose output
    timeout: 60          # Set custom timeout
```

<br/>

## Output Formats

The action supports three output formats:

| Format | Description | Example Output |
|--------|-------------|----------------|
| `text` | Plain text (default) | `value1`<br/>`value2`<br/>`value3` |
| `json` | JSON array | `["value1", "value2", "value3"]` |
| `csv` | Comma-separated | `value1,value2,value3` |

<br/>

### Format Examples

Given extracted values: `JIRA-123`, `JIRA-456`, `JIRA-789`

#### Text format:
```
JIRA-123
JIRA-456
JIRA-789
```

#### JSON format:
```json
["JIRA-123", "JIRA-456", "JIRA-789"]
```

#### CSV format:
```
JIRA-123,JIRA-456,JIRA-789
```

<br/>

## Extract Command Examples

| Purpose | Command | Example Match |
|---------|---------|---------------|
| Environment | `grep -oE 'env:(\\w+)'` | `env:production` |
| Fix IDs | `grep -oE 'fix-[0-9]+'` | `fix-123` |
| Versions | `grep -oE 'v[0-9]+\\.[0-9]+\\.[0-9]+'` | `v1.2.3` |
| Features | `grep -oE 'feature:(\\w+)'` | `feature:login` |
| JIRA IDs | `grep -oE 'JIRA-[0-9]+'` | `JIRA-456` |
| Conventional Commits | `grep -oE '^(feat|fix|chore|docs):'` | `feat:`, `fix:` |

> **Note**: Use `grep -oE` (Extended regex) instead of `grep -oP` (Perl regex) for better compatibility.

<br/>

## Best Practices

<br/>

### Commit Message Format
- Use consistent commit message formats (e.g., [Conventional Commits](https://www.conventionalcommits.org/))
- Include relevant tags or identifiers
- Example: `feat(auth): add login functionality env:production`

<br/>

### Extraction Patterns
- Test regex patterns locally before implementation:
  ```bash
  echo "feat: add login env:production" | grep -oE 'env:(\\w+)'
  ```
- Use specific patterns to avoid false matches
- Consider edge cases and special characters

<br/>

### Performance
- Set appropriate `commit_limit` based on your needs
- Lower values = faster execution
- Typical range: 10-50 commits

<br/>

### Repository Setup
- Ensure sufficient `fetch-depth` in checkout action:
  ```yaml
  - uses: actions/checkout@v4
    with:
      fetch-depth: 20  # Match or exceed commit_limit
  ```

<br/>

## Troubleshooting

<br/>

### No Matches Found

#### Problem: Action completes but returns empty results

#### Solutions:
1. Verify commit messages contain expected patterns:
   ```bash
   git log -10 --pretty=%B
   ```
2. Test your regex pattern locally:
   ```bash
   git log -10 --pretty=%B | grep -oE 'your-pattern'
   ```
3. Ensure `fetch-depth` in checkout is sufficient
4. Check if `fail_on_empty` is set appropriately

### Incorrect Matches

#### Problem: Extracting wrong or unexpected values

#### Solutions:
- Review and refine your regex pattern
- Use more specific patterns with word boundaries
- Test with sample commit messages first
- Use online regex testers like [regex101.com](https://regex101.com)

### Action Fails with Error

#### Problem: Action exits with non-zero code

#### Possible Causes:
- `fail_on_empty: true` is set and no matches found (intended behavior)
- Invalid regex pattern in `extract_command`
- Git repository not available
- Insufficient permissions

#### Debug Steps:
```yaml
- name: Debug Commit Messages
  run: git log -${{ inputs.commit_limit }} --pretty=%B

- name: Test Extract Command
  run: |
    git log -10 --pretty=%B | grep -oE 'your-pattern' || echo "No matches"

# Or use built-in debug mode
- name: Extract with Debug Mode
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 10
    extract_command: "grep -oE 'your-pattern'"
    debug: true  # Shows detailed execution information
```

### Timeout Errors

#### Problem: Action times out during execution

#### Solutions:
- Increase timeout value (default is 30 seconds):
  ```yaml
  - uses: somaz94/commit-info-extractor@v1
    with:
      commit_limit: 10
      extract_command: "complex-command"
      timeout: 120  # Increase to 2 minutes
  ```
- Reduce `commit_limit` to process fewer commits
- Simplify your `extract_command` pattern

<br/>

## Advanced Usage

### Processing Multiple Matches

When multiple values are extracted, you can process them in subsequent steps:

#### Text format:
```yaml
- name: Extract JIRA Tickets
  id: extract
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 10
    extract_command: "grep -oE 'JIRA-[0-9]+'"
    key_variable: 'JIRA_TICKETS'

- name: Process Each Ticket
  run: |
    while IFS= read -r ticket; do
      echo "Processing: $ticket"
      # Your processing logic here
    done <<< "${{ steps.extract.outputs.value_variable }}"
```

#### JSON format:
```yaml
- name: Extract as JSON
  id: extract_json
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 10
    extract_command: "grep -oE 'JIRA-[0-9]+'"
    output_format: 'json'

- name: Process JSON Array
  run: |
    echo '${{ steps.extract_json.outputs.value_variable }}' | \
      jq -r '.[]' | while read -r ticket; do
        echo "Processing: $ticket"
      done
```

### Combining with Other Actions

#### Send to Slack:
```yaml
- name: Extract Deployment Info
  id: deploy
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 5
    extract_command: "grep -oE 'env:(\\w+)'"
    key_variable: 'ENVIRONMENT'

- name: Notify Slack
  uses: slackapi/slack-github-action@v1
  with:
    payload: |
      {
        "text": "Deploying to: ${{ steps.deploy.outputs.value_variable }}"
      }
```

#### Conditional Deployment:
```yaml
- name: Check for Production Tag
  id: check_env
  uses: somaz94/commit-info-extractor@v1
  with:
    commit_limit: 1
    extract_command: "grep -oE 'env:production'"
    fail_on_empty: false

- name: Deploy to Production
  if: steps.check_env.outputs.value_variable == 'env:production'
  run: |
    echo "Deploying to production..."
```

<br/>

## Security Considerations

When using this action, keep the following in mind:

#### Command Injection Prevention
- The `extract_command` executes shell commands
- Never use untrusted user input in extraction commands
- Always validate and sanitize inputs

#### Sensitive Information
- Be careful not to extract secrets or credentials from commit messages
- Use GitHub's [secret scanning](https://docs.github.com/en/code-security/secret-scanning) alongside this action
- Consider filtering sensitive patterns

#### Permission Scopes
- This action only requires **read access** to repository content
- Follow the principle of least privilege in your workflows

<br/>

## Local Testing

Test the Python script locally without Docker:

```bash
# Clone the repository
git clone https://github.com/somaz94/commit-info-extractor.git
cd commit-info-extractor

# Run tests
python3 tests/test_local.py

# Or test manually
export INPUT_COMMIT_LIMIT=10
export INPUT_EXTRACT_COMMAND="grep -oE 'feat|fix|chore'"
export INPUT_PRETTY=true
export INPUT_DEBUG=true      # Enable debug mode
export INPUT_TIMEOUT=60       # Set timeout
python3 entrypoint.py
```

See [tests/TESTING.md](tests/TESTING.md) for more details.

<br/>

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and updates.

<br/>

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<br/>

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

<br/>

## Support

If you find this action helpful, please consider:
- Starring the repository
- Sharing with others
- Contributing improvements

<br/>

## Related Projects

- [actions/checkout](https://github.com/actions/checkout) - Checkout your repository
- [github-script](https://github.com/actions/github-script) - Write workflows using JavaScript
- [setup-python](https://github.com/actions/setup-python) - Set up Python environment

---

Made by [somaz94](https://github.com/somaz94)

