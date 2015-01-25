"""
Brainfuck interpreter in python 3
"""

def bf_eval(code):
    """ evaluate the brainfuck code """
    mem = [0] * 30000
    now = 0
    ptr = 0
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
                stack = 1
                while stack > 0:
                    now += 1
                    if code[now] == "[":
                        stack += 1
                    elif code[now] == "]":
                        stack -= 1
        elif command == "]":
            stack = 1
            while stack > 0:
                now -= 1
                if code[now] == "]":
                    stack += 1
                elif code[now] == "[":
                    stack -= 1
            now -= 1
        now += 1
