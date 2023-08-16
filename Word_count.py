input_sentence = input("Enter sentence: ")
word_counts = {}

# Split the sentence into words
words = input_sentence.split()

for word in words:
    # Remove punctuation and convert to lowercase for consistent counting
    word = word.strip(".,!?").lower()
    
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word, count in word_counts.items():
    print(f"'{word}': {count}")
