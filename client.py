import time
from threading import Thread

from connection import Connection
from whiteboard import WhiteBoard


class Client(Thread,WhiteBoard):
    Objects = {'line': 'L', 'oval': 'O', 'circle': 'C', 'rectangle': 'R', 'square': 'S', 'erase': 'E', 'drag': 'DR'}

    def __init__(self):
        self.conn = Connection()
        Thread.__init__(self)
        WhiteBoard.__init__(self)
        self._init_mouse_event()
        self.setDaemon(True)
        self.isMouseDown = False
        self.x_pos = None
        self.y_pos = None
        self.last_time = None

        self.line_x1,self.line_y1,self.line_x2,self.line_y2 = None, None, None, None

    def _init_mouse_event(self):
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_but_up)


    def left_but_down(self,event=None):
        self.isMouseDown = True
        self.x_pos = event.x
        self.y_pos = event.y
        self.last_time = time.time()
        self.line_x1, self.line_y1 = event.x,event.y


    def left_but_up(self,event=None):
        self.isMouseDown = False
        print(event.x,event.y)
        self.last_time = None
        self.line_x2, self.line_y2 = event.x, event.y
        self.draw_one_obj()

    def draw_one_obj(self):
        tool = self.drawing_tool
        if tool not in Client.Objects.keys():
            return
        else:
            cmd_type = Client.Objects[tool]
            msg = (cmd_type, self.line_x1, self.line_y1, self.line_x2, self.line_y2, 'red')
            self.conn.send_message(msg)



    def motion(self,event=None):
        if self.isMouseDown == True and self.drawing_tool == 'pencil':
            now = time.time()
            if now - self.last_time < 0.02:
                print('too fast')
                return

            self.last_time = now

            msg = ('D',self.x_pos,self.y_pos,event.x,event.y,'red')
            self.conn.send_message(msg)
            self.x_pos = event.x
            self.y_pos = event.y


    def run(self):

        while True:
            msg = self.conn.receive_msg()
            self.draw_from_msg(msg)
            print(msg)
            if msg == 'xxx':
                pass


if __name__ == '__main__':
    client = Client()
    print('startt')
    client.start()
    client.show_window()




