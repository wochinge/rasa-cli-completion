from pathlib import Path

if __name__ == "__main__":
    script_name = "rasa-complete.sh"
    script_location = Path(__file__).parent / script_name

    print("Thanks for installing this library 🚀")
    print("Add this to your bash / zsh config:\n ")
    print(f"EXPORT RASA_COMPLETE_SCRIPT={script_location}")
