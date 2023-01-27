
import view 
import modul 

def but():
    i = view.show_menu()
    if i == 1:
        key = input('Введите фамилию  сотрудника: ')
        print(modul.find_personal(key))
        i = view.show_menu()
    elif i == 2:
        key = input('Введите должность: ')
        print(modul.personal_position(key))
        i = view.show_menu()
    elif i == 3:
         key = input('Введите зарплату: ')
         modul.personal_salary(key)
         i = view.show_menu()
    elif i == 4:
        print(modul.add_personal())
        i = view.show_menu()
    elif i == 5:
        key = input('Введите имя: ')
        key2 = input('Введите  фамилию: ')
        print(modul.personal_delete(key,key2))
        i = view.show_menu()
    elif i == 6:
        key = input('Введите имя: ')
        key2 = input('Введите  фамилию: ')
        print(modul.personal_replace(key,key2))
        i = view.show_menu()
    elif i == 7:
        print(modul.convjson())
        i = view.show_menu()
    elif i == 8:
        print('Уверены что хотите завершить работу?')
        j=str(input())
        if j =='Да':
            print('Всего доброго!')
        if j=='Нет':
            i = view.show_menu()
