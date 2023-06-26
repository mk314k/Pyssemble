A=[0,0,0,0,0,0,0,0,0,0]
Mem=[0,0,0,0,0,0,0,0,0,0,0]
sp=208
def loadword(n):
    return Mem[int((n-200)/4)]

def storeword(n, val):
    n=int((n-200)/4)
    Mem[n]=val
    pass

def mul():
    A[0] = A[0] * A[1]
    for i in range(1,len(A)):
        A[i]=-1

def factorial():
    if (A[0]==0):
        A[0] =1
        return
    A[1] = A[0]-1
    while (A[1]!=0):
        #A[1] = A[2] -1
        storeword(sp,A[1])
        #storeword(sp+4,A[1])
        mul()
        A[1]=loadword(sp)
        A[1] = A[1]-1
    pass

for i in range(5):
    A[0]=i
    factorial()
    print(A[0])