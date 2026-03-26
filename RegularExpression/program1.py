import re
pattern = r"[\w\W]+@[a-zA-Z]{2,7}\.com"
pattern2 = r"\d"
text="(Hello John,Please contact support@example.com or call (555) 123-4567 for assistance.Our office is located at 123 Main St, Springfield, IL 62701.Meeting scheduled for 2024-03-15 at 14:30.Visit our website at https://www.example.com or http://test.orgServer IP: 192.168.1.100Product codes: ABC-123, XYZ-789, TEST-001Prices: $19.99, $5.00, $100.00My email is john.doe@company.co.uk and backup is john_doe@mail.netThe event is on 03/15/2024 from 2:30 PM to 4:45 PMColors: #FF5733, #00FF00, #0000FFHTML:"

a = re.findall(pattern,text)
# b = re.findall(pattern2,text)
print(a)
# print(b)
