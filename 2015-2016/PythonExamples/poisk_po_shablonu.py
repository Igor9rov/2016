import re
match = re.match('Hello[ \t]*(.*)world', 'Hello Python world')
print(match.group(1))

match = re.match('/(.*)/(.*)/(.*)', '/usr/home/lumber jack')
print(match.groups())