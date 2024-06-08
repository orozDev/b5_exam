# 6) zadacha
# import json

# class Avtomat:
#     def __init__(self):
#         self.products = self.load_products()
#         self.balance = 0

#     def load_products(self):
#         with open('D:\Материалы\python\egzamen\egzamen1\products.json', 'r') as file:
#             return json.load(file)

#     def save_products(self):
#         with open('D:\Материалы\python\egzamen\egzamen1\products.json', 'w') as file:
#             json.dump(self.products, file, indent=4)

#     def show_products(self):
#         print("товары:")
#         for product, details in self.products.items():
#             print(f"{product}: {details['price']} com")

#     def add_money(self, amount):
#         self.balance += amount
#         print(f"dobavil {amount} com.balans {self.balance} com")

#     def buy_product(self, product):
#         if product in self.products:
#             price = self.products[product]['price']
#             if self.balance >= price:
#                 self.balance -= price
#                 print(f"kypil {product} za {price} com. na balance ostalos: {self.balance} com")
#                 self.products[product]['quantity'] -= 1
#                 self.save_products()
#             else:
#                 print("net deneg")
#         else:
#             print("tovar nety")

#     def run(self):
#         self.show_products()
#         while True:
#             action = input("\nvyberi deistvie  (1) kypit tovar, (2) exit \n")
#             amount = float(input("vvedi symmu \n"))
#             self.add_money(amount)
#             if action == '1':
#                 product = input("vvedi imya tovara\n")
#                 self.buy_product(product)
#             elif action == '2':
#                 print("vyhod..")
#                 break
#             else:
#                 print(" ")

# Avtomat().run()



# 5)zadacha

import json
import os
import pathlib

class Quiz:
    def __init__(self, question: str, point: int, **kwargs) -> None:
        self.question = question
        self.point = point
        for key, value in kwargs.items():
            self.__setattr__(key, value)
        print(f"Вопрос '{self.question}' создался")

    @property
    def is_true(self):
        return self.__getattribute__('true')

    @property
    def info(self):
        a = self.__dict__.copy()
        a.pop('question')
        a.pop('true')
        return a

    def to_check(self, option):
        return self.is_true == option

class Test:
    def __init__(self, name: str, questions: list[Quiz], user: str) -> None:
        self.questions = questions
        self.name = name
        self.user = user
        self.right_answers = 0
        self.points = 0

    def statistics(self):
        print(f"Статистика теста '{self.name}', Участник: {self.user}")
        print(f"Правильных ответов: {self.right_answers}")
        print(f"Неправильных ответов: {len(self.questions) - self.right_answers}")
        print(f"Всего баллов: {self.points}")

    def start(self):
        for question in self.questions:
            print(question.question)
            for key, value in question.info.items():
                print(f"{key}: {value}")
            option = input("Ваш ответ: ")
            if question.to_check(option):
                self.right_answers += 1
                self.points += question.point
                print("Правильно")
            else:
                print("Неправильно")
        self.statistics()

class QuizManager:
    def __init__(self):
        self.quizzes = self.load_quizzes()
        current_path = pathlib.Path().resolve()
        self.file_path = os.path.join(current_path, 'quizzers.json')
        print(self.file_path)

    def save_quizzes(self):
        with open(self.file_path, 'w') as file:
            json.dump([q.__dict__ for q in self.quizzes], file, ensure_ascii=False, indent=4)

    def load_quizzes(self):
        with open(self.file_path, 'r') as file:
            quizzes_data = json.load(file)
            return [Quiz(**q) for q in quizzes_data]
       
    def add_quiz(self):
        question = input("Введите вопрос: ")
        options = {}
        for letter in ['a', 'b', 'c', 'd']:
            options[letter] = input(f"Введите вариант ответа {letter}: ")
        true_answer = input("Введите правильный вариант (a/b/c/d): ")
        point = 10
        quiz = Quiz(question, point, true=true_answer, **options)
        self.quizzes.append(quiz)
        self.save_quizzes()

    def delete_quiz(self):
        question = input("Введите вопрос, который нужно удалить: ")
        self.quizzes = [quiz for quiz in self.quizzes if quiz.question != question]
        self.save_quizzes()

    def view_quizzes(self):
        for quiz in self.quizzes:
            print(f"Вопрос: {quiz.question}")
            for key, value in quiz.info.items():
                print(f"  {key}: {value}")
            print(f"  Правильный ответ: {quiz.is_true}")
            print(f"  Баллы: {quiz.point}")

    def take_quiz(self):
        user = input("Введите ваше имя: ")
        test = Test("Общий тест", self.quizzes, user)
        test.start()

    def main(self):
        while True:
            print("\nМеню:")
            print("1. Добавить тест")
            print("2. Удалить тест")
            print("3. Просмотреть тесты")
            print("4. Пройти тест")
            print("5. Выйти")
            choice = input("Введите ваш выбор: ")
            if choice == "1":
                self.add_quiz()
            elif choice == "2":
                self.delete_quiz()
            elif choice == "3":
                self.view_quizzes()
            elif choice == "4":
                self.take_quiz()
            elif choice == "5":
                print("Выход")
                break

QuizManager().main()


# 50/50