# # from data_modules.characters import Characters
# # from data_modules.keypad_map import Keypad_5X8
# # from input_modules.keypad import Keypad
# # from output_modules.st7565_spi import Display
# # from process_modules.typer import Typer
# # import utime as time  # type:ignore
# # from math import *

def fun_0():
    print("fun_0")

def fun_1():
    print("fun_1")

def fun_2():
    print("fun_2")

def fun_3():
    print("fun_3")

def fun_4():
    print("fun_4")

def fun_5():
    print("fun_5")

def fun_6():
    print("fun_6")

def fun_7():
    print("fun_7")

def fun_8():
    print("fun_8")

def fun_9():
    print("fun_9")

def fun_10():
    print("fun_10")

# # menu_list=["label_0", "label_1", "label_2", "label_3", "label_4", "label_5", "label_6", "label_7", "label_8", "label_9", "label_10"]
# # menu_list_functions=[fun_0, fun_1, fun_2, fun_3, fun_4, fun_5, fun_6, fun_7, fun_8, fun_9, fun_10]

# menu_list=["label_0", "label_1", "label_2"]
# menu_list_functions=[fun_0, fun_1, fun_2]
                     
# rows=7
# menu_cursor=0
# menu_display_size=rows
# menu_display_position=0

# display_buffer=menu_list[menu_display_position:menu_display_position+menu_display_size]

# display_cursor=menu_cursor-menu_display_position

# refresh_rows=(0,rows)

# while True:
#     # refresh_rows=(0,rows)
#     print(refresh_rows)
#     print(display_buffer)
#     print(display_cursor)
#     inp=input("Enter command: ")
#     if inp=="d":
#         menu_cursor+=1
#         if menu_cursor==len(menu_list):
#             menu_cursor=0
#             menu_display_position=0
#             refresh_rows=(0,rows)
#         elif menu_cursor-menu_display_position==rows:
#             # menu_cursor+=1
#             menu_display_position+=1
#             refresh_rows=(0,rows)
#         else:
#             refresh_rows=(menu_cursor-1-menu_display_position,menu_cursor-menu_display_position)
#     elif inp=="u":
#         menu_cursor-=1
#         if menu_cursor<0:
#             menu_cursor=len(menu_list)-1
#             menu_display_position=len(menu_list)-rows
#             refresh_rows=(0,rows)
#         elif menu_cursor<menu_display_position:
#             # menu_cursor+=1
#             menu_display_position-=1
#             refresh_rows=(0,rows)
#         else:
#             refresh_rows=(menu_cursor-menu_display_position,menu_cursor-menu_display_position+1)
#     elif inp=="e":
#         menu_list_functions[menu_cursor]()
#     display_buffer=menu_list[menu_display_position:menu_display_position+menu_display_size]
#     display_cursor=menu_cursor-menu_display_position

def fun_0():
    print("fun_0")

def fun_1():
    print("fun_1")

def fun_2():
    print("fun_2")

# menu_list = ["label_0", "label_1", "label_2"]
menu_list=["label_0", "label_1", "label_2", "label_3", "label_4", "label_5", "label_6", "label_7", "label_8", "label_9", "label_10"]
# # 
# menu_list_functions = [fun_0, fun_1, fun_2]
menu_list_functions=[fun_0, fun_1, fun_2, fun_3, fun_4, fun_5, fun_6, fun_7, fun_8, fun_9, fun_10]

rows = 7  # number of rows on display
menu_cursor = 0
menu_display_size = min(rows, len(menu_list))  # set display size to the smaller of rows or menu_list length
menu_display_position = 0

display_buffer = menu_list[menu_display_position:menu_display_position + menu_display_size]
display_cursor = menu_cursor - menu_display_position

refresh_rows = (0, rows)

while True:
    print("Display rows to refresh:", refresh_rows)
    print("Display buffer:", display_buffer)
    print("Cursor position:", display_cursor)

    inp = input("Enter command (u for up, d for down, e for enter): ")
    if inp == "d":
        menu_cursor += 1
        if menu_cursor == len(menu_list):  # Wrap to top if at the bottom
            menu_cursor = 0
            menu_display_position = 0
            refresh_rows = (0, menu_display_size)
        elif menu_cursor - menu_display_position == menu_display_size:
            menu_display_position += 1
            refresh_rows = (0, menu_display_size)
        else:
            refresh_rows = (menu_cursor - 1 - menu_display_position, menu_cursor - menu_display_position)
    elif inp == "u":
        menu_cursor -= 1
        if menu_cursor < 0:  # Wrap to bottom if at the top
            menu_cursor = len(menu_list) - 1
            menu_display_position = max(0, len(menu_list) - menu_display_size)
            refresh_rows = (0, menu_display_size)
        elif menu_cursor < menu_display_position:
            menu_display_position -= 1
            refresh_rows = (0, menu_display_size)
        else:
            refresh_rows = (menu_cursor - menu_display_position, menu_cursor - menu_display_position + 1)
    elif inp == "e":
        menu_list_functions[menu_cursor]()

    display_buffer = menu_list[menu_display_position:menu_display_position + menu_display_size]
    display_cursor = menu_cursor - menu_display_position
