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
    

    def buffer(self):
        rows_list=[]
        if len(self.text_buffer)%self.cols!=0:
            self.no_last_spaces=self.cols-len(self.text_buffer)%self.cols
            for i in range(0,self.cols-len(self.text_buffer)%self.cols):
                self.text_buffer+=" "
                self.menu_buffer_size=len(self.text_buffer)
                self.menu_buffer=list(range(self.menu_buffer_size))
        while len(self.text_buffer)<=self.display_buffer[-1] or len(self.text_buffer)<self.rows*self.cols:
            self.no_last_spaces+=1
            self.text_buffer+=" "
            self.menu_buffer_size=len(self.text_buffer)
            self.menu_buffer=list(range(self.menu_buffer_size))
        self.display_buffer=self.menu_buffer[self.display_buffer_position:self.display_buffer_position+self.rows*self.cols]
        counter=0
        for i in range(self.rows):
            row=""
            for j in range(self.cols):
                if counter >= len(self.display_buffer):
                    row+="/t"
                elif self.display_buffer[counter]==self.menu_buffer_cursor:
                    row+="|"+str(self.text_buffer[self.display_buffer[counter]])
                else:
                    row+=""+str(self.text_buffer[self.display_buffer[counter]])
                counter+=1
            rows_list.append(row)
        return rows_list
    
    def update_buffer(self, text):
        if text=="nav_d" or text =="nav_r":
            if text=="nav_d":
                self.menu_buffer_cursor+=self.cols
            else:
                self.menu_buffer_cursor+=1
            if self.menu_buffer_cursor >= len(self.menu_buffer)-self.no_last_spaces:
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
                self.menu_buffer_cursor=len(self.menu_buffer)-self.no_last_spaces-1
                self.display_buffer_position=len(self.menu_buffer)-self.rows*self.cols
            elif self.menu_buffer_cursor < self.display_buffer[0]:
                self.display_buffer_position-=self.cols
        elif text=="nav_b":
            if self.menu_buffer_cursor < 0:
                self.menu_buffer_cursor=0
                self.display_buffer_position=0
            elif self.menu_buffer_cursor < self.display_buffer[0]:
                self.text_buffer=self.text_buffer[0:self.menu_buffer_cursor-1]+self.text_buffer[self.menu_buffer_cursor:len(self.text_buffer)]
                self.display_buffer_position-=self.cols
                self.menu_buffer_size=len(self.text_buffer)
                self.menu_buffer_cursor-=1
            elif self.menu_buffer_cursor > 0 and self.menu_buffer_cursor>=self.display_buffer[0]:
                self.text_buffer=self.text_buffer[0:self.menu_buffer_cursor-1]+self.text_buffer[self.menu_buffer_cursor:len(self.text_buffer)]
                self.menu_buffer_size=len(self.text_buffer)
                self.menu_buffer_cursor-=1
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