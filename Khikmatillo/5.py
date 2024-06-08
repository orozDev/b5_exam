# import json

# length = 0
# file1 = r"C:\Users\User\Desktop\всё\мой труд\егзамен питон\задача1\exzem.json"
# def main():

#     while True:
#         print("старт тестов")
#         print("1. просмотр ")
#         print("2. Создать тест")
#         print("3. Удалить тест")
#         print("4. Выход")
#         choice = int(input("Введите номер действия "))
#         if choice == 1:
#             try:
#                 with open(file1, "r") as file:
#                     data02 = json.load(file)
#                     id_input = int(input("Введите ID: "))
#                     found = False
#                     for item in data02:
#                         if item["id"] == id_input:
#                             print(item)
#                             found = True
#                             break 
#                     if not found:
#                         print("Такого айди нету")
#             except FileNotFoundError:
#                 print("Файл не найден")


#         elif choice == 2:
#             test_question = input("Введите вопрос теста: ")
#             variant_a = input("Введите вариант a ")
#             variant_b = input("Введите вариант b ")
#             variant_c = input("Введите вариант c ")
#             variant_d = input("Введите вариант d ")
#             try:
#                 with open(file1, 'r+') as file:
#                     data = json.load(file)
#                     length = len(data) + 1
#                     test_data = {
#                         "id": length,
#                         "test_question": test_question,
#                         "a": variant_a,
#                         "b": variant_b,
#                         "c": variant_c,
#                         "d": variant_d
#                     }
#                     data.append(test_data)
#                     file.seek(0)
#                     file.truncate() 
#                     json.dump(data, file, indent=4)
#                 print("Тест успешно создан")
#             except FileNotFoundError:
#                 print("Файл не найден")


#         elif choice == 3:
#             try:
#                 test_id = int(input("Введите айди  теста для удаления "))
#                 with open(file1, 'r+') as file:
#                     data = json.load(file)
#                     data = [item for item in data if item["id"] != test_id]
#                     file.seek(0) 
#                     file.truncate()  
#                     json.dump(data, file, indent=4)
#                 print(f"Тест с ID {test_id} успешно удален")
#             except FileNotFoundError:
#                 print("Файл не найден")
#         elif choice == 4:
#             print("Выход из программы")
#             break

#         else:
#             print(" Введите номер от 1 до 4.")

# class Quiz:
#     def __init__(self, question: str, point: int, a, b, c, d, **kwargs) -> None:
#         self.question = question
#         self.point = point
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
        
#         for key, value in kwargs.items():
#             self.__setattr__(key, value)

#         print(f"Вопрос {self.question} создался")
#         with open(file1, "r+") as file:
#             datas_ = json.load(file)
#             length = len(datas_) + 1
#             data = {
#                 "id": length,
#                 "test_question": self.question,
#                 "a": self.a,
#                 "b": self.b,
#                 "c": self.c,
#                 "d": self.d
#             }
#             datas_.append(data)
#         with open(file1, "w") as file:
#             json.dump(datas_, file, indent=4)
    
#     @property
#     def is_true(self):
#         return self.__getattribute__('true')
    
#     @property
#     def info(self):
#         a = self.__dict__.copy()
#         a.pop('question')
#         a.pop('true')
#         return a

#     def to_check(self, option):
#         if self.is_true == option:
#             return True
#         return False

# class Test:
#     def __init__(self, name, questions: list[Quiz], user) -> None:
#         self.questions = questions
#         self.name = name
#         self.user = user
#         self.right_answers = 0
#         self.points = 0

#     def statistics(self):
#         print(f"Статистика теста {self.name}, Участник {self.user}")
#         print(f"Правильных ответов {self.right_answers}")
#         print(f"Неправильных ответов {len(self.questions) - self.right_answers}")
#         print(f"Всего баллов {self.points}")

#     def start(self):
#         for question in self.questions:
#             print(question.question)
#             for key, value in question.info.items():
#                 print(f"{key}: {value}")
#             option = input("Ваш ответ: ")
#             if question.to_check(option):
#                 self.right_answers += 1
#                 self.points += question.point
#                 print("Правильно")
#             else:
#                 print("Неправильно")
#         self.statistics()

# if __name__ == "__main__":
#     main()


# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# oroz
# Сделайте консольное приложение торговых автоматов. Где программа будет сначала спрашивать количество денег.
#  И будет предлагать на выбор различные напитки и сладости. Должна быть возможность купить желаемые напитки и т д.
#  Должно присутствовать индикатор баланса. Нужно все это реализовать с помощью классов и с использованием json базы данных.
# //////////////////////////////////////////////////////////////////////////////////////////
import json
def main():
    while True:
        print("добро пожаловать \n  ")
        price = int(input("Введите вашу сумму"))
        print("что хотите")
        print("1. сладкое")
        print("2. напитки")
        print("3. Выход")
        schot = price
        choice = int(input("Введите номер действия "))
        if choice == 1:
            print("1. наполеон")
            print("2. медовика")
            vybor = int(input("Введите номер действия "))
            if vybor == 1:
                if schot < 200:
                    print("у вас не хвотает денег")
                else:
                    schot - 200
                    print("с вашего счета снято 200 сомов")
            elif vybor == 2:
                    if schot < 200:
                        print("у вас не хвотает денег")
                    else:
                        schot - 200
                        print("с вашего счета снято 150 сомов")
        if choice == 2:
                print("1. pepci")
                print("2. cola")
                vybor2 = int(input("Введите номер действия "))
                if vybor2 == 1:
                    if schot < 200:
                        print("у вас не хвотает денег")
                    else:
                        schot - 200
                        print("с вашего счета снято 200 сомов")
                elif vybor2 == 2:
                    if schot < 200:
                        print("у вас не хвотает денег")
                    else:
                        schot - 200
                        print("с вашего счета снято 150 сомов")
               

# 50/50