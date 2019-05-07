# Lecture day one of Data-Structur


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        def add_to_tail(self, value):
            # wrap the value in a new node
            new_node = Node(value)
            # 1. What if our linked list is empty
            # how do we even check if our linked list is empty ?
            if not self.head and not self.tail:
                # if our list is empty, then the node that we add to
                # the list needs to be set as both the head and the tail
                self.head = new_node
                self.tail = new_node
            # 2. what if our linked list is not empty
            else:
                # add to the tail of the list
                # update the tail node's next_node reference to point to the new node
                self.tail.set_next(new_node)
                # dont' forget to update the linked list's self.tail reference
                self.tail = new_node

          def remove_head(self):
            # 1. what if our linked list is empty?
            if not self.head and not self.tail:
              return None
            # 2. what if our linked list has one node?
            # how dow we check if our linked list only has one node ?
            if self.head == self.tail:
            # if not self.head.get_neext():
            # now we can go ahead and set both head and tail to None
              old_head = self.head
              self.head = None
              self.tail = None
              return head.get_value()
            # 2. what if our linked list has more than  one node?
             else:
               # set the list's head reference to refer to the head node's next node
              old_head = self.head
              self.head = self.head.get_next()
              return old_head.get_value()

            def contains(self, value):
              # make sure we have elements in the list to treverse
              if not self.head and not self.tail:
                return None
              current = self.head
              # keep traversing while we're at a valid node
              while current:
                if current.get_value() == value:
                  return True
                # update our current pointer
                current = current.get_next()
              # we've traversed the entire list and none of the list nodes
              # have the value we're looking for, return False
              return False
