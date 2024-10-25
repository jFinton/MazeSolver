from graphics import *

def main():
    win = Window(800, 600)

    line1 = Line(Point(20, 40), Point(200,40))
    line2 = Line(Point(50, 200), Point(100, 400))
    win.draw_line(line1, "black")
    win.draw_line(line2, "blue")

    win.wait_for_close()



if __name__ == "__main__":
    main()