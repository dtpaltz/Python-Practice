

class Direction:
    LEFT = 0
    RIGHT = 1
    BOTH = 2
    # other directions in the future?


class Instruction:
    @staticmethod
    def set_direction(direction: str):
        if direction == '->':
            return Direction.RIGHT
        elif direction == '<-':
            return Direction.LEFT
        elif direction == '<->':
            return Direction.BOTH
        else:
            raise Exception('Invalid direction!')

    def __init__(self, num: int, direction: str ):
        self.num = int(num)
        self.direction = self.set_direction(direction)


def turn_into_instructions(string_input: str, delimiter: str):
    if string_input == "" or string_input is None:
        return list()

    # split and then parse
    def parse_instruction(string_input_inner: str):
        index = 0
        for ch in string_input_inner:
            if not ch.isdigit():
                break
            index += 1
        return Instruction(string_input_inner[:index], string_input_inner[index:])

    return map(parse_instruction, string_input.split(delimiter))


instructs = turn_into_instructions("1<-> 2-> 3<-", " ")
for istruct in instructs:
    print("Num: {0}   |   Moves: {1}".format(istruct.num, istruct.direction))



















