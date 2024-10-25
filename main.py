from graphics import *

def main():
    win = Window(800, 600)

    cell1 = Cell(win)
    cell1.has_right = False
    cell1.draw(Point(50,50), Point(100,100))

    cell2 = Cell(win)
    cell2.has_bottom = False
    cell2.has_left = False
    cell2.draw(Point(100,50), Point(150,100))

    cell1.draw_move(cell2, True)

    win.wait_for_close()



if __name__ == "__main__":
    main()