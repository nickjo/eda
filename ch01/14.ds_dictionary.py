# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 15:26:38 2019

@author: shkim
"""

# empty dictionary
d1 = {}
type(d1)

#%%
d2 = dict()
type(d2)

#%%
type(d1), d1, type(d2), d2

#%%
info = {1:'kim', 2:'park', 3:'lee'}
info

#%%
info[1] 

#%%
info[5] = 'choi'
info

#%%
info[4] = 'jo'
info

#%%
info.keys()

#%%
info.values()

#%%
info.items()

#%%
for k, v in info.items():
    print('id: {}, name: {}'.format(k,v))
    
#%%
3 in info.keys()

#%%
9 in info.keys()    




