VERSION = "0.0.1"
HELP_TEXT = (
    open("help.txt", encoding="utf8")
    .read()
    .format(version=VERSION, commands="{commands}")
)
