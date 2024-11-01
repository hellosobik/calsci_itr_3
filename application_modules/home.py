from data_modules.characters import Characters
from data_modules.keypad_map import Keypad_5X8
from input_modules.keypad import Keypad
from output_modules.st7565_spi import Display
from process_modules.menu_buffer import Menu
from process_modules.menu_buffer_uploader import Tbf
from process_modules.typer import Typer
from data_modules.configuration import keypad_cols, keypad_rows, st7565_display_pins
from application_modules.calculate import calculate

# calculate()

def hello_world():
    print("hello world!")
cal=calculate
def home():
    # calculate()
    global cal
    chtrs = Characters()
    keymap = Keypad_5X8()
    keyin = Keypad(rows=keypad_rows, cols=keypad_cols)
    calculate()
    display = Display(cs1=st7565_display_pins["cs1"], rs=st7565_display_pins["rs"], rst=st7565_display_pins["rst"], sda=st7565_display_pins["sda"], sck=st7565_display_pins["sck"])
    menu = Menu(menu_list = ["hello_world!", "calculator"], menu_list_functions = [hello_world, cal])
    # calculate()
    tbf = Tbf(disp_out=display, chrs=chtrs, m_b=menu)
    # tbf.refresh()
    typer = Typer(keypad=keyin, keypad_map=keymap)
    # calculate()
    while True:
        inp=input("enter the command: ")
        if inp=="ok" and menu.menu_list[menu.menu_cursor]=="calculator":
            del cal, chtrs, keymap, keyin, display, menu, tbf, typer
            calculate()
        else:
            menu.update_buffer(inp)
            tbf.refresh()