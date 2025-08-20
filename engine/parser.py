def cutCommand(cmd: str) -> list[str]:
    result = []
    current = []
    inQuote = False
    for char in cmd:
        if char == '"':
            inQuote = not inQuote
        elif char == " " and not inQuote:
            if current:
                result.append("".join(current))
                current = []
        else:
            current.append(char)
    if current:
        result.append("".join(current))
    return result


def toExecutable(parts: list[str]):
    return parts[0].lower(), parts[1:], " ".join(parts[1:])


def isPartValid(syntaxPart: str):
    if syntaxPart.startswith("...") and len(syntaxPart) > 3:
        return isPartValid(syntaxPart[3:])
    if syntaxPart == "str" or syntaxPart == "number":
        return True
    return False


def isPartsValid(syntaxParts: list[str]):
    for index in range(len(syntaxParts)):
        part = syntaxParts[index]
        if part.startswith("...") and index != len(syntaxParts) - 1:
            return False
        if not isPartValid(part):
            return False
    return True


def getRestType(syntax: str):
    if syntax.startswith("."):
        return str(getRestType(syntax[1:]))
    else:
        return syntax


def isArgMatch(arg: str, syntax: str):
    if isPartValid(syntax):
        targetType = syntax
        if syntax.startswith("..."):
            targetType = getRestType(syntax)
        if targetType == "str":
            return True
        if targetType == "number":
            try:
                float(arg)
                return True
            except ValueError:
                return False


def isArgsMatch(args: list[str], syntaxParts: list[str]):
    if not isPartsValid(syntaxParts):
        return False
    if len(args) < len(syntaxParts):
        return False
    if len(syntaxParts) == 0 and len(args) > 0:
        return False
    for i in range(len(args)):
        arg = args[i]
        part = syntaxParts[min(len(syntaxParts) - 1, i)]
        if part.startswith("..."):
            if not isArgMatch(arg, getRestType(part)):
                return False
        else:
            if not isArgMatch(arg, part):
                return False
    return True


def castArgs(args: list[str], syntaxParts: list[str]):
    result = []
    rest = []
    for i in range(len(args)):
        arg = args[i]
        part = syntaxParts[min(len(syntaxParts) - 1, i)]
        if part.startswith("..."):
            if getRestType(part) == "str":
                rest.append(arg)
            if getRestType(part) == "number":
                rest.append(float(arg))
        else:
            if part == "str":
                result.append(arg)
            if part == "number":
                result.append(float(arg))
    if len(rest) > 0:
        result.append(rest)
    return result
