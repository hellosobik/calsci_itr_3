rows=7
menu_cursor=0
menu_display_size=rows
menu_display_position=0

input_list={"inp_0":" ", "inp_1":" ", "inp_2":" ", "inp_3":" ", "inp_4":" ", "inp_5":" ", "inp_6":" ", "inp_7":" ", "inp_8":" ", "inp_9":" ", "inp_10":" "}

form_list=["label_0", "inp_0", "label_1", "inp_1", "label_2", "inp_2", "label_3", "inp_3", "label_4", "inp_4", "label_5", "inp_5", "label_6", "inp_6", "label_7", "inp_7", "label_8", "inp_8", "label_9", "inp_9", "label_10", "inp_10"]

display_buffer=form_list[menu_display_position:menu_display_position+menu_display_size]

display_cursor=menu_cursor-menu_display_position

refresh_rows=(0,rows)

input_cursor=0
input_display_position=0
input_cols=21

while True:
    print(refresh_rows)
    print(display_buffer)
    print(display_cursor)
    print()

    for i in range(rows):
        if "inp_" in display_buffer[i]:
            print(i, input_list[display_buffer[i]][input_display_position:input_display_position+input_cols], input_cursor, input_display_position)
        else:
            print(i, display_buffer[i])

    inp=input("Enter command: ")

    if inp=="D":
        menu_cursor+=1

        if menu_cursor==len(form_list):
            menu_cursor=0
            menu_display_position=0
            refresh_rows=(0,rows)

        elif menu_cursor-menu_display_position==rows:
            menu_display_position+=1
            refresh_rows=(0,rows)

        else:
            refresh_rows=(menu_cursor-1-menu_display_position,menu_cursor-menu_display_position)
        input_cursor=0
        input_display_position=0

    elif inp=="U":
        menu_cursor-=1

        if menu_cursor<0:
            menu_cursor=len(form_list)-1
            menu_display_position=len(form_list)-rows
            refresh_rows=(0,rows)

        elif menu_cursor<menu_display_position:
            menu_display_position-=1
            refresh_rows=(0,rows)

        else:
            refresh_rows=(menu_cursor-menu_display_position,menu_cursor-menu_display_position+1)

        input_cursor=0
        input_display_position=0

    else:
        if "inp_" in form_list[menu_cursor]:

            if inp == "R":
                input_cursor+=1

                if input_cursor==len(input_list[form_list[menu_cursor]]):
                    input_cursor=0
                    input_display_position=0

                elif input_cursor==input_display_position+input_cols:
                    input_display_position+=1
                
            elif inp == "L" or inp == "B":
                input_cursor-=1
                
                if input_cursor<0:
                    input_cursor=len(input_list[form_list[menu_cursor]])-1
                    input_display_position=len(input_list[form_list[menu_cursor]])-input_cols
                    if input_display_position<0:
                        input_display_position=0

                elif input_cursor<input_display_position:
                    input_display_position-=1

                if inp == "B" and input_cursor!=len(input_list[form_list[menu_cursor]])-1:
                    input_list[form_list[menu_cursor]]=input_list[form_list[menu_cursor]][:input_cursor]+input_list[form_list[menu_cursor]][input_cursor+1:]
                    if len(input_list[form_list[menu_cursor]]) > input_cols and len(input_list[form_list[menu_cursor]][input_display_position:]) < input_cols:
                        input_display_position=len(input_list[form_list[menu_cursor]])-input_cols
                    elif len(input_list[form_list[menu_cursor]]) <=input_cols:
                        input_display_position=0
                    
            else:
                input_list[form_list[menu_cursor]]=input_list[form_list[menu_cursor]][:input_cursor]+inp+input_list[form_list[menu_cursor]][input_cursor:]
                input_cursor+=len(inp)
            
                if input_cursor==input_display_position+input_cols:
                    input_display_position+=1
            input_list[form_list[menu_cursor]]=input_list[form_list[menu_cursor]].rstrip()+" "

    display_buffer=form_list[menu_display_position:menu_display_position+menu_display_size]
    display_cursor=menu_cursor-menu_display_position