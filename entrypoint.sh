#!/bin/sh

# Function to print headers
print_header() {
	echo "\n=================================================="
	echo "🚀 $1"
	echo "==================================================\n"
}

# Function to print sections
print_section() {
	echo "\n📋 $1:"
}

# Function to print success messages
print_success() {
	echo "✅ $1"
}

# Function to print error messages
print_error() {
	echo "❌ $1"
	exit 1
}

# Function to configure git
configure_git() {
	print_section "Configuring Git"
	git config --global --add safe.directory /usr/src || print_error "Failed to set safe.directory /usr/src"
	git config --global --add safe.directory /github/workspace || print_error "Failed to set safe.directory /github/workspace"
	print_success "Git configuration completed"
}

# Function to fetch commit messages
fetch_commit_messages() {
	print_section "Fetching Commit Messages"
	if [ -d ".git" ]; then
		if ! COMMIT_MESSAGES=$(git log -"$INPUT_COMMIT_LIMIT" "${INPUT_PRETTY:+--pretty=%B}"); then
			print_error "Failed to fetch commit messages"
		fi
		echo "  • Last $INPUT_COMMIT_LIMIT commits:"
		echo "$COMMIT_MESSAGES" | sed 's/^/    /'
	else
		echo "  • No git repository available"
		COMMIT_MESSAGES="No commit messages available."
	fi
}

# Function to extract environment information
extract_environment() {
	print_section "Extracting Environment Information"
	if [ -n "$INPUT_EXTRACT_COMMAND" ]; then
		echo "  • Using extract command: $INPUT_EXTRACT_COMMAND"
		if ! ENVIRONMENT=$(echo "$COMMIT_MESSAGES" | eval "$INPUT_EXTRACT_COMMAND" | sort -u); then
			print_error "Failed to extract environment information"
		fi
	else
		ENVIRONMENT="$COMMIT_MESSAGES"
	fi
	echo "  • Extracted value: $ENVIRONMENT"
}

# Function to set output variables
set_output_variables() {
	print_section "Setting Output Variables"
	OUTPUT_VAR=${INPUT_KEY_VARIABLE:-ENVIRONMENT}
	echo "  • Key Variable: $OUTPUT_VAR"
	
	if [ -n "$GITHUB_ENV" ]; then
		# GitHub Actions environment
		{
			echo "value_variable=$ENVIRONMENT"
			echo "key_variable=$OUTPUT_VAR"
		} >> "$GITHUB_ENV"
		
		{
			echo "value_variable=$ENVIRONMENT"
			echo "key_variable=$OUTPUT_VAR"
		} >> "$GITHUB_OUTPUT"
		
		print_success "Variables set in GitHub Actions environment"
	else
		# Local execution
		print_success "Local execution - variables would be set as:"
		echo "  • $OUTPUT_VAR=$ENVIRONMENT"
	fi
}

# Main execution
main() {
	print_header "Environment Variable Extractor"
	
	configure_git
	fetch_commit_messages
	extract_environment
	set_output_variables
	
	print_header "Process Completed Successfully"
}

# Execute main function
main

exit 0
