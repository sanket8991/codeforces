# -*- coding: utf-8 -*-

cases=int(input())
 
result=[]
 
for i in range(cases):
    c,r,x,y=map(int,input().split())
    result.append(max(x*r,(c-x-1)*r,y*c,(r-y-1)*c))
 
for i in result:
    print(i)
 
