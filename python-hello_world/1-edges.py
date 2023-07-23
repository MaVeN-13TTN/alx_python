word = "Holberton"
word_first_3 = word [:3]
word_last_2 = word [7:]
middle_word = word [-8:-1]
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))

'''
word = ["school", "Holberton"]
for word in word: 
    word_first_3, word_last_2, middle_word = word[:3], word[-2:], word[1:-1]; 
print(f"First 3 letters: {word_first_3}\nLast 2 letters: {word_last_2}\nMiddle word: {middle_word}\n")

words = ["school", "Holberton"]
word_first_3, word_last_2, middle_word = words[0][:3], words[0][-2:], words[0][1:-1]
print(f"First 3 letters: {word_first_3}\nLast 2 letters: {word_last_2}\nMiddle word: {middle_word}\n")
word_first_3, word_last_2, middle_word = words[1][:3], words[1][-2:], words[1][1:-1]
print(f"First 3 letters: {word_first_3}\nLast 2 letters: {word_last_2}\nMiddle word: {middle_word}\n")
'''