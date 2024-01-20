# f=open("fanu.py","wb+")
with open("fanu.py","r")as f:
    x=f.read()
    print(x)
f=open("fanu.py","w")
f.write('hai')
f.close()