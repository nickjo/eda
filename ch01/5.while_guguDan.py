# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:48:40 2019

@author: shkim
"""


while(1):
    dan = int(input('input dan >> '))
    if dan > 9:
        break
     
    for i in range(9):
        print(dan * (i+1))
    
        
    
print("구구단 게임을 종료합니다.")

