'''
Ввести список А из 10 элементов, найти произведение положительных элементов
и вывести его на экран
'''
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
        a = list(map(int, input("Введите 10 цифр: ").split()))
        o = 1
        print([i for i in a if i>0 o*=i])
        print (o)
        
