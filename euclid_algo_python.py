
"""
Take two inputs, check if first one "a" is a power of "b"
return True if Yes, False if Nay
"""
def powerofb(a,b):

    try:
        x = int(a)
        y = int(b)
    except (ValueError, TypeError):
        try:
            x = int(float(a))
            y = int(float(b))
        except (ValueError, TypeError):
            print("Please use numeric values.")
            return "Error"
    
    #making aboslute value
    a = abs(x)
    b = abs(y)

    if a == b:
        return True
  
    if a == 0 and b != 0:
        return False
  
    if a==1:
        return True 

    #test divisibility condition, initiate recursion       
    if a % b == 0 and powerofb(a/b,b):
        return True
     
    
    #if both conditionals fail, it 
    return False

#in this question, I assumed that 0^0 = 1, though there is no real agreed-upon value for it