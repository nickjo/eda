# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:37:58 2019

@author: shkim
"""

"""
# Tuple
"""
#%%

t = (1,2,3,4,5)
type(t)



#%%
t[1:3]
t[1] = 22

#%%
t[1:6:2]

#%%
s = {1,2,3,4}
type(s)

s.update([1,4,5,6,7,8,9])
print(s)
type(s)
s.discard(5)
print(s)

#%%
# 합집합
set_a = {1,2,3}
set_b = {2,3,4}

set_a.union(set_b)

#%%
# 교집합
set_a = {1,2,3}
set_b = {2,3,4}

set_a.intersection(set_b)

#%%
# 차집합
set_a = {1,2,3}
set_b = {2,3,4}

print(set_a.difference(set_b))
print(set_a)










