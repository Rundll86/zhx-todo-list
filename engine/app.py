from . import parser, stored
from .builtin import commands


class ZhXTodoList:
    data: list[str] = []

    def __init__(self) -> None:
        commands.init()

    def run(self, command: str):
        parts = parser.cutCommand(command)
        executable, args, rest = parser.toExecutable(parts)
        action = stored.commands.get(executable)
        syntax = stored.syntaxes.get(executable)
        if action and isinstance(syntax, list):
            if callable(action):
                if parser.isArgsMatch(args, syntax):
                    try:
                        action(parser.castArgs(args, syntax), self.data, rest)
                    except Exception as e:
                        print(f"命令执行失败：{e}")
                else:
                    print(
                        f"命令[{executable}]的语法错误，用法：{stored.generateCommandUsage(executable)}"
                    )
        else:
            print(f"未知命令：{executable}")

    def inputOnce(self, tip: str):
        self.run(input(tip))
