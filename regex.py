import re

"""
must start with character

"""
pattern_str = r'^[a-z]\w*@[a-z]\w*\.[a-z]{3}'
pattern = re.compile(pattern_str)
str = 'hello@example.com'
str1 = 'hello@3example.com'
print(re.match(pattern=pattern,string=str1))