#!/bin/bash

# Function to safely escape single quotes in the command
escape_single_quotes() {
    local input="$1"
    # Replace every single quote ' with '\'' using parameter expansion
    echo "${input//\'/\'\\\'\'}"
}

# Function to add an alias
add_alias() {
    local alias_name="$1"
    local alias_command="$2"
    local shell_rc

    # Escape single quotes in the command
    alias_command=$(escape_single_quotes "$alias_command")

    # Detect the shell configuration file
    # if [[ "$SHELL" == *"zsh" ]]; then
    #     shell_rc="$HOME/.zshrc"
    # elif [[ "$SHELL" == *"bash" ]]; then
    #     shell_rc="$HOME/.bashrc"
    # else
    #     echo "Unsupported shell: $SHELL"
    #     exit 1
    # fi

    # Gets the alias file
    shell_rc="$HOME/.config/zsh/.aliaszshrc"

    # Add the alias to the configuration file
    echo "alias $alias_name='$alias_command'" >>"$shell_rc"

    echo "Alias '$alias_name' added successfully!"
    # echo "Run 'source $shell_rc' to apply the changes."
    echo "Run 'source $HOME/.zshrc' to apply the changes."
}

# Check if the script is run with two arguments
if [[ $# -ne 2 ]]; then
    echo "Usage: createalias <alias_name> <command>"
    echo "Example: createalias ll 'ls -l'"
    exit 1
fi

# Call the function with the provided arguments
add_alias "$1" "$2"
