import csv
import os
import json

def find_personal(key):
    count = 0
    t=''
    with open('members.cvs', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            for k in i.split(','):
                if k == key:
                    t=t+i+('\n')
                    count += 1
        if count==0:
            return 'Not found'
        return t

def personal_position(key):
    count = 0
    t=''
    with open('members.cvs', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            for k in i.split(','):
                if k == key:
                    t=t+i+('\n')
                    count += 1
        if count==0:
            return 'Not found'
        return t

def personal_salary(key):
    count = 0
    t=''
    with open('members.cvs', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            for k in i.split(','):
                if k == key:
                    t=t+i+('\n')
                    count += 1
        if count==0:
            return 'Not found'
        return t

def add_personal():
    name =str(input('Укажите имя  '))
    surname = str(input('Укажите фамилию  '))
    position =str(input('Укажите должность  '))
    salary =str(input('Укажите заработную плату  '))
    full=''
    with open('members.cvs','a',) as file:
        full=('\n')+name+','+surname+','+position+','+salary
        file.write(full)
        return 'Сотрудник добавлен'

def personal_delete(key,key2):
    new=[]
    with open('members.cvs', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if key  not in i:
                if key2 not in i:
                    new.append(i)
        with open('members.cvs', 'w') as file:
            for line in new:
                file.write(f'\n{line}')
            return 'Сотрудник удален'


def personal_replace(key,key2):
    with open('members.cvs', 'r') as file:
        data = file.read().split('\n')
        for i in data:
            if key  in i:
                if key2 in i:
                    new=i
                    name =str(input('Укажите имя  '))
                    surname = str(input('Укажите фамилию  '))
                    position =str(input('Укажите должность  '))
                    salary =str(input('Укажите заработную плату  '))
                    full=name+','+surname+','+position+','+salary
                    l = list(map(lambda x: x.replace(new,full), data))
    with open('members.cvs', 'w') as file:
        for line in l:
            file.write(f'\n{line}')
        return 'Сотрудник перезаписан'

def convjson():                     
    with open('members.cvs','r',encoding='utf-8') as filecvs:     
        basa = csv.reader(filecvs) 
        basa = list(basa) 
    data_json = json.dumps(basa)    
    with open('basa_list.json', 'w', encoding = 'utf-8') as filejson:
       filejson.write(data_json)
       return ' Данные экспортированы в формате json '
