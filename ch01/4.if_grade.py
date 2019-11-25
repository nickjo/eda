# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:58:39 2019

@author: shkim
"""

score = int(input('input score>> '))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)

#%%

score = int(input('input score>> '))

if score >= 90:
    grade = 'A'
elif score >= 80 and score < 90:
    grade = 'B'
elif score >= 70 and score < 80:
    grade = 'C'
elif score >= 60 and score < 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)




