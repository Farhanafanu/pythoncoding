def capitalize_alternate_words(sentence):
    words = sentence.split()
    capitalized_words = [word.upper() if word % 2 == 0 else word for  word in words]
    return " ".join(capitalized_words)

sentence = "this is an example of capitalizing alternate words in a string"
result = capitalize_alternate_words(sentence)
print(result)
