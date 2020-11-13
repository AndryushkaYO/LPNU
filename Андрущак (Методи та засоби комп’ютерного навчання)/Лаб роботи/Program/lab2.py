from graphics import *

#  TASK 1


def task_1():
    colors = ['red', 'yellow', 'green', 'blue', 'pink', 'orange']
    # Part 1

    def task_1_1():
        win = GraphWin('TASK 1.1', 200, 200)
        for i in range(3):
            circle = Circle(Point(100, 50 * (i + 1)), 25)
            circle.setFill(colors[i])
            circle.setOutline('black')
            circle.setWidth(1)
            circle.draw(win)
        Rectangle(Point(75, 25), Point(125, 175)).draw(win)
        win.getMouse()
        win.close()

    # Part 2

    def task_1_2():
        win = GraphWin('TASK 1.2', 420, 120)
        d = 0
        for i in range(6):
            d += (60 - i * 10)
            circle = Circle(Point(d, 60), (60 - i * 10))
            circle.setFill(colors[i])
            circle.setOutline('black')
            circle.setWidth(1)
            circle.draw(win)
            d += (60 - i * 10)
        win.getMouse()
        win.close()

    task_1_1()
    task_1_2()


task_1()


#  TASK 2


def task_2():
    win = GraphWin('TASK 2', 300, 300)
    win.setBackground('white')
    points = []
    for i in range(5):
        points.append(win.getMouse())
        print(points[i])
    polygon = Polygon(points)
    polygon.setFill('orange')
    polygon.draw(win)

    win.getMouse()
    win.close()


for i in range(2):
    task_2()

# TASK 3


def task_3():
    def initialize_board(filename):
        infile = open(filename, 'r')
        board = []
        for i in range(5):
            board.append([])
        for row in range(5):
            for col in range(5):
                columnvalue = eval(infile.readline())
                board[row].append(columnvalue)
        return board

    def draw_lines(window):
        s_x = 0
        s_y = 250
        for i in range(4):
            Line(Point(0, 50*(i+1)), Point(250, 50*(i+1))).draw(window)
            if i == 3:
                s_x = 250
                s_y = 0
            Line(Point(50*(i+1), s_x), Point(50*(i+1), s_y)).draw(window)

    def display_lights(window, board):
        for row in range(5):
            for column in range(5):
                center = Point(column * 50 + 25, row * 50 + 25)
                circ = Circle(center, 25)
                if board[row][column] == 1:
                    circ.setFill('lightpink')
                else:
                    circ.setFill('white')
                circ.draw(window)

    def update_board(board, row, column):
        board[row][column] = (board[row][column] + 1) % 2
        if row > 0:
            board[row - 1][column] = (board[row - 1][column] + 1) % 2
        if row < 4:
            board[row + 1][column] = (board[row + 1][column] + 1) % 2
        if column > 0:
            board[row][column - 1] = (board[row][column - 1] + 1) % 2
        if column < 4:
            board[row][column + 1] = (board[row][column + 1] + 1) % 2

    def check_for_winner(board):
        sum = 0
        for row in range(5):
            for column in range(5):
                sum = sum + board[row][column]
        if sum == 0:
            return True
        else:
            return False

    def clear(win):
        for item in win.items[:]:
            item.undraw()
        win.update()

    def main():
        window = GraphWin('Lights Out', 250, 250)
        board = initialize_board('lights.txt')
        draw_lines(window)
        display_lights(window, board)
        game_over = False
        while not game_over:
            p = window.getMouse()
            column = p.getX() / 50
            row = p.getY() / 50
            update_board(board, int(row), int(column))
            display_lights(window, board)
            game_over = check_for_winner(board)
        message = Text(Point(125, 125), 'GAME OVER')
        message.setSize(24)
        message.setTextColor('red')
        clear(window)
        message.draw(window)
        window.getMouse()
        window.close()

    main()


task_3()


# TASK 4

def task_4():
    def initialize_board(filename):
        infile = open(filename, 'r')
        board = []
        for i in range(5):
            board.append([])
        for row in range(5):
            for col in range(5):
                columnvalue = eval(infile.readline())
                board[row].append(columnvalue)
        return board

    def display_numbers(window, board):
        for row in range(5):
            for col in range(5):
                square = Rectangle(Point(col * 50, row * 50), Point((col + 1) * 50, (row + 1) * 50))
                square.setFill('snow')
                square.setOutline('maroon')
                square.draw(window)
                if board[row][col] != 0:
                    center = Point(col * 50 + 25, row * 50 + 25)
                    number = Text(center, board[row][col])
                    number.setSize(24)
                    number.setTextColor('crimson')
                    number.draw(window)

    def update_board(board, row, col):
        if row > 0 and board[row - 1][col] == 0:
            board[row - 1][col] = board[row][col]
            board[row][col] = 0
            return
        if row < 4 and board[row + 1][col] == 0:
            board[row + 1][col] = board[row][col]
            board[row][col] = 0
            return
        if col > 0 and board[row][col - 1] == 0:
            board[row][col - 1] = board[row][col]
            board[row][col] = 0
            return
        if col < 4 and board[row][col + 1] == 0:
            board[row][col + 1] = board[row][col]
            board[row][col] = 0
            return

    def check_for_winner(board):
        num = 1
        row = 0
        col = 0
        while num <= 24:
            if board[row][col] == num:
                num = num + 1
                col = col + 1
                if col > 4:
                    col = 0
                    row = row + 1
            else:
                return False
        return True

    def clear(win):
        for item in win.items[:]:
            item.undraw()
        win.update()

    def main():
        window = GraphWin('GAME 25', 250, 250)
        board = initialize_board('game_25.txt')
        display_numbers(window, board)
        game_over = False
        while not game_over:
            p = window.getMouse()
            col = int(p.getX() / 50)
            row = int(p.getY() / 50)
            update_board(board, row, col)
            display_numbers(window, board)
            game_over = check_for_winner(board)
        message = Text(Point(125, 125), 'GAME OVER')
        message.setSize(24)
        message.setTextColor('red')
        clear(window)
        message.draw(window)
        window.getMouse()
        window.close()

    main()


task_4()
