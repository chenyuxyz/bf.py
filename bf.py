"""
Brainfuck interpreter in python 3
"""

def build_bracesmap(code):
    bracesmap = {}
    stack = []
    for idx, command in enumerate(code):
        if command not in "[]":
            continue
        if command == "[":
            stack.append(idx)
        elif command == "]":
            if not stack:
                raise Exception("Unmatched Braces")
            openbrace = stack.pop()
            closebrace = idx
            bracesmap[openbrace] = closebrace
            bracesmap[closebrace] = openbrace
    return bracesmap, code

def bf_eval(code):
    """ evaluate the brainfuck code """
    mem = [0] * 30000
    now = 0
    ptr = 0
    bracesmap, code = build_bracesmap(code)
    while now < len(code):
        command = code[now]

        if command not in "><+-[],.":
            now += 1
            continue

        if command == ">":
            ptr += 1
        elif command == "<":
            ptr -= 1
        elif command == "+":
            mem[ptr] += 1
        elif command == "-":
            mem[ptr] -= 1
        elif command == ",":
            mem[ptr] = ord(input()[0])
        elif command == ".":
            print(chr(mem[ptr]), end="")
        elif command == "[":
            if mem[ptr] == 0:
                now = bracesmap[now]
        elif command == "]":
            now = bracesmap[now] - 1
        now += 1

def bf_to_py(code):
    print("mem = [0] * 30000")
    print("ptr = 0")
    indent = ""

    for c in code:
        if c not in "><+-[],.":
            continue

        if c == ">":
            print(indent + "ptr += 1")
        elif c == "<":
            print(indent + "ptr -= 1")
        elif c == "+":
            print(indent + "mem[ptr] += 1")
        elif c == "-":
            print(indent + "mem[ptr] -= 1")
        elif c == ",":
            print(indent + "mem[ptr] = ord(input()[0])")
        elif c == ".":
            print(indent + "print(chr(mem[ptr]), end=\"\")")
        elif c == "[":
            print(indent + "while mem[ptr]:")
            indent += " " * 4
        elif c == "]":
            indent = indent[:-4]
