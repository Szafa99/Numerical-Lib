import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as m


class Interpol:
    x = None
    y = None

    xplt = None
    yplt = None
    polDegree = None
    fileName= None
    points=None
    refx=None
    refy=None
    funName=None

    def __init__(self,points=0):
        self.points = points


    def LoadData(self, fileName):
        self.fileName=fileName
        data = pd.read_excel(fileName, header=None)
        self.x = data[0].to_numpy(float)
        self.y = data[1].to_numpy(float)
        self.polDegree = len(self.x)-1



    def Lagrange(self):
        
        self.xplt = np.linspace(self.x[0], self.x[-1],self.points)  # Rozmieści points punktów na podanym przedzilay osi X
        self.yplt = np.array([], float)
        for xp in self.xplt:
            yp = 0
            for xi, yi in zip(self.x, self.y):
                yp += yi * np.prod((xp-self.x[self.x != xi]) / (xi-self.x[self.x != xi]))
            self.yplt = np.append(self.yplt, yp)




    def diffElement(self,x, y):
        # liczenie roznicy w tabelach
        n = len(y)
        coef = np.zeros([n, n])
        # the first column is y
        coef[:,0] = y

        for j in range(1,n):
            for i in range(n-j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])

        return coef

    def newtonInter(self,coef, x_data, x):
        n = len(x_data) - 1 
        p = coef[n]
        for k in range(1,n+1):
            p = coef[n-k] + (x -x_data[n-k])*p
        return p

    def Newton(self):
        a_s = self.diffElement(self.x, self.y)[0, :]

        self.xplt = self.xplt = np.linspace(self.x[0], self.x[-1],self.points)
        self.yplt = self.newtonInter(a_s, self.x, self.xplt)
    # def Newton(self):
    #     self.xplt = np.linspace(self.x[0], self.x[-1],self.points)  # Rozmieści points punktów na podanym przedzilay osi X
    #     self.yplt = np.array([], float)
    #     for xp in self.xplt:
    #         yp = 0
    #         for xi, yi in zip(self.x, self.y):
    #             yp += yi + np.prod( ( yi - self.y[self.y != yi] ) / (xi-self.x[self.x != xi]) ) * (xp-xi)
    #         self.yplt = np.append(self.yplt, yp)


    def refSin(self):
        self.refx = np.arange(0,self.x[-1],0.1)
        self.refy = np.sin(self.refx)
        self.funName="SIN"
       
    def refLin(self):
        self.refx = np.arange(0,self.x[-1],0.1)
        self.refy = 22*self.refx+4.4
        self.funName="liniowa"


    def refQuad(self):
        self.refx = np.arange(0,3,0.1)
        self.refy = 2*self.refx**2+3
        self.funName="kwadratowa"


    def showDiagram(self):


        plt.plot(self.xplt,self.yplt,'r-o',label='Fukcja zinterpolowana')
        plt.plot(self.refx,self.refy,'b--',label=self.funName)
        plt.title('Stopien wielomianu: %d' % (self.points))
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
        #plt.savefig("diagram.jpg")

    def countSingleVal(self,xp):
        yp=0
        for i in range(len(self.x)):
            p=1
            for j in range(len(self.y)):
                if j!=i:
                    p *= (xp-self.x[j]) / ( self.x[i]-self.x[j] )
            yp+=self.y[i]*p
        print('Dla x=%.2f zinterpolowano y=%.2f' % (xp,yp) )


    def algoLoop(self):
        print("Podaj stopień wielomianu")
        i = int(input())
        self.points=i



        chosen =False
        while(chosen==False):
            print("Wybierz funkcję\n\t1.Sinus\n\t2.Liniowa\n\t3.Kwaddratowa")
            choice = input()
            chosen=True
            if(choice == '1' ):
                self.LoadData('sin.xlsx')
                self.refSin()
            elif(choice== '2'):
                self.LoadData('linear.xlsx')
                self.refLin()
            elif(choice== '3'):
                self.LoadData('square.xlsx')
                self.refQuad()
            else:
                chosen=False

        self.Newton()
        self.showDiagram()

