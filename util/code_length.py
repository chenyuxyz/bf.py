from generate_bf import *

def length_0_to_255():
    total = 0
    for i in range(256):
        total += len(generate_int(i))
    print("total length for printing 0 to 255: %d" % total)

if __name__ == "__main__":
    length_0_to_255()
