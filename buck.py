from sys import argv
from typing import List

lines: str = None
tape: List[int] = [0 for _ in range(10)]
head: int = 0


def increment() -> None:
    tape[head] += 1


def decrement() -> None:
    tape[head] -= 1


def move_right() -> None:
    global head
    head += 1
    if head == len(tape):
        tape.append(0)


def move_left() -> None:
    global head
    head -= 1

    if head < 0:
        temp = [0]
        temp.extend(tape)
        tape = temp


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
    global lines

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
    main(argv[1] if len(argv) == 2 else "sample.bf")
