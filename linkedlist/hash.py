def count_word_frequency(text):
    word_count = {}

    words = text.split()

    
    for word in words:
        word = word.lower().strip(".,!?")
        if word in word_count:
            word_count[word] += 1 
        else:
            word_count[word] = 1   

    return word_count

text = "This is a test example from a code created by haroon"
frequencies = count_word_frequency(text)

for word, count in frequencies.items():
    print(f"{word}: {count}")
