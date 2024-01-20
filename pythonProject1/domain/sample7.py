#
def capital(sentence):
    words=sentence.split()
    capitalword=words.capitalize()
    return " ".join(capitalword)
sentence="my name is munna"
res=capital(sentence)
print(res)