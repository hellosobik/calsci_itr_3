class Keypad_5X8:
    keypad_5X8_layout=[
        ["", "", "nav_u", "", ""],
        ["", "nav_l", "", "nav_r", "x"],
        ["", "", "nav_d", "(", ")"],
        ["pow(", "sin(", "cos(", "tan(", "log("],
        ["7", "8", "9", "nav_b", ""],
        ["4", "5", "6", "*", "/"],
        ["1", "2", "3", "+", "-"],
        [".", "0", "pow(10,", "", "="],
    ]
    def key_out(cls, col, row):
        # global keypad_5X8_layout
        return cls.keypad_5X8_layout[row][col]
