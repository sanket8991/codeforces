# -*- coding: utf-8 -*-

import math
 
cases=int(input())
 
row=0
clm=[0 for i in range(cases)]
 
pair=0
 
 
for i in range(cases):
    val=input()
    p=len(list(filter(lambda x:x=='C',val)))
    
    if p>1:
        nr=math.factorial(p)
        dr=math.factorial(p-2)*2
        row+=nr/dr
 
    for j in range(cases):
        if val[j]=='C':
            
            clm[j]+=1
            
 
for i in clm:
    if i>1:
        nr=math.factorial(i)
        dr=math.factorial(i-2)*2
        
        pair+=nr/dr
 
 
print(int(row+pair))
