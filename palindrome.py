word=input()
word=word.lower()
reversed_word=word[::-1]

if reversed_word==word:
   print("palindrome")
else:
  print("not palindrome")