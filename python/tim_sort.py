import time
import random

#size is low than 16, use insert sort
#size is over than 16, use merge sort
def tim_sort(listdata):
    num = len(listdata)

    if num <= 16:
        return in_sort(listdata)
    else:
        return m_sort(listdata)

#insert sort
def in_sort(listdata):

    list_len = len(listdata)

    #insert sort
    for i in range(1,list_len):
        j = i-1
        while j >= 0 and listdata[j] > listdata[i]:
            j -= 1
        j+= 1
        #if input data is correct side, going next
        if j == i:
            continue
        #if inputdata is not correct side, push correct thing
        else:
            listdata = listdata[0:j] + listdata[i:i+1] + listdata[j:i] + listdata[i+1:]

    return listdata

#merge sort
def m_sort(listdata):
    
    list_len = len(listdata)

    #if slice is lower than 16, use insert sort
    if list_len <= 16:
        listdata = in_sort(listdata)
        return listdata
    
    middle = int(list_len/2)
    return_list = []
    i , j = 0, 0
    #slice list and go merge sort(front, end)
    return_list = m_sort(listdata[:middle])
    
    listdata = m_sort(listdata[middle:])
    
    j_max = len(listdata)
    while i < list_len:
        if i >= len(return_list):
            i += 1
            return_list.append(listdata[j])
            j += 1
        elif j >= j_max:
            break
        elif return_list[i] > listdata[j]:
            return_list.insert(i,listdata[j])
            i+= 1
            j+= 1
        else:
            i += 1



    return return_list


list_insert_rand = []

end_list = []

#random data(min : 1, maxinum : 4096) input for random size(min : 1, maximum : 1024)
for i in range(0,random.randrange(1,1024)):
    list_insert_rand.append(random.randrange(1,4096))
print("before sort:")
print(list_insert_rand)

end_list = tim_sort(list_insert_rand[:])

print("End sort: ")
print(end_list,"\n")

#if doing sort and system sort is same, it say success , but it is different, it say fail
if not sorted(list_insert_rand) == end_list:
    print("\n sort fail")
else:
    print("\n sort success")

time.sleep(10)
