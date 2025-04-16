class Node:
    def __init__(self, potion, next=None):
        self.potion = potion
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.potion, end=" -> " if current.next else "\n")
        current = current.next


def reverse(events):
    current = events
    while current:
        temp = current.next
        current = current.next
        current.next = temp



events = Node("Potion Brewing", 
            Node("Spell Casting", 
                Node("Wand Making", 
                    Node("Dragon Taming", 
                        Node("Broomstick Flying")))))

print_linked_list(reverse(events))