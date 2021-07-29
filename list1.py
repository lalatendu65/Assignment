'''
from random import *
l1=[]
print(randint(0,30),end=' ')
for i in range(20):
    a=randint(0,30)
    print(a)
    l1.append(a)
print(l1)
print(len(l1))
'''
'''
a,b,c,d=10,30,12.456475,45
print('P the sum of values of %i, %d,and %8.2f is:%s'%(a,b,c,a+b+c))
print('Bpsum of values {},{} and {} is{}'.format(a,b,c,a+b+c))
print('vpsum of values {a1},{b1},and {c1},is{ee}'.format(ee=a+b+c,b1=a,a1=a,c1=c))
print(f'the sum of values {a},{b} and {c} is :{a+b+c}')
print('%3.2f'%a)      
'''
from random import *
l1=[]
print(randint(0,30),end=' ')
for i in range(20):
    a=randint(0,30)
    print(a)
    l1.append(a)
print(l1)
l2=set(l1)
print(l2)
c=len(l1)-len(l2)
c1=len(l1)-c
print('the number of duplicate;',c)
print('the nuuber of unique;',c1)


    




    


    
