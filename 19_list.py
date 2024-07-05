num_list = [1,2,3,4,5,6,7,8,9,0,2,1]

name_list = ["Abhi", "Abhi", "Kumar"]

mix_list = [1, "Abhi", 10.9, True, 'A']


print(num_list)

print(name_list)

print(mix_list)

print("length of the list is : " + str(len(num_list)))

print("List allows (-)ve numbers to index from the end of the list : " + str(num_list[-1]))

print("List starts from 0th index to complete end -> [0:] : " + str(num_list[0:]))

print("List starts from 1st index to 3 - 1 position -> [1:3] : " + str(num_list[1:3]))

print("List starts from 0th index to 5 - 1 position -> [1:3] : " + str(num_list[:5]))

print("List starts from 0th index to 5 - 1 position & jump 2 elements-> [0:5:2] : " + str(num_list[0:5:2]))

print(max(num_list))


print("Using sort() function to sort the list : ")

num_list.sort()

print(num_list)


print("Using reverse() function to reverse the list : ")

num_list.reverse()

print(num_list)


print("Using append() function to append in the list this function accepts only one argument: ")

num_list.append(10)

print(num_list)


print("Using insert() function to insert the in list, this function accepts 2 arguments - insert(index_num, value): ")

num_list.insert(2, 11)

print(num_list)


print("Using extend() function to extend the list : ")

num_list.extend([12,13,14,15,16,17,18,19,20])

print(num_list)


print("Using remove() function to remove element from the list : ")

num_list.remove(1)

print(num_list)


print("Using pop() function to remove last element from the list : ")

num_list.pop()

print(num_list)

# there are lots of functions present in the python documentation which you can use apar from the listed above