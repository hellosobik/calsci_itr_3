from data_modules.characters import Characters
from data_modules.keypad_map import Keypad_5X8
from input_modules.keypad import Keypad
from output_modules.st7565_spi import Display
from process_modules.text_buffer import Textbuffer
from process_modules.text_buffer_uploader import Tbf
from process_modules.typer import Typer
from data_modules.configuration import keypad_cols, keypad_rows, st7565_display_pins
import utime as time  # type:ignore
from math import *

def calculate():
    chtrs = Characters()
    keymap = Keypad_5X8()
    keyin = Keypad(rows=keypad_rows, cols=keypad_cols)
    display = Display(cs1=st7565_display_pins["cs1"], rs=st7565_display_pins["rs"], rst=st7565_display_pins["rst"], sda=st7565_display_pins["sda"], sck=st7565_display_pins["sck"])
    sometext="Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world"
    txt = Textbuffer(text_buffer=sometext)
    tbf = Tbf(disp_out=display, chrs=chtrs, t_b=txt)
    display.clear_display()
    tbf.refresh()
    typer = Typer(keypad=keyin, keypad_map=keymap)
    motion=["nav_r", "nav_r", "nav_r", "nav_r", "nav_r", "nav_d", "nav_u", "nav_u", "nav_u", "nav_u", "nav_u", "nav_u", "nav_u", "nav_u", "nav_u", "nav_u", "nav_u", "nav_u",  "nav_r",  "nav_r"]
    counter=0
    while True:
        # x = typer.start_typing()
        x=motion[counter]
        # print(txt.text_buffer, len(txt.text_buffer))
        if x == "=" and txt.text_buffer[0] != "𖤓":
            res = str(eval(txt.text_buffer[: txt.text_buffer_nospace]))
            txt.all_clear()
            display.clear_display()
            txt.update_buffer(res)
        elif x != "=":
            txt.update_buffer(x)
        if txt.text_buffer[0] == "𖤓":
            display.clear_display()
            txt.all_clear()
            # txt.update_buffer(res)
        tbf.refresh()
        # print(txt.text_buffer, txt.menu_buffer_cursor)
        counter+=1
        time.sleep(1)
