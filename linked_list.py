'''
Original problem set can be found at https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/3_LinkedList/3_linked_list_exercise.md
'''


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        print_for = ''
        while itr:
            print_for += str(itr.data) + ' ~~> ' if itr.next else str(itr.data)
            itr = itr.next
        print(print_for)


    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        print_bac = ''
        while itr.next:
            itr = itr.next
        while itr:
            print_bac += str(itr.data) + ' <<< ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(print_bac)


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next
    
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            # self.head.data is None
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next




if __name__ == '__main__':
    # ll = Doubly_LinkedList()
    # ll.insert_values(["banana","mango","grapes","orange"])
    # ll.print_forward()
    # ll.print_backward()

    # ll.insert_after_value("mango","apple") # insert apple after mango
    # ll.print_forward()
    # ll.remove_by_value("orange") # remove orange from linked list
    # ll.remove_by_value("figs")
    # ll.print_forward()

    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.print_forward()


    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()