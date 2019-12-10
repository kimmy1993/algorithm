import time
import random

def cocktail_sort(list_before):

    if not list_before:
        return []

    listdata = list_before

    i,j, k = 0, len(listdata)-1, 0
    move_up = True

    #sort
    while i < j:

        if move_up:
            #k is up to maximum
            while k< j:
                #when up side is bigger than now, switch
                if listdata[k] > listdata[k+1]:
                    save = listdata[k+1]
                    listdata[k+1] = listdata[k]
                    listdata[k]= save
                k+= 1

            #maximum down
            j -= 1
            move_up = False

        else:
            #k is down to minimum
            while i < k:
                #when down side is bigger than now, switch
                if listdata[k] < listdata[k-1]:
                    save = listdata[k-1]
                    listdata[k-1] = listdata[k]
                    listdata[k] = save
                k -= 1
            #minimum up
            i+= 1
            move_up = True


    return listdata



list_insert_rand = []

end_list = []

#random data(min : 1, maxinum : 4096) input for random size(min : 1, maximum : 1024)
for i in range(0,random.randrange(1,1024)):
    list_insert_rand.append(random.randrange(1,4096))
print("before sort:")
print(list_insert_rand)

end_list = cocktail_sort(list_insert_rand[:])


print("End sort: ")
print(end_list,"\n")

#if doing sort and system sort is same, it say success , but it is different, it say fail
if sorted(list_insert_rand) == end_list:
    print("\n sort success")
else:
    print("\n sort fail")

time.sleep(10)
