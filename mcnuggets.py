# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:37:54 2023

@author: meill
"""

packs = [6, 9, 20]

# - k is the number of nuggets

def mcnuggets(k):
    a = packs[0]
    b = packs[1]
    c = packs[2]
    
    if k < 0:
        return False
    elif k == 0:
        return True
    #if k is not in packs, calculate what combinaison we can do 
    else:
        for x in range(0, k):
            for y in range(0, k):
                for z in range(0, k):
                    if a*x + b*y + c*z == k:
                        return True
    return False
    
print(mcnuggets(30))
        
#%% Other version which is more efficient
      
# - box is used to stock results

def mcnuggets_v2(nugg, box):
    if nugg < 0:
        return False
    elif nugg == 0:
        print("Yes Sir !")
        return True
    for k in packs:
        box[nugg - k] = mcnuggets_v2(nugg - k, box)
        if box[nugg - k]:
            return True
    return False


test = [1, 2, 3, 6, 8, 9, 10, 12, 15, 16, 18, 30, 43, 51, 100, 202]
for n in test:
    print(f"Nuggets : {n}", mcnuggets_v2(n, dict()))
    
#%% Version with a pack of 4 

packs_hm = [4, 6, 9, 20]

def mcnuggets_hm(nugg, box):
    if nugg < 0:
        return False
    elif nugg == 0:
        print("Yes Sir !")
        return True
    for k in packs_hm:
        box[nugg - k] = mcnuggets_hm(nugg - k, box)
        if box[nugg - k]:
            return True
    return False


case = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 15, 16, 18, 30, 43, 51, 115, 237]
for ng in case:
    print(f"Nuggets : {ng}", mcnuggets_hm(ng, dict()))
    