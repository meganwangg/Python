'''
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. 
Return -1 if it can't be done.
'''

def make_chocolate(small, big, goal):
  bigBars = goal/5;
  smallBars = goal%5;  
  
  #Not enough bars
  if (goal - bigBars*5 > small):
    return -1
  
  #if not enough small bars after removing big bars first
  count = goal - big*5
  if (small< count):
    return -1
  
  #if # of big bars is not too many
  if (bigBars <= big):
    #if # small bars is > # of remaining bars, return how many needed
    smallsNeeded = goal - bigBars*5
    if ( small>smallBars):
      return smallsNeeded
  
  
  #here we know that the number of needed small bars (count) is less than small
  #and that number needed is not 0, return the modulus of what's leftover from
  #the goal
  if (small >=  count and count > 0):
    return count
  else: 
    return smallBars
