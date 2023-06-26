A=[5,4,3,2,1]
def loadword(n):
    return A[int((n-200)/4)]

def storeword(n, val):
    n=int((n-200)/4)
    A[n]=val
    pass

def bubblesort(a0, a1):
    a3=a0
    #a4=a1
    a1=a1-1
    a6=a1
    while (a6!=0):
        while (a1!=0):
            a2 =loadword(a0)
            a5 = loadword(a0+4)
            print(a1,a6)
            if a2 > a5:
                storeword(a0, a5)
                storeword(a0+4,a2)
            a0=a0+4
            a1=a1-1
        a6 =a6-1
        a1=a6
        a0=a3
    
        


    pass


# print(A)
# print(bubblesort(200,5))
# print(A)
w=29663102
p= 29567148
print(p/w)