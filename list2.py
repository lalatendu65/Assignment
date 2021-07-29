a=['Apple','Banana','Orange','grape']
b=input('enter your favourite fruit')
if b in a:
    print('it was in the list')
    a.remove(b)
    print('you removed your favourite fruit')
    for i in a:
        print(i)
else:
    print('it was not in the list ')
    a.append(b)
    print('you added your favourite fruit')
    for i in a:
        print(i)
        
    
