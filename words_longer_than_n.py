def words_longer_than_n(word_list, n):
    result = []
    for word in word_list:
        if len(word) > n:
            result.append(word)
    return result

# Example usage
word_list = ["apple", "banana", "grape", "kiwi", "orange", "pineapple"]
n = 3

long_words = words_longer_than_n(word_list, n)
print("Words longer than", n, "characters:", long_words)
