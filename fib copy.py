# File: fib.py
from bisect import bisect_left
from termcolor import colored

#set lists
int_set= [x for x in range(1, 46369)]
fib = []

#define rules for list
def fib_n(n):
    golden = (1 + 5 ** 0.5) / 2
    fib_n = int((golden ** n - (-golden) ** -n)/(5 ** 0.5))
    return fib_n

#Generate list of fibonacci numbers
for i in range(1, 25):
    fib.append(fib_n(i))

print()
print(colored('Fibonacci Sequence:', 'red'))
print(colored(fib, 'cyan'))
print()
print()

#number entered displayed as the summation of the two previous fib numbers
for i in fib:
    if i != 1:
        ind = fib.index(i)
        print(colored(str(i) + " represented as the addition of the two previous fib numbers:", 'red'))
        print(colored(str(i) + ' = ', 'magenta'), end="")
        for c, i in enumerate(range((ind-2), ind)):
            print(colored(str(fib[i]), 'magenta'), end="")
            if c != len(range((ind-2), ind)) - 1:
                print(colored(' + ', 'magenta'), end="")
        print()
        print()
print()
print()
print()

#================================FULL PROGRAM===================================

#Display fib number as addition of least number of other fib numbers possible

def max_le(seq, val):
    index = len(seq)-1
    while index >= 0:
        if seq[index] <= val:
            return seq[index]
        index -= 1
        
list1 = []
list2 = []
list3 = []
list5 = []
list8 = []
list13 = []
list21 = []
list34 = []
list55 = []
list89 = []
list144 = []
list233 = []
list377 = []
list610 = []
list987 = []
list1597 = []
list2584 = []
list4181 = []
list6765 = []
list10946 = []
list17711 = []
list28657 = []
list46368 = []
MASTER_LIST = [list1, list2, list3, list5, list8, list13, list21, list34,
               list55, list89, list144, list233, list377, list610, list987,
               list1597, list2584, list4181, list6765, list10946, list17711,
               list28657, list46368]

for i in int_set:    
    user_num = i
    print(colored("Integer: " + str(user_num), 'red'))
    print(colored("Max fib number less than integer: " + str(max_le(fib, user_num)), 'cyan'))

    num_eq = [max_le(fib, user_num)]
    counter = max_le(fib, user_num)
    while counter < user_num:
        for i in fib[len(fib)::-1]:
            if i + counter <= user_num:
                counter += i
                num_eq.append(i)

    num_eq = sorted(num_eq)
    print(colored("Fib numbers that make up integer:", 'red'))
    print(num_eq)
    print(colored("Total:", 'red'))
    print(counter)
    print()
    
#Sort into lists
    if min(num_eq) == fib[0] or min(num_eq) == fib[1]:
            list1.append(user_num)
    elif min(num_eq) == fib[2]:
            list2.append(user_num)
    elif min(num_eq) == fib[3]:
            list3.append(user_num)
    elif min(num_eq) == fib[4]:
            list5.append(user_num)
    elif min(num_eq) == fib[5]:
            list8.append(user_num)
    elif min(num_eq) == fib[6]:
            list13.append(user_num)
    elif min(num_eq) == fib[7]:
            list21.append(user_num)
    elif min(num_eq) == fib[8]:
            list34.append(user_num)
    elif min(num_eq) == fib[9]:
            list55.append(user_num)
    elif min(num_eq) == fib[10]:
            list89.append(user_num)
    elif min(num_eq) == fib[11]:
            list144.append(user_num)
    elif min(num_eq) == fib[12]:
            list233.append(user_num)
    elif min(num_eq) == fib[13]:
            list377.append(user_num)
    elif min(num_eq) == fib[14]:
            list610.append(user_num)
    elif min(num_eq) == fib[15]:
            list987.append(user_num)
    elif min(num_eq) == fib[16]:
            list1597.append(user_num)
    elif min(num_eq) == fib[17]:
            list2584.append(user_num)
    elif min(num_eq) == fib[18]:
            list4181.append(user_num)
    elif min(num_eq) == fib[19]:
            list6765.append(user_num)
    elif min(num_eq) == fib[20]:
            list10946.append(user_num)
    elif min(num_eq) == fib[21]:
            list17711.append(user_num)
    elif min(num_eq) == fib[22]:
            list28657.append(user_num)
    else:
            list46368.append(user_num)
print()
print()
print()

