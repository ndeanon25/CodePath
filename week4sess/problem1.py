def is_valid_post_format(posts):
  dict = { ")":"(" , "]":"[", "}":"{" }
  stack=[]
  popped = ""

  for i in posts:
# if open, push on stack, else if close pop
    if  i  in dict.values():
      stack.append(i)
    else:
      if not stack:
        return False
      popped = stack.pop()
      if popped != dict[i]:
       return False
    
  if not stack:
    return True
  else:
    return False
    
print(is_valid_post_format("()")) #True
print(is_valid_post_format("()[]{}")) #True
print(is_valid_post_format("(]")) #False