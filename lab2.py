#CS2302 Data Structures
#Programmed by Luis Garcia.
#Last modified October 22, 2018.
#Instructor Diego Aguirre.
#Implementation of linked linkedList, dictionaries, and sorting algorithms in order to determine the 20 most used passwords out of 10 million passwords.

# This is an example of how to use a dictionary.
"""
    list_with_duplicates = ["utep", "go", "utep", "utep", "miners", "go", "miners"]
    dict = {}
    
    for item in list_with_duplicates:
        if item in dict: # You can assume this operation takes O(1)
                dict[item] = dict[item] + 1
        else:
            dict[item] = 1
            print(dict["go"]) # 2
            print(dict["utep"]) # 3
            print(dict["miners"]) # 2
"""        
 import time # in order to use the function start_time = time.time() and determine running time.
class Node(object):
    def __init__(self):
        self.passwords = []
        self.doubles = []
        self.next = None # 0
            
"""To accomplish this, your program must create a linked list to store 
all of the passwords contained in the file.Your linked list must not contain any duplicates, 
so each node must store the following values:
    
○ A unique password extracted from the file (string)

○ The number of times the password appears in the file (integer)

○ A reference called ‘next’ that points to the next node in the linked list
"""
            
    
   
#Another soluton with declaring aand initializing a linkedlist class with several methods.
class linkedList(object):
    def __init__(self):
        
        self.size = 0
		self.head = None
		
	def theSize(self):
        return self.size

	# Insert method will insert the items and will keep track and count of duplicates if any.
	def insert(self, data): 
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.size += 1
            return

        curr = self.head

        while curr is not None:
            if curr.password == newNode.password:
                curr.count += 1
                break

            elif curr.next is None:
                curr.next = newNode
                self.size += 1
                break

            curr = curr.next

    # This is the Linked List print method and will print the value of the list including passwords.
	def printList(self):  
        value = self.head
        while value is not None:
            print(value.password, value.count)
            value = value.next

    # This is also a linked list method, but only for the top 20 passwords used
	def mostUsed(self): 
        curr = self.head
        print("Most used 20 passwords are: ")
        for i in range(20):
            print("Password: ", curr.password)
            print("Add: ", curr.count, "\n")
            curr = curr.next
    
  """Solution A: Every time you read a password from the file, 
  check (using a loop) if that password has already been added to the linked list.
  That is, you need to traverse the linked list to see if that password has been added already. 
  If the password is already in your linked list, update the number of times 
  the password has been seen in the file. Otherwise, add a the password to the
  linked list.
"""
    def traverseA(self, password):
        for i in range(len(password)):
            if password[i] in self.passwords:
                self.amount += 1
                self.doubles.append(password[i])
            else:
                self.passwords.append(password[i])



"""Solution B: This is a variation of Solution A. 
Instead of traversing the linked list to check if
a password has been seen before, we will be using what is called a dictionary. 
Read the following code snippet to understand how to use a dictionary 
in a similar context:
"""
   # implementation of a dictionary
# This method will print the dictionary when an index is the head.      
	def nodeDict(dict, node):  
		curr = node.head
		while curr != None:
			print(dict[curr.password].password)
			print(dict[curr.password].count)
			curr = curr.next
        
# This prints the most used passwords.
	def printmostUsed(dictionary, node):  
		curr = node.head
		for i in range(20): #The 20 most used passwords.
			print(dictionary[curr.password].password)
			print(dictionary[curr.password].count, "\n")
			curr = curr.next

# This method when the file is being readed will create a list.
	def populatesLists(dictionary, node): 
		current = node.head
		while current != None:
			dictionary[current.password] = current
			current = current.next

# This method will generate the dictionary from the file or while is being readed.
	def populatesFile(dictionary, object): 
			if object in dictionary:  
				dictionary[object] = dictionary[object] + 1
			else:
				dictionary[object] = 1

# This method will print a dictionary as long as it is not a list.
	def printDict(dict): 
		for object in dict:
			print("Password: ", object)
			print("Count: ", dict[object], "\n")
                
                
"""Once the linked list has been created, implement the following solutions 
to find the 20 passwords that appear the most in the file:
    
○ Solution A: Sort the list (in descending order) using bubble sort, 
and print the 20 most used passwords along with the number of times 
they appear in the file.


○ Solution B: Sort the list (in descending order) using merge sort, 
and print the 20 most used passwords along with the number of times 
they appear in the file.
"""


"""Implement the program described above, and upload your code to GitHub. 
Use the following Node class to construct your linked list:

    
 class Node(object):
 password = ""
 count = -1
 next = None
 def __init__(self, password, count, next):
 self.password = password
 self.count = count
 self.next = next
 """
 
#This is the program that will execute a merging sort.
 
def mergeSort(arr):
    if len(arr) > 1:
        middle = len(arr)//2
        lefthalf = arr[:middle]
        righthalf = arr[middle:]
        
		mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i = 0
        j = 0
        k = 0
        
        while (i < len(left) and j < len(right)):
            if(left[i] < right[j]):
                arr[k] = left[i]
                i = i + 1
            else:
                arr[k] = right[j]
                j = j + 1
                k = k + 1
  
        while(i < len(left)):
            arr[k] = left[i]
            i = i + 1
            k = k + 1
  
        while(j < len(right)):
            arr[k] = right[j]
            j = j + 1
            k = k + 1
            
#This is the implementation of bubble sort.
	def bubbleSort1(list):

		isSorted = False
		lastItem = len(list) - 1

		while not isSorted:
			isSorted = True

			for i in range(0, lastItem):
				if list[i] > list[i + 1]:
					list[i], list[i + 1] = list[i + 1], list[i]
					isSorted = False

			lastItem = lastItem - 1
        
    #Another implementation of bubble sort in case the previous one presented an error.
    #We can test it directly by creating an array of numbers. 
	def bubbleSort
		array = [7,27,8,13,41,36,17,11] #Array that will be tested.
		#Represenets the lenght of the array.
		n = len(array)   
		passNum = 1
	 #Will swap the elements.
		while(passNum <= n - 1):
			index = 0
			while(index <= n - passNum - 1):
				if array[index]>array[index + 1]:
					array[index],array[index + 1] = array[index + 1],array[index]  
					index = index + 1
					passNum = passNum  + 1
			for item in array:
				print item
	  
#Main method.
 
	def main():
		# This will open the file and will help in encoding
		file = open("10-million-combos.txt", "r", encoding = "utf-8") 
	"""
		print("\nBubble Sort")
		bubbleList.bubbleSort1()
		bubbleList.mostUsed()
		print("\nMerge Sort")
		mergeSort(mergeList.head)
		mergeList.mostUsed()
		print("\nSorted Dictionary: ")
		printDict(populatesFile)
		print("\nPost-Sorted Dictionary")
		populatesLists(sortedDict, bubbleList)
		nodeDict(sortedDict, bubbleList)
	"""
		#I used 10,000 since 10,000,000 will be a lot and will take longer for the program to run.
		start_time = time.time()
		engine = Node()
		for i in range(10000):
			# The passwords will be splitted
			engine.traverseA(txt.readline().split('\t'))
		print("The time", .format(time.time() - start_time)) 
		
		

  