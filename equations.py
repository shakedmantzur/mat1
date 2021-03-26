# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 15:51:39 2021

@author: Shaked
"""

def power(x,b):
    num=1.0
    if x<=0.0:
        return(0.0)
    if b>=0.0:
        i=b
        while i>0:
            num=num*x
            i=i-1
        return float(num)
    elif b<=0.0:
        i=b*(-1)
        while i>0:
            num=num*x
            i=i-1
        return float(1/num)

def factorial(x):
    num=x
    if x>1:
        while(x>1):
            num=num*(x-1.0)
            x=x-1.0
        return float(num)
    elif x>=0:
        return(1.0)
    else:
        return(0.0)
        
    
def exponent(x:float)-> float:
    n=0.0
    e=1.0
    while n<90:
        e=e+(power(x, n))/(factorial(n))
        n=n+1.0
    return(e)    


def Ln(x:float)->float:
    try:
        if x<=0.0:
            return(0.0)
        yn=x-1.0
        while True:
            exp1= exponent(yn)
            yn1=yn+2*((x-exp1)/(x+exp1))
            if(yn-yn1)<=0.001 and(yn1-yn)<=0.001:
                return(yn1)
            yn=yn1
    except:
        return(0.0)
        
        
def XtimesY(x:float, y:float) -> float:
    try:
        if x>0:
            ans=exponent(Ln(x)*y)
            return float('%0.4f' %ans)
    except:
        return(0.0)

def sqrt(x:float, y:float)-> float:
    if x!=0 and y>0:
        x=1/x
        num= XtimesY(y,x)
        return float('%0.4f' %num)
    else:
        return(0.0)
    
def calculate(x:float)->float:
    try:
        ans=exponent(x)*XtimesY(7,x)*XtimesY(x,-1)*sqrt(x,x)
        return float('%0.4f' %ans)
    except:
        return(0.0)    
    