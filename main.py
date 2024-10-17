from data_modules.characters import Characters
from data_modules.keypad_map import Keypad_5X8
from input_modules.keypad import Keypad
from output_modules.st7565_spi import Display
from process_modules.text_buffer import Textbuffer
from process_modules.text_buffer_uploader import Tbf
from process_modules.typer import Typer
import utime as time # type:ignore
from math import *

chtrs=Characters()
keymap=Keypad_5X8()
keyin=Keypad(rows=[4, 5, 13, 14, 15, 16, 17, 18], cols=[19, 21, 22, 23, 25])
display=Display(cs1=2, rs=32, rst=33, sda=27, sck=26)
txt=Textbuffer()
txt.buffer()
tbf=Tbf(disp_out=display, chrs=chtrs, t_b=txt)
typer=Typer(keypad=keyin, keypad_map=keymap)
while True:
    x=typer.start_typing()
    if x=="=":
        res=str(eval(txt.text_buffer))
        txt.all_clear()
        txt.update_buffer(res)
        tbf.refresh()
    else:
        txt.update_buffer(x)
    tbf.refresh()
