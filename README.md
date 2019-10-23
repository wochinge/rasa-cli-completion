# rasa-cli-completion

Simple implementation of a bash / zsh autocomplete script for [Rasa](https://github.com/rasahq/rasa).

## Requirements
- Installed [rasa](https://github.com/rasahq/rasa) library
- A unix system

![rasa-cli-completion gif](https://media.giphy.com/media/l1IZ379sMbT1WjulKr/giphy.gif)

## Installation

### Using pip

1. Run `pip install rasa-cli-completion`
2. Run `pip install .` in the cloned directory
3. Add the output of the following command to your `.bashrc` / `.zshrc`

    ```bash
    python -m rasa_cli_completion.show_config
    ```

### Using this repository

1. Clone this repository
2. Run `pip install .` in the cloned directory
3. Add the output of the following command to your `.bashrc` / `.zshrc`

    ```bash
    python -m rasa_cli_completion.show_config
    ```

## Notes
- The completion is a bit slow at the beginning. However, the completion results are cached in `~/.rasa-autocomplete.json` (you can turn caching off by setting `RASA_AUTOCOMPLETE_CACHING_OFF=true`)
