class Node:
    def __init__(self, house, score, next=None):
        self.house = house
        self.value = score
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print((current.house, current.value), end=" -> " if current.next else "\n")
        current = current.next

def count_element(house_points, score):
    count = 0
    cur = house_points
    while cur:
        if cur.value == score:
            count += 1
        cur = cur.next
    return count

# Sample linked list
house_points = Node("Gryffindor", 600, 
                Node("Ravenclaw", 300,
                    Node("Slytherin", 500,
                        Node("Hufflepuff", 600))))

score = 600
print(count_element(house_points, score))  # Expected Output: 2