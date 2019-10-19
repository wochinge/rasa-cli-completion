from rasa_cli_completion import rasa_complete as complete

HELP_OUTPUT = """
usage: rasa [-h] [--version]
            {init,run,shell,train,interactive,test,visualize,data,x} ...

Rasa command line interface. Rasa allows you to build your own conversational
assistants 🤖. The 'rasa' command allows you to easily run most common commands
like creating a new bot, training or evaluating models.

positional arguments:
  {init,run,shell,train,interactive,test,visualize,data,x}
                        Rasa commands
    init                Creates a new project, with example training data,
                        actions, and config files.
    run                 Starts a Rasa server with your trained model.
    shell               Loads your trained model and lets you talk to your
                        assistant on the command line.
    train               Trains a Rasa model using your NLU data and stories.
    interactive         Starts an interactive learning session to create new
                        training data for a Rasa model by chatting.
    test                Tests Rasa models using your test NLU data and
                        stories.
    visualize           Visualize stories.
    data                Utils for the Rasa training files.

optional arguments:
  -h, --help            show this help message and exit
  --version             Print installed Rasa version
  --no-prompt           Artificial example
"""


def test_find_positional_arguments():
    positional_arguments = complete.find_positional_arguments(HELP_OUTPUT)
    assert set(positional_arguments) == {
        "init",
        "run",
        "shell",
        "train",
        "interactive",
        "test",
        "visualize",
        "data",
        "x",
    }


def test_find_optional_arguments():
    optional_arguments = complete.find_optional_arguments(HELP_OUTPUT)
    assert set(optional_arguments) == {"--help", "--version", "--no-prompt"}


def test_call_rasa():
    command = ["rasa"]
    result = complete.call_rasa(command)
    assert "positional arguments" in HELP_OUTPUT
    assert isinstance(result, str)


def test_call_rasa_level_2():
    command = ["rasa", "data"]
    result = complete.call_rasa(command)
    assert "positional arguments" in HELP_OUTPUT
    assert isinstance(result, str)


def test_call_rasa_until_complete():
    command = "rasa --".split()
    result = complete.call_rasa_until_valid(command)
    assert "positional arguments" in HELP_OUTPUT
    assert isinstance(result, str)


def test_call_rasa_until_complete_rasa_x():
    command = "rasa x --".split()
    result = complete.call_rasa_until_valid(command)
    optional_arguments = complete.find_optional_arguments(result)
    assert len(optional_arguments) > 1


def test_call_rasa_if_argument_expected():
    command = "rasa x --rasa-x-port --help".split()
    result = complete.call_rasa_until_valid(command)

    assert result == ""


def test_remove_already_used_optional_arguments():
    command = "rasa run --enable-api"
    arguments = complete.get_arguments(command)

    assert "--enable-api" not in arguments
