import random
import time

def q_sort(listdata):
    if len(listdata) <= 1:
        return listdata

    middle = int(len(listdata)/2)
    return_data = []
    i = 0
    while i < len(listdata):
        if i < middle and listdata[i] > listdata[middle]:
            save = listdata[i]
            del listdata[i]
            listdata.insert(middle,save)
            middle -= 1
            i -= 1
        elif i > middle and listdata[i] < listdata[middle]:
            save = listdata[i]
            del listdata[i]
            listdata.insert(middle,save)
            middle +=1
        i+= 1

    return_data += q_sort(listdata[:middle])

    return_data += listdata[middle:middle+1]

    return_data += q_sort(listdata[middle+1:])

    return return_data


list_insert_rand = []

end_list = []

for i in range(0,10):
    list_insert_rand.append(random.randrange(1,1025))
print("before sort:")
print(list_insert_rand)

end_list = q_sort(list_insert_rand)

print(end_list)

time.sleep(10)
