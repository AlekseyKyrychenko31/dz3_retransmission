#n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке?
# Программа получает на вход числа `n` и `k` и должна вывести искомое количество яблок (два числа)

k = int(input('яблоки в корзине: '))
n = int(input('кол. школьников: '))
x = k//n
y = x * n
o = k - y
print('достанется каждому школьнику :', x)
print('яблок останется в корзинке:', o)

# 2. В школе решили набрать три новых математических класса. Так как занятия по математике у них проходят
# в одно и то же время,было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.

a = int(input('класс1:'))
b = int(input('класс2:'))
c = int(input('класс3:'))
x = a + b + c
p = x//2 + 1
print('нужно купить парт: ', p)
