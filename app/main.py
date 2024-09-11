import sys

all_tkns = {
    '(' : "LEFT_PAREN",
    ')' : "RIGHT_PAREN",
    '{' : "LEFT_BRACE",
    '}' : "RIGHT_BRACE",
}

class Scanner:
    def __init__(self, src):
        self.src = src
        self.tkns = []
        self.strt = 0
        self.curr = 0
    
    def is_at_end(self):
        return self.curr >= len(self.src)


def main():

    # filename = sys.argv[1]

    # with open(filename) as file:
    #     file_contnts = file.read()

    scanner = Scanner(")(}{)")
    all_tkns_symbls = all_tkns.keys()
    for char in scanner.src:
        if char in all_tkns_symbls:
            scanner.tkns.append(char)
        print(f"{all_tkns[char]} {char} null")

    
if __name__ == "__main__":
    main()
