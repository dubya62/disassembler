import sys

if len(sys.argv) < 2:
    print("usage:")
    print("python main.py <program_name>")
    exit(0)

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename, 'rb') as f:
        data = bytearray(f.read())



    







