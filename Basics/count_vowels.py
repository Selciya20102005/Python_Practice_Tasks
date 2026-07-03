vowels=['a','e','i','o','u']
word=input("enter the word:")
count=0
word_li=list(word)
for i in range(len(word_li)):
  if word_li[i] in vowels:
   count+=1
print("vowels count:",count)