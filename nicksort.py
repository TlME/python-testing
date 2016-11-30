# A rudimentary quicksort algorithm
# O(nlogn) runtime
#Nick Henegar

list1 = [67,45,2,13,1,998]
list2 = [89,23,33,45,10,12,45,45,45]


def mainfunction():
    nicksort(list1)
    nicksort(list2)
    print('[%s]' % ', '.join(map(str, list1))) #the hard part of this was figuring out how to format these things
    print('[%s]' % ', '.join(map(str, list2)))
#determines if the current pivot is a good partition point, then recursively calls itself on the half of the list
#before the pivot and the half immediately following the pivot, until the list has been fully sorted.
def nicksort(listX, small=0, big=None): 
    if (big is None):
        big = len(listX)-1
    if (small >= big):
        return
    
    pivot = partition(listX, small, big)
    nicksort(listX, small, pivot - 1)
    nicksort(listX, pivot + 1, big)
#Figures out whether or not the pivot is larger or smaller than the elements after it, and swaps their positions
#Before returning a new pivot point to be used as the partitioning split point in the two recursive calls above
def partition(listX, small, big):
    pivot = small
    for i in range(small + 1, big + 1):
        if listX[i] <= listX[small]:
            pivot += 1
            listX[i], listX[pivot] = listX[pivot], listX[i] 
    listX[pivot], listX[small] = listX[small], listX[pivot] 
    return pivot

if __name__ == "__main__":
    mainfunction()
