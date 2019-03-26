###########################################
#            William Francis              #
#               3/14/19                   #
#             CSC 325-001                 #
#       Assignment:"Find it fast"         #
###########################################

import time


# Brute Force Algorithm

def brute(userin, input):

    # Brute Force Method
    y = 0
    print("\nBrute Force Method Initiated!\n")
    # print("Cycle # |  Status ")
    inputlength = input.length()
    n = 0
    m = 0
    counter = 0
    userlength = len(userIn)


    while counter != inputlength:

        DataIn1 = (input.listdata(m))
        DataUser = (userList.listdata(n))
        counter += 1

        if DataIn1 != DataUser:

            n = 0
            DataUser = (userList.listdata(n))

            if DataIn1 == DataUser:

                n += 1
                m += 1
                if userlength == n:
                    y += 1
                    endp = counter
                    startp = (endp - userLength + 1)

                    pos.append(startp)
                    pos.append(endp)
                    n = 0
                    continue
                else:
                    continue

            elif DataIn1 != DataUser:

                m += 1
                continue

        elif DataIn1 == DataUser:

            n += 1
            m += 1

            if userlength == n:
                y += 1
                endp = counter
                startp = (endp - userlength + 1)
                pos.append(startp)
                pos.append(endp)
                n = 0
                continue
            else:
                continue

    if y > 0:
        u = y
        e = 0
        f = 1
        cou = 1
        while y != 0:
            print("Found at: ", pos[e])
            cou += 1
            e += 2
            f += 2
            y -= 1
        print("Found", u, " Times! ")
    elif y == 0:
        print("\nYour substring must be somewhere else , ¯\_(ツ)_/¯ Sorry :(\n")
        return -1

# KMP Algorithm


def kmp(seq, subseq):

    print("\nKMP Method Initiated\n")
    n = seq.length()
    m = userList.length()
    pi = prefix(subseq)
    k = 0
    y = 0
    for i in range(n):
        while k > 0 and userList.listdata(k) != seq.listdata(i):
            k = pi[k - 1]
        if userList.listdata(k) == seq.listdata(i):
            k += 1
        if k == m:
            print("Found at: " + str(((i + 2) - m)))
            y += 1
            k = 0
    if y == 0:
        print("\nYour substring must be somewhere else , ¯\_(ツ)_/¯ Sorry :(\n")
        return -1
    if y != 0:
        print("Found", y, " Times!")


def prefix(seq):
    m = userList.length()
    pi = range(m)
    k = 0

    for i in pi[1:]:
        while k > 0 and userList.listdata(k + 1) != userList.listdata(i):
            k = pi[k]
        if userList.listdata(k + 1) == userList.listdata(i):
            k = k + 1
        i = k

    return pi


# Boyer Moore Algorithm

# I was able to use my Singly Linked List with my listdata def I made

NO_OF_CHARS = 256


def badCharHeuristic(string, size):


    badChar = [-1] * NO_OF_CHARS

    for i in range(size):
        badChar[ord(userList.listdata(i))] = i;

    return badChar


def boyermoore(txt, pat):

    h = 0
    print("\nBoyer Moore Method Initiated\n")
    m = userList.length()
    n = txt.length()

    badChar = badCharHeuristic(pat, m)

    s = 0
    while (s <= n - m):
        j = m - 1

        while j >= 0 and userList.listdata(j) == txt.listdata(s + j):
            j -= 1

        if j < 0:
            print("Found at: {}".format(s + 1))
            h += 1
            s += (m - badChar[ord(txt.listdata(s + m))] if s + m < n else 1)
        else:

            s += max(1, j - badChar[ord(txt.listdata(s + j))])
    if h == 0:
        print("\nYour substring must be somewhere else , ¯\_(ツ)_/¯ Sorry :(\n")
        return -1
    if h != 0:
        print("Found", h, " Times!")



# finds fastest algorithm


def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else:
        smallest_num = num3
    print("The Fastest Speed is : ", smallest_num, "seconds")
    if num1 == smallest_num:
        print("Brute Force is the Fastest Algorithm")
    elif num2 == smallest_num:
        print("KMP is the Fastest Algorithm")
    elif num3 == smallest_num:
        print("Boyer Moore is the Fastest Algorithm")

# Linked List


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode at the end
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Print Node Index
    def listdata(self, index):
        node = self.headval
        for x in range(index):
            node = node.nextval
        return node.dataval

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def length(self):
        count = 0
        printval = self.headval
        while printval is not None:
            count += 1
            printval = printval.nextval
        return count


