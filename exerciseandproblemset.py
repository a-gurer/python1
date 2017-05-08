#A
#False. The sizes of lists can be modified by append or remove functions
#False. It is 0 based
#True
#Correct. myList.remove(index) would remove the element given the index of
#False. pop(index) would remove the elemnt given the index of. pop() would remove the last element of the list. And to print we need to add the comment print(mylist..pop(...)
#When we provide and index in append(...), an element to be added is chosen by this index but it does not determine the position that it would be added inside that list.

#A-Code analysis
listA = [1,2,3,4,
listB = [7,6,5,4,3,2]
listC = ["Apple", "Sauce", "Pizza"]
listA.append("Lucy")
#The word is added to the list A
print(listA)
listA.pop(0)
#first element of list A is excluded
print(listA)
print(listA[2])
#prints 3rd element of the list A
listB.append(listC.pop())
#adds the last element of list C to list B
print(listB)
listC.append(listB[listA[4]])
#appends the 6th (the number that corresponds to 4th element of element of list B) to the list C
print(listC)
print(listA.pop())
#prints the last element of list A
print(listA)

#B-LOOPS
#There are 2 main types of loops in Python. For and while loops. Do while and do until statements can be stated in terms of for and while loops.
#The only necessary number is the upper limit; but it is not included in the range.
#correct
for i in (1,2,3):
    s=i+5
    print (s)
#the correct form is: for x in condition
#B-Code Analysis
myList = (1,2,3,4,5)
myOtherList = []

for i in range(len(myList)):
  myOtherList.append(myList[i])
print(myOtherList)

#Programming Questions



list2=list(range(0,101))
print(list2)

sum1=sum(list2)
print(sum1)


def addOddNumbers(list2):
    odd = []
    for num in list2:
        if num % 2 == 1:
          odd.append(num)
          sumodd=sum(odd)
    print (sumodd)
addOddNumbers(list2)

def addEvenNumbers(list2):
    even = []
    for num in list2:
        if num % 2 == 0:
          even.append(num)
          sumeven=sum(even)
    print (sumeven)
    
addEvenNumbers(list2)

#problem2
listp2=[55,60,75,43,10,75,23]
        
average=sum(listp2)/len(listp2)
print(average)

sd=(((55-average)**2+(60-average)**2+(75-average)**2+(43-average)**2+(10-average)**2+(75-average)**2+(23-average)**2)/len(listp2))**(0.5)
print(sd)

def average(value):
    
    length=len(value)
    totsum=0
    for i in value:
        totsum=totsum+i
        avg=totsum/length

    print(avg)

average(listp2)

def sd(value):
    
    length=len(value)
    totsum=0
    difsqrdlist=[]
    for i in value:
        totsum=totsum+i
        avg=totsum/length
        difsqrd=(i-avg)**2
        difsqrdlist.append(difsqrd)
        standarddev=(sum(difsqrdlist)/length)**(0.5)

    print (standarddev)

sd(listp2)
