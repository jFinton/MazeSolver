from graphics import *

def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.draw(Point(50,50), Point(100,100))

    cell = Cell(win)
    cell.has_bottom = False
    cell.draw(Point(100,100), Point(150,150))

    cell = Cell(win)
    cell.has_left = False
    cell.has_right = False
    cell.draw(Point(175,175), Point(225,225))

    win.wait_for_close()



if __name__ == "__main__":
    main()