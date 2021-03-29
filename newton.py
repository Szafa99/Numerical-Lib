from sympy import Symbol,diff
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
import math

class Newton:
    gueasVal = None
    derivative=None
    equation=None
    equation2=None
    precision=None
    maxIter=None
    x = {'x': Symbol('x', real=True)}


    def __init__(self,equation,guesVal=5,precision=0.001,maxIter=100):
        self.gueasVal = guesVal
        self.equation = equation
        self.equation2 = parse_expr(equation, self.x)
        self.precision=precision
        self.maxIter=maxIter
        self.derivative = diff(  self.equation2,self.x['x'])
    
    def fun(self,x):
        return math.sin(x)

    def der(self,x):
        return math.cos(x)

    def newtonBasic(self,x=gueasVal):
        for it in range(self.maxIter):
            xnew = x -  ( eval(self.equation,{'x':x} )/ eval( str(self.derivative),{'x':x})  )
            #xnew = x -  ( self.fun(x) )/ ( self.der(x) )
            if abs( xnew- x) <= self.precision: break
            x = xnew
        return x

    


    def plotNewton(self,xlist):
        ylist = []
        for x in xlist:
            ylist.append( self.newtonBasic(x) ) 
        plt.plot(xlist,ylist,'o',label = self.equation)
        plt.legend(loc='best')
        plt.show()
