import numpy as np

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

    n = len(b)
    result = np.zeros(n, float)

    def __init__(self):
        pass

    

    def elimination(self):
        print(self.a)
        for k in range(self.n - 1):
            for i in range(k + 1, self.n):
                if self.a[i][k] == 0: continue
                dzielnik = self.a[k, k] / self.a[i, k]
                print("dzielnik:%f" %dzielnik)
                for j in range(k, self.n):
                    self.a[i, j] = self.a[k, j] - self.a[i, j] * dzielnik
                print(self.a)
                print()
                self.b[i] = self.b[k] - self.b[i] * dzielnik
        print("After elimination")
        print(self.b)



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
        print("Result :")  
        print(self.result)
