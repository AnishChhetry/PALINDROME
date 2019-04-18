z=input("")
a=list(z)
c=0
for i in z:
    if i==a[len(a)-1-a.index(i)]:
        pass
    else:
        c='not palindrome'
if c=='not palindrome':
    print('not palindrome')
else:
    print('palindrome')
