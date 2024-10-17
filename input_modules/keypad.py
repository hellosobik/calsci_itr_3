from machine import Pin  # type: ignore
import utime as time #type: ignore

class Keypad:
    # Instance attribute
    def __init__(self, rows, cols):
        self.rows=rows
        self.cols=cols
        for pin in cols:
            Pin(pin, Pin.IN, Pin.PULL_UP)

        # Set column pins as OUTPUT and HIGH
        for pin in rows:
            p = Pin(pin, Pin.OUT)
            p.value(1)
        self.state=True
    def keypad_loop(self):    
        # global numRows, rowPins, numCols, colPins, graph_letters
        while self.state==True:
            for row in range(len(self.rows)):

                Pin(self.rows[row], Pin.OUT).value(0)
                for col in range(len(self.cols)):
                    buttonState = Pin(self.cols[col], Pin.IN, Pin.PULL_UP).value()
                    
                    if buttonState == 0:
                        # str=default_key(row, col)
                        # time.sleep(0.4)  # Debounce delay
                        Pin(self.rows[row], Pin.OUT).value(1)
                        # time.sleep(0.3)  # Debounce delay
                        col_row=(col, row)
                        return col_row
                Pin(self.rows[row], Pin.OUT).value(1)
    def keypad_stop(self):
        self.state=False

    def keypad_start(self):
        self.state=True