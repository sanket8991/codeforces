# -*- coding: utf-8 -*-

num=int(input())
 
a=input()
luck=list('47')
 
b=list(filter(lambda x:x in luck ,a))
 
h=int(num/2)
 
if a=='44' or a=='77':
    print('YES')
 
elif len(b)==len(a):
    
    f=sum(list(map(int,a[:h])))
    
    s=sum(list(map(int,a[h:])))
   
    if f==s:
        print('YES')
    else:
        print('NO')
 
else:
    print('NO') 