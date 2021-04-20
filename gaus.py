import numpy as np
import math
# This class implements a gauss-crout method for solving linear equations
class Gaus:
    a = np.array(
        [
            [6,    -2,    2,    4], 
            [12,    -8,    6,    10],
            [3,    -13,    9,    3],
            [-6,    4,    1,    -18]
         ], float)
    b = np.array([ 12,34,27,-38 ], float)

    Acpy = np.copy(a)
    Bcpy = np.copy(b)
    n = len(b)
    result = np.zeros(n, float)

    remember = np.arange(0,n,1 )

    def __init__(self):
        print("Macierz a\n",self.a)
        print("Macierz b\n",self.b)
        



    def checkResult(self):
        print(np.linalg.solve( self.Acpy , self.Bcpy) )



    def forwardSub(self):
        # k - diagonalne elementy od zerowej do przedosttatniej kolumny
        # i 0- kolejne wiersze od pierwszego do ostatniego
        # j - przechodi przez elementy danego wiersza
        for k in range(self.n - 1):
            for i in range(k + 1, self.n):
                if self.a[k,k] == 0: continue
                mnoznik = self.a[i, k] / self.a[k, k ]
                
                for j in range(k, self.n):
                    self.a[i, j] -= self.a[k, j]  * mnoznik

                self.b[i] -= self.b[k] * mnoznik
       



    def backSub(self):
        n= self.n
        if self.a[n-1,n-1] == 0 : self.result[n-1] = 0
        else : self.result[n-1] = self.b[n-1] / self.a[n-1,n-1]

        for i in range(n-2,-1,-1): # going from last row up
            sumX= 0
            for j in range(i+1,n):
                sumX += self.a[i,j] * self.result[j]
            
            if self.a[i,i] == 0:
                self.result[i] = 0
            else:
                self.result[i] = (self.b[i] - sumX) / self.a[i,i]


    def showResult(self):
        print("Wynik :")  
        print(self.result)


# Place the bigest modulo at the first position of the array
    def croutMethod(self,row,dzielnik,diagonal):
        index=0
        modulo = 0
        if dzielnik==0:
            index = np.argmax(row,axis=0)
        else:
            for i in range( len(row) ):    
                 if math.fabs( math.fmod(row[i],dzielnik) ) > modulo: 
                     modulo,index = math.fabs( math.fmod(row[i],dzielnik) ),i
        
        self.remember[ [diagonal,index]] = self.remember[[index,diagonal]] # swap columns in the remeber



    def CroutforwardSub(self):
        # k - diagonalne elementy od zerowej do przedosttatniej kolumny
        # i 0- kolejne wiersze od pierwszego do ostatniego
        # j - przechodzi przez elementy danego wiersza
        for k in range(self.n - 1):
            
            for i in range(k + 1, self.n):
                self.croutMethod(self.a[i],self.a[k,k],i)                
                if self.a[k, self.remember[k] ] < math.fabs(0.001):
                    print("Can't solve")
                    return
                mnoznik = self.a[i, self.remember[k]] / self.a[k, self.remember[k] ]
                for j in range(k, self.n):
                    self.a[i, self.remember[j] ] -= self.a[k, self.remember[j] ]  * mnoznik

                self.b[i] -= self.b[k] * mnoznik

    
    
    def CroutBackSub(self):
        n= self.n
        if self.a[n-1,n-1] == 0 : self.result[n-1] = 0
        else : self.result[n-1] = self.b[n-1] / self.a[n-1,n-1]

        for i in range(n-2,-1,-1): # going from last row up
            sumX= 0
            for j in range(i+1,n):
                sumX += self.a[i,j] * self.result[j]
            
            if self.a[i,i] == 0:
                self.result[i] = 0
            else:
                self.result[i] = (self.b[i] - sumX) / self.a[i,i]
        print("Wynik :")  
        print(self.result)            


