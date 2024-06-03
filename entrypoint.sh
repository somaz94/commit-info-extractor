#!/bin/sh

# Fetch commit messages with optional pretty formatting
COMMIT_MESSAGES=$(git log -$INPUT_COMMIT_LIMIT ${INPUT_PRETTY:+--pretty=%B})

echo "Commit Messages: $COMMIT_MESSAGES"

# Use the provided command to extract information.
if [ -n "$INPUT_EXTRACT_COMMAND" ]; then
	# Using eval to execute the command, ensuring the command is wrapped in quotes for proper handling
	ENVIRONMENT=$(echo "$COMMIT_MESSAGES" | eval "$INPUT_EXTRACT_COMMAND")
else
	ENVIRONMENT="$COMMIT_MESSAGES"
fi

echo "Extracted Environment: $ENVIRONMENT"

# Set the output variable name, defaulting to 'ENVIRONMENT' if not specified
OUTPUT_VAR=${INPUT_OUTPUT_VARIABLE:-ENVIRONMENT}

# Conditional handling for GitHub Actions or local execution
if [ -n "$GITHUB_ENV" ]; then
	# GitHub Actions environment
	echo "$OUTPUT_VAR=$ENVIRONMENT" >> "$GITHUB_ENV"
	echo "$OUTPUT_VAR=$ENVIRONMENT" >> "$GITHUB_OUTPUT"
else
	# Local execution
	echo "Final Environment Variable ($OUTPUT_VAR): $ENVIRONMENT"
fi