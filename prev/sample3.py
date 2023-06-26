#Quicksort
"""
#include "src/defines.h"
.section ".text.init"
    .globl sort
    .globl kth_smallest
    .globl violation

/*

QUICKSORT & PARTITION

C implementation (for reference)

int partition(int* p, int start, int end) {
    int x = p[end]; // select pivot
    int j, tmp, i = start - 1;
    for (j = start; j < end; j++) {
        if (p[j] <= x) {
            i++;
            tmp = p[i];
            p[i] = p[j];
            p[j] = tmp;
        }
    }
    tmp = p[i + 1];
    p[i + 1] = p[end];
    p[end] = tmp;
    return i + 1;
}

void quicksort(int* p, int start, int end) {
    if (start < end) {
        int q = partition(p, start, end);
        quicksort(p, start, q - 1);
        quicksort(p, q + 1, end);
    }
}

Python implementation (for reference)

def partition(p, start, end):
    x = p[end]
    i = (start - 1)
    for j in range(start, end):
        if p[j] <= x:
            i = i + 1
            tmp = p[i]
            p[i] = p[j]
            p[j] = tmp
    tmp = p[i + 1]
    p[i + 1] = p[end]
    p[end] = tmp
    return i + 1

def quicksort(p, start, end):
    if start < end:
        q = partition(p, start, end)
        quicksort(p, start, q - 1)
        quicksort(p, q + 1, end)

*/

//  QUICKSORT (should call "partition")
//
//  Inputs:
//  a0 = p (address of array)
//  a1 = start
//  a2 = end

sort:
  ret


// PARTITION
//
// Inputs:           
// a0 = starting address of the array
// a1 = index of the starting element
// a2 = index of the ending element

partition:
  ret



/*

Kth SMALLEST

Python implementation (for reference)

# array is the sorted array from sort
# gets index k from the user and prints array[k]
# returns nothing

def kth_smallest(array):
    x = input("enter the index to print\n")
    print array[x]
    return

*/

//  Input:  a0 = address of sorted array
kth_smallest:
  ret
"""

mem=[0]*70
a=[0]*8
t=[0]*8
s=[0]*8
def loadword(n):
    if (n==40004000):
        return int(input())
    return mem[int(n/4)]

def storeword(n, val):
    if (n==40000004):
        print(val)
        return
    n=int(n/4)
    mem[n]=val
    pass
def debug(k='0'):
    print(mem,a,t[0],k)
    return

"""
a0 = p (address of array)
//  a1 = start
//  a2 = end
"""

def quicksort(sp=260,ra=500):
    x1=sp
    x2=ra
    #debug("brakpoint 94")
    sp=sp-20
    if (a[1]<a[2]):
        storeword(sp,ra)
        storeword(sp+4,a[0])
        storeword(sp+8,a[1])
        storeword(sp+12,a[2])
        ra =200
        partition(sp, ra)
        a[2]=a[0]-1
        a[0]=loadword(sp+4)
        a[1]=loadword(sp+8)
        storeword(sp+16,a[2])
        ra=300
        quicksort(sp,ra)
        a[0]=loadword(sp+4)
        a[1]=loadword(sp+16)
        a[1]=a[1]+2
        a[2]=loadword(sp+12)
        ra=400
        quicksort(sp,ra)
        ra=loadword(sp)
    sp=sp+20
    assert(sp==x1 and ra==x2)
    return


def partition(sp=260,ra=200):
    x1=sp
    x2=ra
    a[3]=a[2]*4
    a[3]=a[0]+a[3]
    a[5]=loadword(a[3])   #x=p[end]
    a[4]=a[1]*4
    a[4]=a[0]+a[4]
    a[6]=a[4]
    while (a[6]<a[3]):
        a[7]=loadword(a[6])
        if (a[7]<=a[5]):
            t[0]=loadword(a[4])
            storeword(a[4],a[7])
            storeword(a[6],t[0])
            a[4]=a[4]+4
        a[6]=a[6]+4
    t[0]=loadword(a[4])
    storeword(a[4],a[5])
    storeword(a[3],t[0])
    a[0]=a[4]-a[0]
    a[0]=int(a[0]/4)
    assert(sp==x1 and ra==x2)
    return

def kth(sp=260,ra=200):
    x1=sp
    x2=ra
    a[1]=40004000
    a[2]=loadword(a[1])
    a[2]=a[2]*4
    a[2]=a[2]+a[0]
    a[3]=loadword(a[2])
    a[1]=40000004
    storeword(a[1],a[3])
    assert(sp==x1 and ra==x2)
    return




q=[12,16,12,8,0,0,4]
for i in range(2,9):
    mem[i]=q[i-2]


a[0]=8
a[1]=0
a[2]=6
print(mem)
quicksort()
print(mem)
kth()
kth()
kth()