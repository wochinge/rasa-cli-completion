# rasa-cli-completion

Simple implementation of a bash / zsh autocomplete script for [Rasa](https://github.com/rasahq/rasa).

## Requirements
- Installed [rasa](https://github.com/rasahq/rasa) library
- A unix system

## Usage
1. Clone this repository
2. Source `rasa-complete.sh` 
3. Add the given export of `RASA_COMPLETE_SCRIPT` to your bash / zsh config


## Notes
- The completion is quite slow at the beginning. However, the completion results are cached in `~/.rasa-autocomplete.json` (you can turn caching off by setting `RASA_AUTOCOMPLETE_CACHING_OFF=true`
