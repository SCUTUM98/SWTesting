class Calculator:
    def add(self,a,b):        
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Only numeric is allowed")
        
        return a+b;

    def sub(self,a,b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Only numeric is allowed")
        
        return a-b

    def div(self,a,b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Only numeric is allowed")
        if b == 0:
            raise ZeroDivisionError("Zero Division Error")
        
        return a/b
    
    def multi(self,a,b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Only numeric is allowed")
        
        return a*b