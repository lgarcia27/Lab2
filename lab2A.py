# CS2302 Data Structures
# Programmed by Luis Garcia.
# Last modified October 14, 2018.
# Instructor Diego Aguirre.
# Implementation of bubble sort, merge sort and functions to test for duplicates
# lab 2


class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    # Inserts new node into the linked list
    def insert(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.size += 1
        else:
            temp = self.head
            new_node = Node(data, None)
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            self.size += 1

    def getSize(self):
        return self.size

    def getHead(self):
        return self.head

    # This method computes the linked list and checks if there are any duplicates already present
    def solution1(self):
        currNOde = self.head
        # nested loop to compare every element
        while currNOde is not None:
            nextNode = currNOde.next
            while nextNode is not None:
                if currNOde.data == nextNode.data:
                    print("Duplicate found:", currNOde.data)
                nextNode = nextNode.next
            currNOde = currNOde.next

    # This method completes bubble sort on the linked list
    def solution2(self):
        yes_no = True
        while yes_no is True:
            yes_no = False
            temp = self.head
            while temp.next is not None:
                if temp.data > temp.next.data:
                    holds_place = Node(temp.data, None)
                    temp.data = temp.next.data
                    temp.next.data = holds_place.data
                    yes_no = True
                temp = temp.next

    # This Method creates a new array of boolean variables and updates to true if node has already been seen or inserted
    def solution4(self):
        temp = self.head
        size = self.getSize() + 1
        boolean = [False] * size
        # used to keep track of previously visited nodes
        seen_numbers = []
        duplicates_counter = 0
        while temp is not None:
            if temp.data in seen_numbers:
                boolean[temp.data] = True
                duplicates_counter += 1
            else:
                seen_numbers.append(temp.data)
            temp = temp.next
        temp = self.head
        # Printing of the array of seen nodes
        while temp is not None:
            print("There are duplicates of ", temp.data, ": ", boolean[temp.data])
            temp = temp.next
        print("The total number of found repeats is:", duplicates_counter)


# Prints Linked List
def printList(head):

    if head is None:
        print("Linked List is empty")
    else:
        temp = head
        num_elements = 0
        while temp is not None:
            print(temp.data)
            num_elements += 1
            temp = temp.next
        print("Total number of elements is:", num_elements)


# This is used for merge sort to split the list into two parts and continue to do so recursively
def separateList(head):
    if head is None or head.next is None:
        return head, None
    else:
        mid_node = head
        end_node = head.next
        while end_node is not None:
            end_node = end_node.next
            if end_node is not None:
                mid_node = mid_node.next
                end_node = end_node.next

            # Beginning of the first list
    first_half = head
    # Sves where second head of list s
    second_half = mid_node.next
    # Used to end and start both new lists
    mid_node.next = None
    return first_half, second_half


# This method is used to merge the two lists that have been split but now sorted

def mergeSort(first_half, second_half):
    new_head = Node(None, None)
    temp = new_head
    while first_half is not None and second_half is not None:
        if first_half.data <= second_half.data:  # If
            temp.next = first_half
            first_half = first_half.next
        else:
            temp.next = second_half
            second_half = second_half.next

        temp = temp.next
    if first_half is None:
        temp.next = second_half
    elif second_half is None:
        temp.next = first_half
    return new_head.next


# Main Merge Sort operation calling for spilt and merge of the linked list

def solution3(head):
    if head is None or head.next is None:
        return head
    else:
        # List split in half to sort
        first_half, second_half = separateList(head)
        first_half = solution3(
            first_half)
        second_half = solution3(second_half)
        # Sorted list is merged together to form the final complete list
    return mergeSort(first_half, second_half)


def main():
    file_activision = open("words.txt", "r")
    file_vivendi = open("nums.txt", "r")
    bubble_List = LinkedList()
    merge_List = LinkedList()
    solution4_List = LinkedList()

    for line in file_activision:
        number_id = int(line.strip())
        bubble_List.insert(number_id)
        merge_List.insert(number_id)
        solution4_List.insert(number_id)

    for line in file_vivendi:
        number_id = int(line.strip())
        bubble_List.insert(number_id)
        merge_List.insert(number_id)
        solution4_List.insert(number_id)

    print("****************************************")
    print("Test for Solution #1:")
    print("The following duplicates were found:")
    bubble_List.solution1()
    print("****************************************")
    print("Test for Solution #2:")
    print("The linked list will now be sorted using bubble sort.")
    bubble_List.solution2()
    bubble_head = bubble_List.getHead()
    printList(bubble_head)
    print("****************************************")
    print("Test for Solution #3:")
    print("The linked list will now be sorted using merge sort.")
    head = merge_List.getHead()
    sorted_LL = solution3(head)
    printList(sorted_LL)
    print("****************************************")
    print("Test for Solution #4")
    solution4_List.solution4()
    print("****************************************")


main()
