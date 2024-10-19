class Tbf:
    def __init__(self, disp_out, chrs, t_b):
        self.disp_out=disp_out
        self.chrs=chrs
        self.t_b=t_b
        self.disp_out.clear_display()
        # self.buf=self.t_b.buffer()
    def update(self, t_b_new):
        self.t_b=t_b_new
    def refresh(self):
        # self.disp_out.clear_display()
        buf=self.t_b.buffer()
        # print(buf)
        for i in range(len(buf)):
            self.disp_out.set_page_address(i)
            self.disp_out.set_column_address(0)
            if buf[i].strip() != "":

                for j in buf[i]:
                    chtr=j
                    # print(buf[i])
                    # print(chtr)
                    # print(str(chtr))
                    chtr_byte_data=self.chrs.Chr2bytes(chtr)
                    for k in chtr_byte_data:
                        self.disp_out.write_data(k)
                    self.disp_out.write_data(0b00000000)
                for k in range(8):
                    self.disp_out.write_data(0b00000000)
            else:
                for k in range(8):
                    self.disp_out.write_data(0b00000000)