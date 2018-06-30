import re
string = 'my name is alok my dalokrockstar@outlook.com age is 26 my email is alokchoudhary162@gmail.com 40'
print(re.findall('\S+@\S+.com',string))

# o/p [dalokrockstar@outlook.com, alokchoudhary162@gmail.com]