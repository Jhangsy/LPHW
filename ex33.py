# Exercises 33
def creat_num_list(number, step):
    i = 0
    numbers = []
    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers


#print creat_num_list(6)
#print numbers
#for num in numbers:
    #rint num
#print creat_num_list(6, 3)


def creat_num_list_for(number, step):
    numbers = []
    for i in range(0, number, step):
        numbers.append(i)
        #print i
        i += 1
        #print i
    return numbers

print creat_num_list_for(6,1)
