# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 23:22:15 2019

@author: shkim
"""

"""
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white', 'pupple']
"""

color1 = ['red', 'blue', 'green']
cities = ['서울', '부산', '인천', '대구', '대전', '광주', '울산', '수원']
cities[0:len(cities)]
cities[-1:]
cities[-5:-1]

#%%
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white', 'pupple']

print(len(color1), len(color2))


#%%
color3 = color1 + color2
print(color3)

#%%
#color1.append(color2)
color1
color1[0]='grey'
color1

#%%
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white', 'pupple']
color1.append(color2)
print(color1)
#color1 = ['red', 'blue', 'green']
#color1.extend(color2)
#print(color1)


#%%