# Menu Thingy
# It's really extra lol but it gives it personality

n = 0
while n == 0:
    answer = input("HELLLOOOOOO!! Would you like to use my Substring Location Program!?!?!?\n")
    if answer == "yes":
        print("YAYYYYYYYYY!!!! :D", "\n")
        break
    elif answer == "no":
        print("Well then, let me ask again!!!!! :)\n")
        continue
    else:
        print("I have no idea what you just said\n")
        print("Anwser with 'yes' or 'no' please :)\n")
        print("It's okay! let me ask again!!!!!\n")
        continue


# User Input

userIn = input("What substring would you like to search for? \n")
print("Okay! My program search for:", userIn, "\n")

# lower cases all characters to not be case sensitive

userIn = userIn.lower()

# Puts User Input into a Linked List

userList = SLinkedList()
userList.headval = Node(userIn[0])

j = 1

while j < len(userIn):
    userList.AtEnd(userIn[j])
    j += 1


# Read Input1.txt & Input2.txt

Input1 = open(r"Input1.txt", "r")
Input2 = open(r"Input2.txt", "r")

In1 = (Input1.read())
In2 = (Input2.read())

# lower cases all characters to not be case sensitive

In1 = In1.lower()
In2 = In2.lower()

# Choosing Input1 or Input2 + Main Code

pos = []
a = 0
while a == 0:
    answer = input("Which text file would you like to search?\nInput1.txt = '1' , Input2.txt = '2'\n")
    if answer == "1":
        print("Input1.txt Selected, \n")

        # Puts Input1 into a Linked List

        In1List = SLinkedList()
        In1List.headval = Node(In1[0])

        i = 1

        while i < len(In1):
            In1List.AtEnd(In1[i])
            i += 1

        # Brute Force Method

        start = time.time()

        brute(userList, In1List)

        end = time.time()
        print("\n", end - start, "seconds\n")
        brutetime = (end - start)

        # KMP Method
        start = time.time()

        kmp(In1List, userList)

        end = time.time()
        print("\n", end - start, "seconds\n")
        kmptime = (end - start)

        # Boyer Moore Method
        start = time.time()

        boyermoore(In1List, userList)

        end = time.time()
        print("\n", end - start, "seconds\n")
        boyertime = (end - start)

        smallest(brutetime, kmptime, boyertime)

        break

    elif answer == "2":
        print("Input2.txt Selected\n")
        print("Putting Input2.txt into a linked list takes my program around 67 - 68 Seconds\n")

        # Puts Input2 into a Linked List

        In2List = SLinkedList()
        In2List.headval = Node(In2[0])
        b = 1
        while b < len(In2):
            In2List.AtEnd(In2[b])
            b += 1

        # Brute Force Method
        start = time.time()

        brute(userList, In2List)

        end = time.time()
        print("\n",end - start, "seconds\n")
        brutetime = (end - start)

        # KMP Method
        start = time.time()

        kmp(In2List, userList)

        end = time.time()
        print("\n", end - start, "seconds\n")
        kmptime = (end - start)

        # Boyer Moore Method
        start = time.time()

        boyermoore(In2List, userList)

        end = time.time()
        print("\n", end - start, "seconds\n")
        boyertime = (end - start)

        smallest(brutetime, kmptime, boyertime)

        break

    else:
        print("I have no idea what you just said\n")
        print("Anwser with '1' or '2' please :)\n")
        print("It's okay! let me ask again!!!!!\n")
        continue

# I am extremely glad we are able to code in python I am way stronger in python than java
#
# Websites I used for help:
#
# Sorry its a lot I just wanted to include everything
#
# https://stackoverflow.com/questions/15221516/printing-one-character-at-a-time-from-a-string-using-the-while-loop
# https://www.tutorialspoint.com/python/python_linked_lists.htm
# https://stackabuse.com/getting-user-input-in-python/
# https://www.w3schools.com/python/python_conditions.asp
# https://www.w3schools.com/python/python_while_loops.asp
# https://stackoverflow.com/questions/50095248/how-to-get-node-for-negative-index-in-a-linked-list
# https://www.tutorialspoint.com/python/list_append.htm
# https://stackoverflow.com/questions/42333383/brute-force-algorithm-and-string-matching
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
# https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/
# https://gist.github.com/ujwaltrivedi/3a74eba536680f9c911b
# https://gist.github.com/Derog/f7363522246129c9f25a
# https://medium.com/programminginpython-com/python-program-to-find-the-biggest-and-smallest-of-3-numbers-5978c1e8fbfa
#
