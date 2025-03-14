# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 13:23:29 2025

@author: joana
"""

# x%k=0, gives us a remaider of 0, that yes says it is divisible by k
# but the assert just gives us an error if the condition is not met, not true or false?
#changed it to return jsut with the x%k == 0, to give us TRUE if condition is met, or FALSE if not met
def is_divisible_by_k(x, k):
    '''
    Checks whether x is divisible by k.
    '''
    return x%k == 0

'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000 (excluding doubles)
'''
# x was a tuple because of (), changed it to a list []
x = [] 
#in pyhton, if we had range (1000), the number 1000 wouldn't be considered, and added the the 1 otherwise it would start in 0
#they had "is_divisible_by_K(x, 2) but should be i instead of x and or instead of &. and should be divisable by 2 or 5 or 7
#cannot have doubles, so need to make sure the number is not repeated?
for i in range(1, 1001):
    if (is_divisible_by_k(i, 2) or is_divisible_by_k(i, 5) or is_divisible_by_k(i, 7)):
        if i not in x:
            x.append(i)
    
'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000 (excluding doubles)
'''
print(sum(x))



#alternatively, to not store doubles, we can consider a set instead of a list
x = set() 

for i in range(1, 1001):
    if (is_divisible_by_k(i, 2) or is_divisible_by_k(i, 5) or is_divisible_by_k(i, 7)):
        x.add(i)
'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower
or equal to 1000 (excluding doubles)
'''
print(sum(x))
