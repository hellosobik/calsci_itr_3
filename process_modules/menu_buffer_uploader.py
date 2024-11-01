class Tbf:
    def __init__(self, disp_out, chrs, m_b):
        self.disp_out=disp_out
        self.chrs=chrs
        self.m_b=m_b
        self.disp_out.clear_display()

    def refresh(self):
        buf=self.m_b.buffer()
        ref_ar=self.m_b.ref_ar()
        for i in range(0, self.m_b.menu_display_size):
            self.disp_out.set_page_address(i)
            self.disp_out.set_column_address(0)
            buf[i]+=" "*(self.m_b.cols-len(buf[i]))
            for j in buf[i]:
                if i == self.m_b.cursor():
                    chtr_byte_data=self.chrs.invert_letter(j)
                    cursor_line=0b11111111
                    for k in chtr_byte_data:
                        self.disp_out.write_data(k)
                    self.disp_out.write_data(cursor_line)
                else:
                    chtr_byte_data=self.chrs.Chr2bytes(j)
                    cursor_line=0b00000000
                    for k in chtr_byte_data:
                        self.disp_out.write_data(k)
                    self.disp_out.write_data(cursor_line)