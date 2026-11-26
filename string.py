from collections import Counter
og="Apples are Apples colour"
rep=og.replace("Apples","Orange")
rep_c=og.replace("p","o")
print("Original String :",og)
print("Replaced String Apples with Oranges:",rep)
print("Replaced Characters p with o :",rep_c)
words=og.split()
w_c=Counter(words)
ch_c=Counter(og.lower())
print("The Frequency of Characters  :",dict(ch_c))
print("The Frequency of String:",dict(w_c))
txt=input("Enter a String :").lower()
print("Reversed String :",txt[::-1])
if txt==txt[::-1]:
    print(txt," is a palindrome")
else:
    print(txt," is not a palindrome")


