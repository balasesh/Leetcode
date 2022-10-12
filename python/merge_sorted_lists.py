def mergeTwoLists(list1 ,list2 ):
    list3 = [None] * (len(list1)+len(list2))
    i = 0
    j = 0
    k = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            list3[k] = list1[i]
            k = k+1
            i = i+1
        else:
            list3[k] = list2[j]
            k = k+1
            j = j+1

    while i < len(list1):
        list3[k] = list1[i]
        k = k+1
        i = i+1
    while j < len(list2):
        list3[k] = list2[j]
        k = k+1
        j = j+1
    return list3

list1 = [1,2,4] 
list2 = [1,3,4]
print(mergeTwoLists(list1 ,list2 ))
list1 = [] 
list2 = []
print(mergeTwoLists(list1 ,list2 ))
list1 = []
list2 = [0]
print(mergeTwoLists(list1 ,list2 ))