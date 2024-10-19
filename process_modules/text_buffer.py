class Textbuffer:
    def __init__(self, text_buffer=" ", rows=8, cols=20):
        self.text_buffer=text_buffer
        self.menu_buffer_size=len(self.text_buffer)
        self.menu_buffer=list(range(self.menu_buffer_size))
        self.menu_buffer_cursor=0
        self.rows=rows                                  
        self.cols=cols
        self.display_buffer_position=0
        self.display_buffer=self.menu_buffer[self.display_buffer_position:self.display_buffer_position+self.rows*self.cols]
        self.no_last_spaces=0
        self.buffer_length=len(self.text_buffer)
    
    def buffer(self):            
        # rows_list = []
        
        # Calculate the number of spaces needed to make the buffer length a multiple of cols
        self.buffer_length = len(self.text_buffer)
        remaining_spaces = self.cols - (self.buffer_length % self.cols) if self.buffer_length % self.cols != 0 else 0
        self.no_last_spaces = remaining_spaces
        
        # Append all necessary spaces at once to avoid repeated string concatenation
        if remaining_spaces > 0:
            self.text_buffer += " " * remaining_spaces
        
        # Calculate the menu_buffer only once
        self.menu_buffer_size = len(self.text_buffer)
        self.menu_buffer = list(range(self.menu_buffer_size))
        
        # Ensure text_buffer has enough characters to fill display buffer
        total_buffer_size = self.rows * self.cols
        if len(self.text_buffer) < total_buffer_size:
            extra_spaces = total_buffer_size - len(self.text_buffer)
            self.text_buffer += " " * extra_spaces
            self.menu_buffer_size = len(self.text_buffer)
            self.menu_buffer = list(range(self.menu_buffer_size))

        # Slicing menu_buffer to create the display buffer
        self.display_buffer = self.menu_buffer[self.display_buffer_position:self.display_buffer_position + total_buffer_size]
        new_rows_list=[]

        for i in range(self.rows):
      
            rownew=self.text_buffer[self.display_buffer[self.cols*i]:self.display_buffer[self.cols*i+self.cols-1]+1]
            new_rows_list.append(rownew)
        buff_index=self.display_buffer.index(self.menu_buffer_cursor)
        new_rows_list[buff_index//self.cols]=new_rows_list[buff_index//self.cols][0:buff_index%self.cols]+"|"+new_rows_list[buff_index//self.cols][buff_index%self.cols:self.cols]
        return new_rows_list


    def update_buffer(self, text):
        if text=="nav_d" or text =="nav_r":
            if text=="nav_d":
                self.menu_buffer_cursor+=self.cols
            else:
                self.menu_buffer_cursor+=1
            # if self.menu_buffer_cursor >= len(self.menu_buffer)-self.no_last_spaces:
            if self.menu_buffer_cursor >= self.buffer_length:
                self.menu_buffer_cursor=0
                self.display_buffer_position=0
            elif self.menu_buffer_cursor > self.display_buffer[-1]:
                self.display_buffer_position+=self.cols
        elif text=="nav_u" or text=="nav_l":
            if text=="nav_u":
                self.menu_buffer_cursor-=self.cols
            else:
                self.menu_buffer_cursor-=1
            if self.menu_buffer_cursor < 0:
                if len(self.text_buffer)<=self.rows*self.cols:
                    self.menu_buffer_cursor=self.buffer_length-1
                else:
                    self.menu_buffer_cursor=len(self.menu_buffer)-self.no_last_spaces-1
                self.display_buffer_position=len(self.menu_buffer)-self.rows*self.cols
            elif self.menu_buffer_cursor < self.display_buffer[0]:
                self.display_buffer_position-=self.cols

        elif text == "nav_b":
            # Handle backspace when the cursor is at the start of the buffer
            if self.menu_buffer_cursor <= 0:
                # Prevent cursor from going negative and ensure display starts at 0
                self.menu_buffer_cursor = 0
                self.display_buffer_position = 0
            else:
                # Remove the character before the cursor and adjust the buffer
                self.text_buffer = self.text_buffer[:self.menu_buffer_cursor - 1] + self.text_buffer[self.menu_buffer_cursor:]
                self.menu_buffer_cursor -= 1
                self.menu_buffer_size = len(self.text_buffer)
                
                # Ensure that display position is adjusted accordingly
                if self.menu_buffer_cursor < self.display_buffer[0]:
                    self.display_buffer_position = max(0, self.display_buffer_position - self.cols)

        else:
            self.text_buffer=self.text_buffer[0:self.menu_buffer_cursor]+text+self.text_buffer[self.menu_buffer_cursor:len(self.text_buffer)]
            self.menu_buffer_size+=len(text)
            self.menu_buffer=list(range(self.menu_buffer_size))
            self.menu_buffer_cursor+=len(text)
            if self.menu_buffer_cursor>self.display_buffer[-1]:
                self.display_buffer_position=self.menu_buffer_cursor-self.menu_buffer_cursor%self.cols-((self.rows-1)*self.cols)
        self.text_buffer=self.text_buffer.strip()+" "
    def all_clear(self):
        """Reset the buffer and cursor positions."""
        self.text_buffer = " "
        self.menu_buffer_size = len(self.text_buffer)
        self.menu_buffer = list(range(self.menu_buffer_size))
        self.menu_buffer_cursor = 0
        self.display_buffer_position = 0
        self.no_last_spaces = 0                            
