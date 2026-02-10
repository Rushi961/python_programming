list1 = [] #Empty List
print(type(list1))

list2 = [10,30,60] #List of integers numbers
list3 = [10.77,30.66,60.89] #list of float numbers
list4 = ['one','two','three'] #list of String
list5 = ['Asif', 25,[50,100],[150,90]] #nusted list
list6 = [100, 'Asif', 17.765] #list of mixed data type 
list7 = ['Asif', 25,[50, 100],[150, 90],{'john', 'David'}]
print(len(list6))
#List Indexing
list2[0] #Retreve first element of the list
list4[0] #Retreve first element of the list 
list4[0][0] #Nested indexing - Access the first character of the first list ele
list4[-1] #Last itam of the list
list5[-1] #Last itam of the list 
#List Slicing
mylist = ['one', 'two', 'three','four','five','six', 'seven', 'eight']
mylist[0:3] #Return all itam from 0th to 3rd index location excluding the itam
mylist[2:5] #List all items from 2nd to 5th index location excluding the itam a
mylist[:3] #list all items from 2nd to 5th index location excluding the itam a 
mylist[:2] #Return first two itam
mylist[-3:] #return last three items
mylist[-2:] #Return last two itam
mylist[-1:] #Return last itam of the list
mylist[:] #Return whole list

#Add, Remove & Change Items

mylist
mylist.append('nine') #Add an item to the end of the list
mylist
mylist.insert(9,'ten') #Add item at index Location9
mylist
mylist.insert(1,'one') #Add item at index location 1
mylist
mylist.remove('one') #Remove item "one"
mylist
mylist.pop() #remove last item of the list
mylist
mylist.pop(8) #Remove itam at index location 8
mylist
del mylist[7] #Remov item at index location 7
mylist

#Change value of the string 
mylist[0] = 1
mylist[1] = 2
mylist[2] = 3
mylist
mylist.clear() #Empty list / Delete all items in list
mylist

#Copy List

mylist = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
mylist1 = mylist #create a new reference "mylist1"
id(mylist) , id(mylist) #The address of both mylist & mylist will be the same 
mylist2 = mylist.copy() #Create a copy of the list
id(mylist2) # The address of mylist2 will be different from mylist becaise mylist

mylist[0] = 1
mylist

mylist1 #mylist will be also impacted as it is pointing to the same list
mylist2 #Copy of list won't be impacted due to changes made on the original list

#Join List

list1 = ['one', 'two', 'three','four']
list2 = ['five', 'six', 'seven','eight']
list3 = list1 + list2 #join two lists by '+' operator
list3
list1.extend(list2) #Append List2 with list1
list1

#List Membership

list1
'one' in list1 #Check if 'one' exist in the list
'ten' in list1 #Check if 'ten' exist in the list
if 'three' in list1: #Check if 'three' exist in the list
    print('Three is present in the list')
else:
    print('Three is not present in the list')
if 'eleven' in list1: #Check if 'eleven' exist in the list
    print('eleven is present in the list')
else:
    print('eleven is not present in the list')
    
#Reverse & Sort List

list1
list1.reverse() #Reverse the list
list1
List1 = list1[::-1] #Reverse the list
list1
mylist3 = [9,5,2,99,12,88,34]
mylist3.sort(reverse=True) #Sort list in descending order
mylist3
mylist4 = [88,65,33,21,11,98]
sorted(mylist4)    #Returns a new sorted list and doesn't change original list
mylist4


#Count
list10 = ['one', 'two', 'three', 'four', 'one', 'one', 'two', 'three']
list10.count('one')  #Number of time item "one" occurred in the list.
list10.count('two') #Occurence of item 'two' in the list
list10.count('four') #Occurence of item 'four' in the list
 






