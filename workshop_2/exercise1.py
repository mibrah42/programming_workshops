class Stack:
    # TASK:
    #   This stack data structure has the push and pop methods
    #   already implemented. Your task is to add the peek method.
    def __init__(self):
        self.items = []
        self.topOfStack = -1
    def pop(self):
        if self.topOfStack == -1:
            raise Exception("cannot pop - stack is empty")

        # Python already implements the pop method,
        #   so it is also correct to just do this:
        # return self.items.pop()

        # 1. Get the value at the top of the stack
        lastItem = self.items[self.topOfStack]

        # 2. Remove the item from the stack
        del self.items[self.topOfStack]

        # 3. Update the "stack pointer" by subtracting 1
        self.topOfStack = self.topOfStack - 1

        # 4. Return the value we took from the stack
        return lastItem

    def push(self, newValue):
        # 1. Append the item to the end of the list (top of stack)
        self.items.append(newValue)

        # 2. Update the "stack pointer" by adding 1
        self.topOfStack = self.topOfStack + 1
    
    def peek(self):
        # This function should return the value on top
        #   of the stack like pop does, but without removing
        #   the item from the stack.
        return # lastItem

class Queue:
    # Task:
    #  This queue takes a long time to dequeue items because it has
    #  to move every item in the array, but it can enqueue items very
    #  quickly beadding them to the end of the array.
    #
    #  Your task is to implement a new Queue class, called Queue2,
    #  that will enqueue items slowly and dequeue items quickly.
    #
    #  Note: these kinds of queues are called "array queues",
    #        but there are other more efficient implementations.
    def __init__(self):
        self.items = []

    def enqueue(self, newValue):
        self.items.append(newValue)

    def dequeue(self):
        if len(self.items) < 1:
            raise Exception("cannot dequeue - queue is empty")

        # 1. Get the first item that was enqueued
        nextItem = self.items[0]

        # 2. Shift the array (this also removes the first item)
        for i in range(len(self.items)-1):
            self.items[i] = self.items[i+1]

        # 3. Remove the old copy of the last element
        #    (we need to do this after shifting the array)
        del self.items[len(self.items) -1]

        # 4. Return the value we took from the queue
        return nextItem

class Node: # for linked-list
    def __init__(self, value, nextNode):
        self.value = value
        self.next  = nextNode

class LinkedList:
    # Task:
    #   This LinkedList data structure has the "easy methods" already
    #   implemented. The remaining methods are addLast(value), popLast(),
    #   and insert(index, value)
    #
    #   A getLast() method has been implemented as a starting point for
    #   addLast() and popLast()
    #
    #   For popLast, keep in mind you will need to update the second-last node
    #   so that it points to None instead of the last node (otherwise the last
    #   node will not be removed from the linked list)
    #
    #   It is likely your first implementation of popLast will fail if the last
    #   item is also the first item. This is a bit tricky to handle, so focus
    #   on having it work with more than one item in the linked list first.
    def __init__(self):
        # If the first item is "None", that means the
        # linked-list is empty.
        self.firstItem = None
    
    def addFirst(self, newValue):
        """Append newValue, which will become the new firstItem.

        This method is similar to push() on a stack.
        """
        # Create a new node. This will be the new first item,
        # and it will point "next" to the previous first item.
        newNode = Node(newValue, self.firstItem)

        # Set this node as the new first item.
        self.firstItem = newNode

    def popFirst(self):
        """Return the value of the first item and remove it from the linked list.

        This method is similar to pop() on a stack.
        """

        if self.firstItem == None:
            raise Exception("cannot popFirst - linked list is empty")

        oldFirstItem = self.firstItem
        self.firstItem = oldFirstItem.next
        return oldFirstItem

    def getLast(self):
        """Return the value of the last item withut removing it.
        """

        if self.firstItem == None:
            raise Exception("cannot getLast - linked list is empty")

        # 1. Find the last item
        lastItem = self.firstItem
        while lastItem.next != None:
            lastItem = lastItem.next

        # 2. Return the value
        return lastItem

def main():
    print("\nRunning the stack functions")
    mystack = Stack()
    mystack.push(1)
    mystack.push(2)
    mystack.push(3)
    mystack.push(4)
    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())
    try:
        print(mystack.pop())
    except:
        print("last pop fails because the stack is empty")

    print("\nRunning the queue functions")
    myqueue = Queue()
    myqueue.enqueue(1)
    myqueue.enqueue(2)
    myqueue.enqueue(3)
    myqueue.enqueue(4)
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    print(myqueue.dequeue())
    try:
        print(myqueue.dequeue())
    except:
        print("last dequeue fails because the queue is empty")

    print("\nRunning the linked-list functions")
    mylinkedlist = LinkedList()
    mylinkedlist.addFirst(1)
    mylinkedlist.addFirst(2)
    mylinkedlist.addFirst(3)
    mylinkedlist.addFirst(4)

    print(mylinkedlist.getLast().value)

    print(mylinkedlist.popFirst().value)
    print(mylinkedlist.popFirst().value)

    print(mylinkedlist.getLast().value)

    print(mylinkedlist.popFirst()) # See what happens when ".value" is omitted
    print(mylinkedlist.popFirst().value)

    try:
        print(mylinkedlist.popFirst().value)
    except:
        print("last popFirst fails because the linked list is empty")

# Run the main function only if this file is run as a program.
# (so main will not run if we import it in another Python program)
if __name__ == "__main__":
    main()
