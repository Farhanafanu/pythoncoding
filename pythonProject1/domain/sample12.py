# Using list comprehension to generate a list of lengths of words
sentence = "This is an example sentence for list comprehension."
word_lengths = [len(word) for word in sentence.split()]

print(word_lengths)
