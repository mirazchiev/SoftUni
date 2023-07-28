import re

pattern = r"(\bw{3}\.[A-Za-z0-9-\.]+\.[a-z]+)"
line = input()
valid_urls = []
while line:
    matches = re.search(pattern, line)
    if matches:
        valid_urls.append(matches.group(1))
    line = input()

for valid_url in valid_urls:
    print(valid_url)
