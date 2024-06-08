# //////////////////////6 Задание Чуть Чуть не успель ...///////////////////////
import json

class Ali:
    def init(self):
        self.balance = 0
        self.products = self.abu_products()

    def abu_products(self):
        with open('products.json') as f:
            return json.load(f)

    def display_products(self):
        print("Выберите продукт:")
        for product_id, product in self.products.items():
            print(f"{product_id}: {product['name']} - {product['price']} руб")

    def add_balance(self, amount):
        self.balance += amount
        print(f"Баланс: {self.balance} руб")

    def buy_product(self, product_id):
        if product_id in self.products:
            product = self.products[product_id]
            if product['price'] <= self.balance:
                self.balance -= product['price']
                print(f"Вы купили {product['name']} за {product['price']} руб")
                print(f"Остаток на балансе: {self.balance} руб")
            else:
                print("Недостаточно средств на балансе")
        else:
            print("Такого продукта нет")

    def display_balance(self):
        print(f"Баланс: {self.balance} руб")

def main():
    vending_machine = Ali()

    while True:
        print("\n1. Добавить деньги")
        print("2. Показать баланс")
        print("3. Показать продукты")
        print("4. Купить продукт")
        print("0. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            amount = float(input("Введите сумму для добавления: "))
            vending_machine.add_balance(amount)
        elif choice == '2':
            vending_machine.display_balance()
        elif choice == '3':
            vending_machine.display_products()
        elif choice == '4':
            product_id = input("Введите ID продукта: ")
            vending_machine.buy_product(product_id)
        elif choice == '0':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
   main()
json
{
  "1": {"name": "Кола", "price": 50},
  "2": {"name": "Чипсы", "price": 30},
  "3": {"name": "Шоколадка", "price": 40},
  "4": {"name": "Кофе", "price": 60}
}


# 50/50