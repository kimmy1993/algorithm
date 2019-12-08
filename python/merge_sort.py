import time
import random


def m_sort(listdata):

    if len(listdata) <= 1:
        return listdata

    middle = int(len(listdata)/2)

    return_list = []
    sub_list = []
    i , j = 0, 0
    list_len = 0

    return_list = m_sort(listdata[:middle])
    
    sub_list = m_sort(listdata[middle:])

    list_len = len(return_list + sub_list)

    while i < list_len:
        if i >= len(return_list):
            i += 1
            return_list.append(sub_list[j])
            j += 1
        elif j >= len(sub_list):
            break
        elif return_list[i] > sub_list[j]:
            return_list.insert(i,sub_list[j])
            i+= 1
            j+= 1
        else:
            i += 1



    return return_list


list_insert_rand = []

end_list = []

for i in range(0,10):
    list_insert_rand.append(random.randrange(1,1025))
print("before sort:")
print(list_insert_rand)

end_list = m_sort(list_insert_rand)

print(end_list)

time.sleep(10)
