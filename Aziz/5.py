import json

class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        
    def __str__(self):
        return f"{self.name} - {self.price} сом ({self.count} шт )"

class Avtomat:
    def __init__(self, products):
        self.products = products
        self.balance = 0
        self.purchased_products = []
        
    def add_balance(self, count):
        self.balance += count
        print(f'Ваш баланс: {self.balance} сом ')
        
        
        
        
        
    def show_products(self):
        print('Доступные товары:')
        for product in self.products:
            print(product)
    
    
    def show_purchased_products(self):
        print('Купленные товары:')
        for product in self.purchased_products:
            print(product)
            
            
            
      
      
            
            
            
            
    def buy_product(self, choice):
        if 0 < choice <= len(self.products):
            product = self.products[choice - 1]
            if product.count > 0 and self.balance >= product.price:
                self.balance -= product.price
                product.count -= 1
                self.purchased_products.append(product)
                print(f'Вы купили {product.name}')
            elif product.count == 0:
                print(f'{product.name} закончился')
            else:
                print('Недостаточно средств')
        else:
            print('Такого товара нет')









class Data:
    def __init__(self, filename):
        self.filename = filename
        
    def load_products(self):
        with open(self.filename, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            products = []
            for product in data:
                products.append(Product(product['name'], product['price'], product['count']))
            return products
        
    def save_product(self, product):
        with open(self.filename, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            data.append(product.__dict__)
            f.seek(0)
            json.dump(data, f, indent=4)









def main():
    data = Data('products.json')
    products = data.load_products()
    avtomat = Avtomat(products)
    avtomat.show_products()
    avtomat.add_balance(1000)
    
    while True:
        print("\n1. Внести деньги")
        print("2. Показать товары")
        print("3. Показать купленные товары")
        print("4. Купить товар")
        choice = input("Выберите действие: ")

        if choice == '1':
            amount = int(input("Введите количество денег: "))
            avtomat.add_balance(amount)
        elif choice == '2':
            avtomat.show_products()
        elif choice == '3':
            avtomat.show_purchased_products()
        elif choice == '4':
            avtomat.show_products() 
            product_index = int(input("Введите номер товара: "))
            avtomat.buy_product(product_index)
        else:
            print("Неправильный выбор.")
            
            
main()



# ?