# function checkOverlap
# returns true if two lines overlap
# returns false if not
def checkOverlap(x1, x2, x3, x4):
    #rearrange inputs such that x1 < x2 and x3 < x4;
    if x1 > x2:
        x1, x2 = x2, x1
    if x3 > x4:
        x3, x4 = x4, x3
    
    #check if two lines are overlapped    
    if(min(x2, x4) - max(x1, x3) + 1):
        return True
    else:
        return False

print(checkOverlap(5, 1, 6, 8))