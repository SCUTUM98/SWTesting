def add(a,b):        
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numeric is allowed")
    
    return a+b;

def sub(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numeric is allowed")
    
    return a-b

def div(a,b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Only numeric is allowed")
    if b == 0:
        raise ZeroDivisionError("Zero Division Error")
    
    return a/b