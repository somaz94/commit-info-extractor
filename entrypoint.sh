#!/bin/sh

# Allow git operations in the current directory
git config --global --add safe.directory /usr/src
# Explicitly set safe directory for git operations
git config --global --add safe.directory /github/workspace

# Check if .git directory exists
if [ -d ".git" ]; then
	# Fetch commit messages with optional pretty formatting
	if ! COMMIT_MESSAGES=$(git log -"$INPUT_COMMIT_LIMIT" "${INPUT_PRETTY:+--pretty=%B}"); then
		echo "Error fetching commit messages"
		exit 1
	fi
	echo "Commit Messages:"
	echo "$COMMIT_MESSAGES"
else
	echo "No git repository available."
	COMMIT_MESSAGES="No commit messages available."
fi

# Use the provided command to extract information.
if [ -n "$INPUT_EXTRACT_COMMAND" ]; then
	# Using eval to execute the command, ensuring the command is wrapped in quotes for proper handling
	if ! ENVIRONMENT=$(echo "$COMMIT_MESSAGES" | eval "$INPUT_EXTRACT_COMMAND" | sort -u); then
		echo "Error extracting environment information"
		exit 1
	fi
else
	ENVIRONMENT="$COMMIT_MESSAGES"
fi

echo "Extracted Environment: $ENVIRONMENT"

# Set the output variable name, defaulting to 'ENVIRONMENT' if not specified
OUTPUT_VAR=${INPUT_OUTPUT_VARIABLE:-ENVIRONMENT}

# Echo input variable for debugging or further use
echo "Input Variable: $OUTPUT_VAR"

# Conditional handling for GitHub Actions or local execution
if [ -n "$GITHUB_ENV" ]; then
	# GitHub Actions environment
	echo "output_variable=$ENVIRONMENT" >> "$GITHUB_ENV"
	echo "::set-output name=output_variable::$ENVIRONMENT"
	echo "::set-output name=input_variable::$OUTPUT_VAR"  # 추가된 부분
else
	# Local execution
	echo "Final Environment Variable ($OUTPUT_VAR): $ENVIRONMENT"
fi

exit 0
