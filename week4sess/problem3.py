def is_symmetrical_title(title):
  left = 0
  right = len(title) - 1

  while left < right:
    if title[left] == " ":
        left += 1
    if title[right] == " ":
        right -= 1
    if title[left].lower() != title[right].lower():
       return False
    left += 1
    right -= 1
  return True


print(is_symmetrical_title("A Santa at NASA")) # True
print(is_symmetrical_title("Social Media")) #False