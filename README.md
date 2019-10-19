# rasa-cli-completion

Simple implementation of a bash / zsh autocomplete script for [Rasa](https://github.com/rasahq/rasa).

## Requirements
- Installed [rasa](https://github.com/rasahq/rasa) library
- A unix system

![rasa-cli-completion gif](https://media.giphy.com/media/l1IZ379sMbT1WjulKr/giphy.gif)

## Usage
1. Clone this repository
2. Source `rasa-complete.sh` 
3. Add this your bash / zsh config:

    ```bash
    RASA_CLI_COMPLETION_PATH=<path to cloned directory>
    source ${RASA_CLI_COMPLETION_PATH}/rasa-cli-completion/rasa-complete.sh
    export RASA_COMPLETE_SCRIPT=${RASA_CLI_COMPLETION_PATH}/rasa_cli_completion/rasa_complete.py
    
    ```

## Notes
- The completion is a bit slow at the beginning. However, the completion results are cached in `~/.rasa-autocomplete.json` (you can turn caching off by setting `RASA_AUTOCOMPLETE_CACHING_OFF=true`)
