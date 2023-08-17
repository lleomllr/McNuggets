# McNuggets
McNuggets Challenge. 3 differents solutions 

we create a pack in which the numbers declared correspond to the boxes offered at mcdo (6, 9, 20).
We then check whether or not the number of nuggets is less than zero. 
If this is not the case and n nuggets is large enough, then n = 6xC1 + 9xC2 + 20xC3 (CX as a coefficient).

In a more efficient version, we look at the number of McNuggets left after taking a box of size 6, 9 or 20 and check whether it can be stored in a box.

Finally, the last version uses the previous one with the option of a box of 4 nuggets, which radically changes the results. 
