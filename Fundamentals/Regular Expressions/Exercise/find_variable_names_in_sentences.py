import re

text = input()
pattern = r"\b[_]([A-Z,a-z,d]+)\b"

matches = re.findall(pattern, text)
print(",".join(matches))
