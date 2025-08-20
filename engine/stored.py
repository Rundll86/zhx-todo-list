from typing import Callable

commands: dict[str, Callable] = {}
syntaxes: dict[str, list[str]] = {}
descriptions: dict[str, str] = {}


def action(description: str, *syntax: str):
    def wrapper(func: Callable):
        commands[func.__name__] = func
        syntaxes[func.__name__] = list(syntax)
        descriptions[func.__name__] = description
        return func

    return wrapper


def generateCommandUsage(executable: str):
    return f"{executable.upper()}{''.join(list(map(lambda x: f' <{x}>',syntaxes[executable])))} - {descriptions[executable]}"
