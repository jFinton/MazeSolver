from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.is_running = False

        self.root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()
        
    def close(self):
        self.is_running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)
    

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line():
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas: Canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)


class Cell():
    def __init__(self, win: Window):
        self.has_left = True
        self.has_right = True
        self.has_top = True
        self.has_bottom = True
        self.p1 = None
        self.p2 = None
        self.win = win
    
    def draw(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
        if self.has_left:
            line = Line(self.p1, Point(self.p1.x, self.p2.y))
            self.win.draw_line(line, "black")
        if self.has_right:
            line = Line(Point(self.p2.x, self.p1.y), self.p2)
            self.win.draw_line(line, "black")
        if self.has_top:
            line = Line(self.p1, Point(self.p2.x, self.p1.y))
            self.win.draw_line(line, "black")
        if self.has_bottom:
            line = Line(Point(self.p1.x, self.p2.y), self.p2)
            self.win.draw_line(line, "black")
    

    def draw_move(self, to_cell, undo=False):
        cell_center = Point((self.p2.x + self.p1.x) / 2, (self.p2.y + self.p1.y) / 2)
        print(f"{cell_center.x}, {cell_center.y}")
        to_cell_center = Point((to_cell.p2.x + to_cell.p1.x) / 2, (to_cell.p2.y + to_cell.p1.y) / 2)
        fill_color = "gray" if undo == True else "red"
        line = Line(cell_center, to_cell_center)
        self.win.draw_line(line, fill_color=fill_color)