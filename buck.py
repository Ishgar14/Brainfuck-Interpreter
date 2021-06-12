from sys import argv
from typing import List

lines: str = None
tape: List[int] = [0 for _ in range(100)]
head: int = 0
position: int = 0


def increment() -> None:
    tape[head] += 1


def decrement() -> None:
    tape[head] -= 1


def move_right() -> None:
    global head
    head += 1


def move_left() -> None:
    global head
    head -= 1


def loop() -> None:
    global head


def display() -> None:
    print(chr(tape[head]), end='')


instructions = {
    '+': increment,
    '-': decrement,
    '>': move_right,
    '<': move_left,
    '.': display,
}


def execute(ins: str, pos: int) -> None:
    global tape, head

    func = instructions.get(ins, None)

    if func is not None:
        func()

    elif ins == '[':
        # find index of `]` with `pos` as starting index
        end = lines.index(']', pos)

        while tape[head] != 0:
            for i in range(pos + 1, end):
                instruction = lines[i]
                execute(instruction, i)


def main(filename: str = None) -> None:
    global lines, position

    if filename is None:
        filename = 'bf-interpreter/first.bf'

    with open(filename, 'r') as f:
        lines = f.read()

    i = 0
    while i < len(lines):
        instruction = lines[i]
        execute(instruction, i)

        if instruction == '[':
            i = lines.index(']', i) + 1
        else:
            i += 1


if __name__ == '__main__':
    print("The commandline is\n", argv)
    #  python .\bf-interpreter\buck.py .\bf-interpreter\first.bf

    if len(argv) == 2:
        main(argv[1])
    else:
        main()
