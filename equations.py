
def power(x:float,n:float):
    machpela = 1.0
    for i in range(int(n)):
        machpela = machpela * x
    return machpela  
def azeret(n):
    result3=1.0
    for i in range(1,int(n)+1):
        result3=result3 * i    
    return result3   
def exponent(marih:float) -> float:
    result2=0.0
    for i in range(0,50):
        result2= result2 + (power(marih,i))/(azeret(i)) 
    return result2        
def ln(x:float) -> float:
    if x<=0:
        return 0
    else:
        yn=0
        result= x-1.0
        while((yn-result)>0.001 or (result-yn)>0.001):
            yn=result
            result = result + 2*((x-exponent(result))/(x+exponent(result)))
        return result     
def XtimesY(x:float,y:float) -> float:
    try:
        if(x>0):
            a=exponent(ln(x)*y)
            result=float('%0.6f' % a)
            return result
        elif (x<0 and y>=0 and y%1==0):
            a=power(x,y)
            result=float('%0.6f' % a)
            return result
        elif (x<0 and y<0 and y%1==0):
            a=(power(1/x,-y))
            result=float('%0.6f' % a)
            return result
        elif (x==0):
            return 0
        else:
            return 0
    except:
        return 0
def sqrt(x:float,y:float) -> float:
    try:
        if(y>0 and x!=0):
            x=1/x
            a=(XtimesY(y,x))
            result=float('%0.6f' % a)
            return result
        elif ((y<0 and x%2==0) or (x==0) or (y==0)):
            return 0
        elif (y<0 and (1/x)%int(1/x)==0 and (1/x)%2!=0):
            x=1/x
            y=-y
            a=(XtimesY(y,x))
            result=float('%0.6f' % a)
            return result
        elif (y<0 and (1/x)%int(1/x)==0 and (1/x)%2==0):
            x=1/x
            y=-y
            a=(XtimesY(y,x))
            result=float('%0.6f' % a)
            return result
        else:
            return 0
    except:
        return 0
def calculate(x:float) -> float:
    try:
        calc=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
        result=float('%0.6f' % calc)
        return result
    except:
        return 0
 
# try:    
#     num1=input ('enter a num: ')
#     x=float(num1)
#     print(calculate(x))
# except:
#     print(0)
 
 
 
 