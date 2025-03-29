

def reverse_comments_queue(comments):
    newlist = []
    stack = [] 
    for comment in comments:
        stack.append(comment)
    for i in range(len(stack)):
        newlist.append(stack.pop())
    return newlist

    # comments[::-1]


print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

