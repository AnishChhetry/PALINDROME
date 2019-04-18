# PALINDROME
#This is a program to check if a word or a number is palindrome or not in PYTHON.
z=input('enter any word or number')
a=list(z)
c=0
for i in z:
    if i==a[len(a)-1-a.index(i)]:
           pass
    else:
         c=='n'
if c=='n':
     print('inputted word or number is not palindrome')
else:
     print('inputted word or number is palindrome')
