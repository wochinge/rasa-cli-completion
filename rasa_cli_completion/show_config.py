from pathlib import Path

if __name__ == "__main__":
    install_directory = Path(__file__).parent
    shell_script_location = install_directory / "rasa-complete.sh"
    py_script_location = install_directory / "rasa_complete.py"

    print("Thanks for installing this library 🚀")
    print("Add this to your bash / zsh config:\n ")
    print(f"source {shell_script_location}")
    print(f"export RASA_COMPLETE_SCRIPT={py_script_location}")
