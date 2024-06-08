# 5
from json import load, dump
import os
import pathlib

current_path = pathlib.Path().resolve()
file = os.path.join(current_path, 'app.json')
        

class Tovar:
    def __init__(self) -> None:
        self.date = []

    def add_tovar(self, titel, prise):
        
    
        with open(file, "r+", encoding="utf8") as fl:
            arr: list = load(fl)
            if type(arr) != list:
                dump([], fl)
        id = 0
        if len(arr) >= 1:
            for i in arr:
                if i['titel'] == titel:
                    print('такой тавар есть')
                    return 'такой тавар есть'
            id = sorted(arr, key=lambda x: x["id"])[-1]['id'] +1
        else:
            id = 1
        print(id)
        arr.append({"id": id, "titel": titel, "prise": prise})
        self.date.append({"id": id, "titel": titel, "prise": prise})
        with open(file, "w", encoding="utf8") as fl:
            dump(arr, fl, ensure_ascii=False, indent=4)
        print("[INFO] Good add")

    def in_prise(self, manu):
        with open(file, "r", encoding="utf8") as fp:
            arr = load(fp)

        new_arr = []
        for i in arr:
            if i["prise"] <= manu:
                new_arr.append(i)
        return new_arr
    
    def del_item(self,id):
        with open(file, "r", encoding="utf8") as fl:
            arr: list = load(fl)
        new_arr = []
        for i in arr:
            if i['id'] != id:
                new_arr.append(i)
        with open('app.json','w',encoding='utf8') as fp:
            dump(new_arr,fp,ensure_ascii=False,indent=4)

    def izmenit_prise(self,id,prise):
        with open(file, "r", encoding="utf8") as fl:
            arr: list = load(fl)
        for i in arr:
            if i['id'] == id:
                i['prise'] = prise
        with open('app.json','w',encoding='utf8') as fp:
            dump(arr,fp,ensure_ascii=False,indent=4)
        return 'not id'
    
    @property
    def info(self):
        with open('app.json','r' ,encoding='utf8') as fl:
            return load(fl)
        
    def admin(self):
        viber = int(input('1) удолить\n2) добавить\n3) изменить цену\n4) выхед\nВыбер: '))
        if viber == 1:
            for i in self.info:
                print(f'{i['id']}) titel => {i['titel']}\n   prise => {i['prise']}\n')
            viber = int(input('Выбкрите по id (0 - exet): '))
            if viber == 0:
                self.admin(
                )
            self.del_item(viber)
            print('товар удолён')
            return self.admin()
        elif viber == 2:
            titel = input('titel = ')
            prise = int(input('prise = '))
            if not titel and prise:
                print('error titel prise')
                return self.admin()
            self.add_tovar(titel,prise)
            return self.admin()
        elif viber == 3:
            for i in self.info:
                print(f'{i['id']}) titel => {i['titel']}\n   prise => {i['prise']}\n')
            viber = int(input('Выбкрите по id (0 - exet): '))
            if viber == 0:
                self.admin()
            new_prise =int( input('new prise = '))
            self.izmenit_prise(viber,new_prise)
            return self.admin()
        elif viber == 4:
            return self.start()
        else:
            print('error')
            return self.admin()
        
    
        
    def user(self,manu):
        viber = int(input('1) karzina\n2) bay\n3) exet\nВыберте: '))
        if viber == 2:
            text = self.in_prise(int(manu))
            for i in text:
                print(f'{i['id']}) titel => {i['titel']}\n   prise => {i['prise']}\n')
            viber = int(input('Выберте (0 = выхед): '))
            if viber == 0:
                return self.user()
            caunt = int(input('caunt: '))
            for i in self.info:
                if i['id'] == viber:
                    with open('user.json' , 'r' , encoding='utf8') as fl:
                        arr:list = load(fl)
                    for j in arr:
                        if j['titel'] == i['titel']:
                            j['caunt'] += caunt
                            j['sum'] += caunt * i['prise'] 
                        manu -= caunt * i['prise']
                        print(f'manu => {manu}')
                        with open('user.json' , 'w',encoding='utf8') as fl:
                            dump(arr,fl,indent=4,ensure_ascii=False)
                        return self.user(manu)
                    
                    arr.append({
                        'titel':i['titel'],
                        'prise':i['prise'],
                        'caunt': caunt,
                        'sum' : caunt * i['prise'] ,
                    })
                    manu -= caunt * i['prise']
                    print(f'manu => {manu}')
                    with open('user.json' , 'w',encoding='utf8') as fl:
                        dump(arr,fl,indent=4,ensure_ascii=False)
                    return self.user(manu)
        elif viber == 1:
            with open('user.json' , 'r',encoding='utf8') as fp:
                arr = load(fp)
            if len(arr) == 0:
                return self.user(manu)
            for i in arr:
                print(f'titel : {i['titel']}\nprise : {i['prise']}\n caunt : {i['caunt']}\n sum : {i['sum']}\n')
                print(f'manu = {manu}')
                return self.user(manu)
        elif viber == 3:
            return self.start()
        else:
            return self.user(manu)
            
        


    def start(self):
        manu = input('сколько у вас денек: ')
        if manu.isnumeric():
            manu = int(manu)
            self.user(manu)
            
        elif manu == 'admin':
            self.admin() 
        else:
            raise TypeError

a = Tovar()
a.start()
# a.del_item(1)
