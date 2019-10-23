#!/bin/bash

function complete_rasa() {
    local current_word possible_arguments
    COMPREPLY=()

    if [[ -z ${RASA_COMPLETE_SCRIPT} ]]; then
        echo "You didn't add RASA_COMPLETE_SCRIPT to your bash config!"
        return 1
    else
        current_word="${COMP_WORDS[COMP_CWORD]}"
        possible_arguments=`python -m rasa_cli_completion.rasa_complete "$COMP_LINE"`
        COMPREPLY=( $(compgen -W "${possible_arguments}" -- ${current_word}) )
    fi
}

complete -F complete_rasa rasa
