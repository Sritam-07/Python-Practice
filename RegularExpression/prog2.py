import re
ph_no = input("Enter your phone number")
pattern = r'\+91 [6-9]\d{9}'
ans = re.fullmatch(pattern,ph_no)
print(ans)