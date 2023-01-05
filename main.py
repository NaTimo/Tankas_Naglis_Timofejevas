import random


class Tankas:
    def __init__(self):
        self.x = []
        self.y = []
        self.kryptis = ["šiaurę"]
        self.suviu_dic = {"Šūviai šiaurės kryptimi: ": 0, "Šūviai pietų kryptimi: ": 0, "Šūviai vakarų kryptimi ": 0,
                          "Šūviai rytų kryptimi ": 0}
        sum(self.suviu_dic.values())

    def pirmyn(self):
        self.y.append(1)
        self.kryptis[0] = "šiaurę"

    def atgal(self):
        self.y.append(-1)
        self.kryptis[0] = "pietus"

    def kairen(self):
        self.x.append(-1)
        self.kryptis[0] = "vakarus"

    def desinen(self):
        self.x.append(1)
        self.kryptis[0] = "rytus"

    def suvis(self):
        if self.kryptis[0] == "šiaurę":
            self.suviu_dic["Šūviai šiaurės kryptimi: "] += 1

        if self.kryptis[0] == "pietus":
            self.suviu_dic["Šūviai pietų kryptimi: "] += 1

        if self.kryptis[0] == "vakarus":
            self.suviu_dic["Šūviai vakarų kryptimi "] += 1

        if self.kryptis[0] == "rytus":
            self.suviu_dic["Šūviai rytų kryptimi "] += 1

    def info(self):
        return print("Tankas šiuo metu atsisukę į", self.kryptis[0], "\nTanko kordinatės: \nx: ", sum(self.x), " \ny: ",
                     sum(self.y), "\nIšviso atliko", sum(self.suviu_dic.values()), "šūvių", "\nIš kurių: ",
                     self.suviu_dic)

    def koor_x(self):
        return sum(self.x)

    def koor_y(self):
        return sum(self.y)

    def direction(self):
        return self.kryptis[0]


tank_obj = Tankas()

h_line = "-  " * 10
asis_0 = "|  " * 21
asis_x = f"{asis_0}\n"
one_line = f"{h_line}|  {h_line}\n"
h_board = one_line * 10
board = f"{h_board}{asis_x}{h_board}"

enemy_x = random.randint(-10, 10)
enemy_y = random.randint(-10, 10)
enemy_index = (11 - enemy_y) * 64 - 1 - (11 - enemy_x) * 3

first_index = 670

if enemy_index < first_index:
    board = board[:enemy_index] + "E" + board[enemy_index + 1:first_index] + "P" + board[first_index + 1:]
else:
    board = board[:first_index] + "P" + board[first_index + 1:enemy_index] + "E" + board[enemy_index + 1:]
print(board)
points = [100, ]
print(f"Taškai: {sum(points)}")
tank_obj.info()

while True:
    if sum(points) == 0:
        print("\nPabaiga")
        break
    meniu = input("\nw - pirmyn \ns - atgal \na - kairėn \nd - dešinėn \nf - šauti \nb - baigti žaidimą")

    match meniu:
        case "w":
            if tank_obj.koor_y() < 10:
                tank_obj.pirmyn()
                points.append(-10)
        case "s":
            if tank_obj.koor_y() > -10:
                tank_obj.atgal()
                points.append(-10)
        case "a":
            if tank_obj.koor_x() > -10:
                tank_obj.kairen()
                points.append(-10)
        case "d":
            if tank_obj.koor_x() < 10:
                tank_obj.desinen()
                points.append(-10)
        case "f":
            tank_obj.suvis()
            if tank_obj.koor_y() == enemy_y:
                if enemy_x > tank_obj.koor_x() and tank_obj.direction() == "rytus":
                    board = board.replace("E", "d")
                    points.append(50)
                if enemy_x < tank_obj.koor_x() and tank_obj.direction() == "vakarus":
                    board = board.replace("E", "d")
                    points.append(50)
            if tank_obj.koor_x() == enemy_x:
                if enemy_y > tank_obj.koor_y() and tank_obj.direction() == "šiaurę":
                    board = board.replace("E", "d")
                    points.append(50)
                if enemy_y < tank_obj.koor_y() and tank_obj.direction() == "pietus":
                    board = board.replace("E", "d")
                    points.append(50)

        case "b":
            print("\nPabaiga")
            break

    enemy_index = board.find("E")

    if enemy_index < 0:
        enemy_x = random.randint(-10, 10)
        enemy_y = random.randint(-10, 10)
        enemy_index = (11 - enemy_y) * 64 - 1 - (11 - enemy_x) * 3

    h_line = "-  " * 10
    asis_0 = "|  " * 21
    asis_x = f"{asis_0}\n"
    one_line = f"{h_line}|  {h_line}\n"
    h_board = one_line * 10
    board = f"{h_board}{asis_x}{h_board}"

    player_index = (11 - tank_obj.koor_y()) * 64 - 1 - (11 - tank_obj.koor_x()) * 3

    if enemy_index < player_index:
        board = board[:enemy_index] + "E" + board[enemy_index + 1:player_index] + "P" + board[player_index + 1:]
    else:
        board = board[:player_index] + "P" + board[player_index + 1:enemy_index] + "E" + board[enemy_index + 1:]

    print(board)
    print("Taškai:")
    print(sum(points))

    tank_obj.info()
