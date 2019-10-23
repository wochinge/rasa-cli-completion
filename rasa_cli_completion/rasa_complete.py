import io
import time
import contextlib
from pathlib import Path
from sys import argv
import re
import json
from typing import Text, List, Dict
import sys


max_caching_time = 345_600  # 4 weeks
cache_file_path = Path.home() / ".rasa-autocomplete.json"

EXPECTED_ARGUMENT_ERROR = "expected one argument"
OTHER_ARGUMENT_ERROR = "error: "  # e.g. invalid argument


def find_positional_arguments(text: Text) -> List[Text]:
    pattern = r"{(.*)}"
    regex = re.compile(pattern)
    matched = regex.search(text)
    if matched:
        return matched.group(1).strip().split(",")
    else:
        return []


def find_optional_arguments(text: Text) -> List[Text]:
    pattern = r"[^\[](--[^\s]+)"
    regex = re.compile(pattern)
    matched = regex.findall(text)
    return [match.strip() for match in matched]


def call_rasa(command: List[Text]) -> Text:
    import rasa.__main__

    command.append("--help")
    sys.argv = command

    std_out = io.StringIO()
    std_error = io.StringIO()

    with contextlib.redirect_stdout(std_out):
        with contextlib.redirect_stderr(std_error):
            try:
                rasa.__main__.main()
            except SystemExit as _:
                # expected behavior
                pass

    printed_messages = std_out.getvalue()
    if not printed_messages:
        return std_error.getvalue()
    else:
        return printed_messages


def call_rasa_until_valid(command: List[Text]) -> Text:
    command_result = call_rasa(command.copy())

    if EXPECTED_ARGUMENT_ERROR in command_result:
        return ""
    elif OTHER_ARGUMENT_ERROR in command_result:
        return call_rasa(command[:-1])
    else:
        return command_result


def get_cache() -> Dict:
    if cache_file_path.exists():
        content = cache_file_path.read_text(encoding="utf-8")
        return json.loads(content)
    else:
        return {}


def store_cache(command: Text, arguments: List[Text], current_cache: Dict) -> None:
    import os

    if os.environ.get("RASA_AUTOCOMPLETE_CACHING_OFF"):
        return

    current_cache[command] = {"args": arguments, "timestamp": time.time()}
    dumped = json.dumps(current_cache)
    cache_file_path.touch()
    cache_file_path.write_text(dumped, encoding="utf-8")


def get_arguments(current_command: Text) -> List[Text]:
    command_as_array = [c.strip() for c in current_command.split()]

    help_input = call_rasa_until_valid(command_as_array)

    optional_arguments = find_optional_arguments(help_input)
    positional_arguments = find_positional_arguments(help_input)
    optional_arguments = [
        arg for arg in optional_arguments if arg not in command_as_array
    ]

    return positional_arguments + optional_arguments


if __name__ == "__main__":
    if len(argv) < 2:
        # No command was provided
        exit(1)

    _current_command = argv[1]

    cached = get_cache()
    cached_result = cached.pop(_current_command, None)
    if not cached_result or time.time() - cached_result["timestamp"] > max_caching_time:
        possibilities = get_arguments(_current_command)
    else:
        possibilities = cached_result["args"]

    store_cache(_current_command, possibilities, cached)

    for possibility in possibilities:
        print(possibility)
