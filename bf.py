def run(code):
    mem = [0] * 30000
    now = 0
    ptr = 0
    l = len(code)
    while now < l:
        c = code[now]
        if c == ">":
            ptr += 1
        elif c == "<":
            ptr -= 1
        elif c == "+":
            mem[ptr] += 1
        elif c == "-":
            mem[ptr] -= 1
        elif c == ",":
            mem[ptr] = ord(input()[0])
        elif c == ".":
            print(chr(mem[ptr]), end="")
        elif c == "[":
            if mem[ptr] == 0:
                stack = 1
                while stack > 0:
                    now += 1
                    if code[now] == "[":
                        stack += 1
                    elif code[now] == "]":
                        stack -= 1
        elif c == "]":
            stack = 1
            while stack > 0:
                now -= 1
                if code[now] == "]":
                    stack += 1
                elif code[now] == "[":
                    stack -= 1
            now -= 1
        now += 1
