# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:09:26 2019

@author: shkim
"""

a = [1, 2, 3, 4, 5]
a.append(6)
a

#%%
a.pop()



#%%

word = input("Input a word: ")
print(word)
world_list = list(word)
print(len(world_list), world_list)

result = []

for _ in range(len(world_list)):
    result.append(world_list.pop())

print('-' * 50)
print(result)
print(word[::-1])



