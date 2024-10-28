from data_modules.characters import Characters
from data_modules.keypad_map import Keypad_5X8
from input_modules.keypad import Keypad
from output_modules.st7565_spi import Display
from process_modules.text_buffer import Textbuffer
from process_modules.text_buffer_uploader import Tbf
from process_modules.typer import Typer
import utime as time  # type:ignore
from math import *

def calculate():
    chtrs = Characters()
    keymap = Keypad_5X8()
    # keyin=Keypad(rows=[4, 5, 13, 14, 15, 16, 17, 18], cols=[19, 21, 22, 23, 25])
    keyin = Keypad(rows=[4, 2, 18, 5, 17, 23, 22, 21], cols=[33, 32, 15, 16, 19])
    # display=Display(cs1=2, rs=32, rst=33, sda=27, sck=26)
    display = Display(cs1=25, rs=27, rst=26, sda=14, sck=13)

    # txt=Textbuffer()
    # sometext2="""Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world.Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world.Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world.Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world.Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world.Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world.Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world.Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world.Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world.Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world.Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world"""
    # sometext="Mechanical engineering is one of the oldest and most fundamental disciplines in the field of engineering. It is a branch of engineering that combines principles of physics, materials science, and mathematics to design, analyze, manufacture, and maintain mechanical systems. As a vast and versatile domain, mechanical engineering plays a pivotal role in various industries such as automotive, aerospace, energy, manufacturing, robotics, and many more. Its breadth encompasses everything from the micro-scale of nanotechnology to the macro-scale of large industrial machinery, making it an integral part of the modern world.hello world"
    txt = Textbuffer()
    tbf = Tbf(disp_out=display, chrs=chtrs, t_b=txt)
    tbf.refresh()
    typer = Typer(keypad=keyin, keypad_map=keymap)
    while True:
        x = typer.start_typing()
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
        time.sleep(0.2)