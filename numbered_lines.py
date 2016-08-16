#!/usr/bin/env python3
def numbered_lines():
    with open("small.txt", "r") as fin:
        with open("small2.txt", "w") as fout:
            for idx, item in enumerate(fin):
                fout.write(str(idx + 1) + " " + item)

def main():
    numbered_lines()

if __name__ == "__main__":
    main()
