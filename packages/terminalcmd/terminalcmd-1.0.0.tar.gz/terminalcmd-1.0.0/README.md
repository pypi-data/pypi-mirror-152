# terminalcmd

**`Terminalcmd`** is a Python library which can help you to 
make your own terminal program with high-intellegence instruments, 
that will make your code "clear" and readable.

`Note`: Library is in beta-test now, so it will update very often.

# Installition
###### Using Pypi:
```bash
$ pip install terminalcmd
```

## Examples :
##### Easy-to-build greeter:
```py
from terminalcmd import core


@core.command(
    short_descrtiption="Greet you!",  # Set description, that will be shown in help-message.
    usage="greet (No arguments)"  # Let user know how to use this command.
    # Of course, all this params can be unfilled.
    # But don't forget about () after decorator!
)
def greet() -> None:  
    # Create functiuon. As command name in console will be used function name.
    name = input("What's your name: ")
    print(f"Hello {name}!")


if __name__ == "__main__":
    core.start_console()  # Starting console.
```
Let's see aguments of `core.command()` *(ALL parameter can be unfilled)*:

1. `name: str` - If you need to name your command such as '8ball', you can name function however you want, and set parameter `name="8ball"` to name command like this. 
2. `description: str` - Long command description, that will be show after typing `[command name] ?` (will be discussed later).
3. `short_description: str` - Short note about command (You can add empty decorator upside function and add a `"""Docstring"""` to function, this is another way to set short_description). Will be shown after typing `help` and `[command name] ?`.
4. `usage: str` - Examples of usage this command.

##### Builtins:
```py
from terminalcmd import core


@core.command()  # Create some random command.
def hello() -> None:
    """Say "Hello!" to user."""
    print("hello!")


if __name__ == "__main__":
    core.start_console()
```
If you'll run this file and type `'help'`, you'll see
that you have 3 commands: `'help'`, `'exit'` and `'hello'`.
But why? You added only one!
It's because of builtins commands:  

  Command `help` show all commands in your programm.
  Command `exit` kill current task with exit code 0.

If you need to get information about one command,
Use next syntax: `[command] ?`.
Let's see what will be after typing `help ?`:
```bash
Command 'help':
  Short description:
    'Show help message.'
  Description:
    'Show information about every commands in list.'
  Usage:
    '<help>, <help ?>'
```
Like this you can get info about every command.

*Interest fact*:
If you will call `core.start_console()` without any
registred command in your file, you'll get
ZeroCommandsError (:

##### Some usefull things:
```py
from terminalcmd import (
    core, 
    get_command,
    line_args,
    commands_list
)

@core.command()
def all_commands() -> None:
    """Show all commands in your programm."""
    print(commands_list)


@core.command(
    short_descrtiption="Show usefull functions and methods.",
    usage="You can type whatever you want, but it must startswith 'show_uf'."
)
def show_ut() -> None:
    print("\nLet's see commands arguments"
          f"(like sys.argv, but after typing command):\n{line_args()}")
    
    curr_command = get_command("show_ut")
    print(
        "Description: " + curr_command.description,
        "Usage: " + curr_command.usage
    )


if __name__ == "__main__":
    core.start_console()
```

Function `line_args` don't take any arguments and return lit time typed arguments to comandlet by `typing.List[str]`.

Function `get_command` take 2 arguments:
1. `name: str` - A name of a command.
2. `allow_none_return: bool` - Argument allowing return None if function cannot find given command by name.

Run this code to watch this usefull things.

Open issues if you meet some not standard situation and good luck!