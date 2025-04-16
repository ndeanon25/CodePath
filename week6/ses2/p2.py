class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    curr = evidence
    tempCurr = curr.next
    found = False
    tempStack = []
    while curr:
        if curr.next == evidence:
            tempStack.clear()
            found = True
        else:
            tempStack.append(curr)
        curr = curr.next  
    
    # if bool == false
    # return collect_false_evidence and change curr to curr.next
    if found == False:
        print("Hello")
        return tempStack 
    collect_false_evidence(tempCurr)


clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

# ['The stolen goods are at an abandoned warehouse', 'The mayor is accepting bribes', 
# 'They dumped their disguise in the lake']
# []