#Print lists
print()
print(colored("List 1", 'red'))
print(colored(list1, 'blue'))
print()
print()
print()
print(colored("List 2", 'red'))
print(colored(list2, 'blue'))
print()
print()
print()
print(colored("List 3", 'red'))
print(colored(list3, 'blue'))
print()
print()
print()
print(colored("List 5", 'red'))
print(colored(list5, 'blue'))
print()
print()
print()
print(colored("List 8", 'red'))
print(colored(list8, 'blue'))
print()
print()
print()
print(colored("List 13", 'red'))
print(colored(list13, 'blue'))
print()
print()
print()
print(colored("List 21", 'red'))
print(colored(list21, 'blue'))
print()
print()
print()
print(colored("List34", 'red'))
print(colored(list34, 'blue'))
print()
print()
print()
print(colored("List 55", 'red'))
print(colored(list55, 'blue'))
print()
print()
print()
print(colored("List 89", 'red'))
print(colored(list89, 'blue'))
print()
print()
print()
print(colored("List 144", 'red'))
print(colored(list144, 'blue'))
print()
print()
print()
print(colored("List 233", 'red'))
print(colored(list233, 'blue'))
print()
print()
print()
print(colored("List 377", 'red'))
print(colored(list377, 'blue'))
print()
print()
print()
print(colored("List 610", 'red'))
print(colored(list610, 'blue'))
print()
print()
print()
print(colored("List 987", 'red'))
print(colored(list987, 'blue'))
print()
print()
print()
print(colored("List 1597", 'red'))
print(colored(list1597, 'blue'))
print()
print()
print()
print(colored("List 2584", 'red'))
print(colored(list2584, 'blue'))
print()
print()
print()
print(colored("List 4181", 'red'))
print(colored(list4181, 'blue'))
print()
print()
print()
print(colored("List 6765", 'red'))
print(colored(list6765, 'blue'))
print()
print()
print()
print(colored("List 10946", 'red'))
print(colored(list10946, 'blue'))
print()
print()
print()
print(colored("List 17711", 'red'))
print(colored(list17711, 'blue'))
print()
print()
print()
print(colored("List 28657", 'red'))
print(colored(list28657, 'blue'))
print()
print()
print()
print(colored("List 46368", 'red'))
print(colored(list46368, 'blue'))
print()
print()
print()

#Divide every integer in list mod(12)
for list in MASTER_LIST:
    for i in range(len(list)):
        list[i] = list[i] % 12
    print(colored('list ' + str(fib_n(MASTER_LIST.index(list) + 2)) + ':', 'red'))
    print('Fib numbers in list, mod 12: ')
    print(colored(list, 'green'))
    print()




    
#//////////////////////////////FIB PART 2//////////////////////////////////////#
print()
print()
print()
print(colored("PART 2", "yellow"))
print()
print()
print()

#Create lists of consecutive fib numbers
consec_lists = []
for i in fib:
    consec_lists.append([])

counter = 0
for list in consec_lists:
    current = consec_lists[counter]
    if counter == 0:
        current.append(fib[counter])
    else:
        for i in range((counter + 1), 0, -1):
            current.append(fib[i-1])
            current.sort()
    counter += 1
    
#Print CONSECUTIVE lists
print(colored("CONSECUTIVE FIBONACCI LISTS", "red"))
print(consec_lists)
print()

#Raise each fib number in each list to fib powers in decreasing order
#Add zeros to consec lists
for list in consec_lists:
    list.insert(0, 0)
    
#Create POWER lists
pow_lists = []
for i in consec_lists:
    pow_lists.append([])
    
#Add raised elements to POWER lists  
for clist in consec_lists:
    index_count = clist.index(max(clist))
    for c in clist:
        power_count = clist[index_count]
        pow_lists[consec_lists.index(clist)].append(c ** power_count)
        index_count -=1

print(colored("POWER LISTS", "red"))
print()
for list in pow_lists:
    print("POWER list " + str(pow_lists.index(list) + 1) + ": " + str(list))
    print()
    print()

#Create ADD lists. Add together elements of power lists
add_lists = []
for list in pow_lists:
    add_lists.append([])

for plist in pow_lists:
    for i in range(len(plist) - 1):
        add_lists[pow_lists.index(plist)].append((plist[i] + plist[i + 1]))

print(colored("PASCAL ADDITION LISTS", "red"))
print()
for list in add_lists:
    print("ADD list " + str(add_lists.index(list) + 1) + ": " + str(list))
    print()
    print()

#FUNCTION TO FIND ELEMENT CLOSEST to each number in fib list
def takeClosest(myList, myNumber):
    pos = bisect_left(myList, myNumber)
    if pos == 0:
        return myList[0]
    if pos == len(myList):
        return myList[-1]
    before = myList[pos - 1]
    after = myList[pos]
    if after - myNumber < myNumber - before:
       return after
    else:
       return before
    
#Create DISTANCE_FROM lists
distance_from_lists = []
for list in pow_lists:
    distance_from_lists.append([])

for alist in add_lists:
    for i in alist:
        subtract_from = takeClosest(fib, i)
        diff = i - subtract_from
        distance_from_lists[add_lists.index(alist)].append(diff)

print(colored("DISTANCE OF EACH NEW VALUE FROM FIBONACCI NUMBER", "red"))
print()
for list in distance_from_lists:
    print("DIFFERENCE List " + str(distance_from_lists.index(list) + 1) + ": " + str(list))
    print()
    print()

#PROGRAM COMPLETE
print()
print()
print(colored("PROGRAM COMPLETE", "green"))
print()
print()
    



