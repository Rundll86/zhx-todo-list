import sys, math
from .. import sysinfo
from ..stored import action, commands, generateCommandUsage


@action("显示帮助")
def help(args, data, rest):
    commandsUsages = []
    for command in commands:
        commandsUsages += [generateCommandUsage(command)]
    print(sysinfo.HELP_TEXT.format(commands="\n".join(commandsUsages)))


@action("添加新任务", "...str")
def add(args, data, rest):
    data.extend(args[0])


@action("删除指定任务", "...str")
def rm(args, data, rest):
    for arg in args[0]:
        data.remove(arg)


@action("显示当前待办列表")
def show(args, data, rest):
    if len(data) == 0:
        print("没有添加任何内容")
    else:
        for i in range(len(data)):
            item = data[i]
            print(f"{i + 1}. {item}")


@action("退出程序", "number")
def exit(args, data, rest):
    sys.exit(args[0])


@action("重复添加新任务", "number", "...str")
def repeat(args, data, rest):
    for task in args[1]:
        for i in range(math.floor(args[0])):
            data.append(task)


@action("合并两个任务", "number", "number", "str")
def merge(args, data, rest):
    first = data[int(args[0] - 1)]
    second = data[int(args[1] - 1)]
    data.append(first + args[2] + second)
    symbol = object()
    data[int(args[0] - 1)] = symbol
    data[int(args[1] - 1)] = symbol
    while symbol in data:
        data.remove(symbol)


def init():
    pass
