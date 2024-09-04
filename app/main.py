import sys


def main():

    if len(sys.argv) < 3:
        print("Usage: ./your_program.sh tokenize <filename>", file=sys.stderr)
        exit(1)

    command = sys.argv[1]
    filename = sys.argv[2]

    if command != "tokenize":
        print(f"Unknown command: {command}", file=sys.stderr)
        exit(1)

    with open(filename) as file:
        file_contents = file.read()

    for char in file_contents:
        if char == '(':
            print(f"LEFT_PAREN {char} null")
        elif char == ')':
            print(f"RIGHT_PAREN {char} null")
        elif char == '{':
            print(f"LEFT_BRACE {char} null")
        elif char == '}':
            print(f"RIGHT_BRACE {char} null")
        elif char == ',':
            print(f"COMMA {char} null")
        elif char == '.':
            print(f"DOT {char} null")
        elif char == '-':
            print(f"MINUS {char} null")
        elif char == '+':
            print(f"PLUS {char} null")
        elif char == ';':
            print(f"SEMICOLON {char} null")
        elif char == '*':
            print(f"STAR {char} null")
    print("EOF  null")

if __name__ == "__main__":
    main()
