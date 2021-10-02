#%%
import re
with open(r'./data.txt','r') as file:
    text=file.read()
#%%
# emails
pattern1=re.compile("\w+@\w+.(com)")
s=pattern1.finditer(text)
l=[]
emails=[]
for i in s:
    l.append(i.span())
for i,j in l:
    emails.append(text[i:j])
print(emails)
#%%
# numbers
pattern2=re.compile("\d{3}-\d{3}-\d{4}")
n=pattern2.finditer(text)
numbers=[text[i.span()[0]:i.span()[1]] for i in n]
print(numbers)
# %%
# names
pattern3=re.compile("[\nA-Z][a-z]+\s(?!St)[A-Z][a-z]+")
o=pattern3.finditer(text)
names=[text[i.span()[0]:i.span()[1]] for i in o]
print(names)
# %%
# addresses
pattern4=re.compile("\n\d{3}\s[^\n].+")
a=pattern4.finditer(text)
addresses=[text[i.span()[0]:i.span()[1]] for i in a]
print(addresses)
