# 5)
import json
import os, pathlib

current_path = pathlib.Path().resolve()
file = os.path.join(current_path, 'db.json')
print("торговых автомат")
money1 = int(input("количество денег: "))


class Torgovy:
    def __init__(self, money, string) -> None:
        self.money = money
        self.string = string
        self.money1 = 0

    def indekator(self):
        while True:
            print("1)kupit tovar \n2)moi vy kupki \n3)vy hod")
            a1 = int(input("menu: "))
            if a1 == 1:
                print(
                    "1)Nitro=120som \n2)Flesh=80som \n3)pepsi=135som \n4)kinder=55som \n5)Alpenkold=85som \n6)chupachup=5som"
                )
                a = int(input("menu: "))
                if a == 1:
                    if self.money >= 120:
                        self.money -= 120
                        self.money1 += 120
                        self.string += "Nitro" + " "
                    else:
                        print(f"dengi nehvataet na Nitro u vas est tolka {self.money}")
                elif a == 2:
                    if self.money >= 80:
                        self.money -= 80
                        self.money1 += 80
                        self.string += "Flesh" + " "
                    else:
                        print(f"dengi nehvataet na Flesh u vas est tolka {self.money}")
                elif a == 3:
                    if self.money >= 135:
                        self.money -= 135
                        self.money1 += 135
                        self.string += "pepsi" + " "
                    else:
                        print(f"dengi nehvataet na pepsi u vas est tolka {self.money}")
                elif a == 4:
                    if self.money >= 55:
                        self.money -= 55
                        self.money1 += 55
                        self.string += "kinder" + " "
                    else:
                        print(f"dengi nehvataet na kinder u vas est tolka {self.money}")
                elif a == 5:
                    if self.money >= 85:
                        self.money -= 85
                        self.money1 += 85
                        self.string += "Alpenkold" + " "
                    else:
                        print(f"dengi nehvataet na Alpenkold u vas est tolka {self.money}")
                elif a == 6:
                    if self.money >= 5:
                        self.money -= 5
                        self.money1 += 5
                        self.string += "chupachup" + " "
                    elif self.money == 0:
                        print(f"vy ne mojete kupit u vas astalsya 0")
                        break
                    else:
                        print(f"vy ne mojete kupit u vas astalsiya tolka menshe 5som")
                        break
            elif a1 == 2:
                m = self.string.split(" ")
                m.pop(-1)
                print(m)
            if self.money <5:
                    break
            else:
                break
    def json_file(self):
        b = self.string.split(" ")
        b.pop(-1)
        id = 0
        try:
            with open(file, "r") as file1:
                data = json.load(file1)
                ali = data[-1]["id"]
                id = id + ali
        except:
            data = []
        for i in b:
            if i == "Nitro":
                data.append({"id": id + 1, "name": i, "money": 120})
            elif i == "Flesh":
                data.append({"id": id + 1, "name": i, "money": 80})
            elif i == "pepsi":
                data.append({"id": id + 1, "name": i, "money": 135})
            elif i == "kinder":
                data.append({"id": id + 1, "name": i, "money": 55})
            elif i == "Alpenkold":
                data.append({"id": id + 1, "name": i, "money": 85})
            elif i == "chupachup":
                data.append({"id": id + 1, "name": i, "money": 5})
        with open(file, "w") as file1:
            json.dump(data, file1, indent=4)

    def informasiya(self):
        with open(file, "r") as file1:
            data = json.load(file1)
            print(data)


abu = Torgovy(money1, "")
abu.indekator()
abu.json_file()
# abu.informasiya()

# 50/50