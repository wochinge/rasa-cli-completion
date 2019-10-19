#!/bin/bash

function complete_rasa() {
    local current_word possible_arguments
    COMPREPLY=()

    if [[ -z ${RASA_COMPLETE_SCRIPT} ]]; then
        echo "You didn't add RASA_COMPLETE_SCRIPT to your bash config!"
        return 1
    else
        current_word="${COMP_WORDS[COMP_CWORD]}"
        possible_arguments=`python ${RASA_COMPLETE_SCRIPT} "$COMP_LINE"`
        COMPREPLY=( $(compgen -W "${possible_arguments}" -- ${current_word}) )
    fi
}

complete -F complete_rasa rasa

echo "Thanks for sourcing me 🎉"
echo "Please add this to your bash / zsh config:\n"

current_directory="$( cd "$(dirname "$0")" ; pwd -P )"

echo "export RASA_COMPLETE_SCRIPT=${current_directory}/rasa_cli_completion/rasa_complete.py"
