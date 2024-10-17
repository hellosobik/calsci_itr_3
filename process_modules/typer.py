class Typer:
    def __init__(self, keypad, keypad_map):
        self.keypad=keypad
        self.keypad_map=keypad_map
        # self.text_buffer_uploader=text_buffer_uploader

    def start_typing(self):
        key_inp=self.keypad.keypad_loop()
        # print(key_inp[0], key_inp[1])
        text=self.keypad_map.key_out(col=int(key_inp[0]), row=int(key_inp[1]))
        # print(key_inp[0], key_inp[1])
        # text=self.keypad_map.key_out(tuple(key_inp))
        
        # self.text_buffer_uploader.t_b.update_buffer(text)
        return text
        # self.text_buffer_uploader.refresh()
