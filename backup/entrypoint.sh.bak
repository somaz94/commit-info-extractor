#!/bin/sh

# Function to print headers
print_header() {
	printf "\n%s\n" "=================================================="
	printf "🚀 %s\n" "$1"
	printf "%s\n\n" "=================================================="
}

# Function to print sections
print_section() {
	printf "\n📋 %s:\n" "$1"
}

# Function to print success messages
print_success() {
	printf "✅ %s\n" "$1"
}

# Function to print error messages
print_error() {
	printf "❌ %s\n" "$1"
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
		printf "  • Last %s commits:\n" "$INPUT_COMMIT_LIMIT"
		printf "%s\n" "$COMMIT_MESSAGES" | sed 's/^/    /'
	else
		printf "  • No git repository available\n"
		COMMIT_MESSAGES="No commit messages available."
	fi
}

# Function to extract environment information
extract_environment() {
	print_section "Extracting Environment Information"
	if [ -n "$INPUT_EXTRACT_COMMAND" ]; then
		printf "  • Using extract command: %s\n" "$INPUT_EXTRACT_COMMAND"
		if ! ENVIRONMENT=$(printf "%s" "$COMMIT_MESSAGES" | eval "$INPUT_EXTRACT_COMMAND" | sort -u); then
			print_error "Failed to extract environment information"
		fi
	else
		ENVIRONMENT="$COMMIT_MESSAGES"
	fi
	printf "  • Extracted value: %s\n" "$ENVIRONMENT"
}

# Function to set output variables
set_output_variables() {
	print_section "Setting Output Variables"
	OUTPUT_VAR=${INPUT_KEY_VARIABLE:-ENVIRONMENT}
	printf "  • Key Variable: %s\n" "$OUTPUT_VAR"
	
	if [ -n "$GITHUB_ENV" ]; then
		# GitHub Actions environment
		{
			printf "value_variable=%s\n" "$ENVIRONMENT"
			printf "key_variable=%s\n" "$OUTPUT_VAR"
		} >> "$GITHUB_ENV"
		
		{
			printf "value_variable=%s\n" "$ENVIRONMENT"
			printf "key_variable=%s\n" "$OUTPUT_VAR"
		} >> "$GITHUB_OUTPUT"
		
		print_success "Variables set in GitHub Actions environment"
	else
		# Local execution
		print_success "Local execution - variables would be set as:"
		printf "  • %s=%s\n" "$OUTPUT_VAR" "$ENVIRONMENT"
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
