import zipfile
with zipfile.ZipFile("demo.zip","w") as u:
    u.write("t1.txt")
    u.write("t2.txt")
    u.write("t3.txt")