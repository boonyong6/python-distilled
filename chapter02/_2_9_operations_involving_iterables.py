words = ["apple", "boy", "cat", "dog"]

for word in words:
    print(word)

# Unpack a list
word1, word2, *remaining_words = words
print("1st word:", word1, ",", "2nd word:", word2)
print("Remaining words:", remaining_words)

new_word = "elephant"
print(
    f"{new_word} is in the list."
    if new_word in words  # Membership test
    else f"{new_word} is not in the list."
)

# Expansion in a list
reordered_words = [*remaining_words, word2, word1]
print("Reordered words:", reordered_words)

datetime = ((5, 19, 2008), (10, 30, "am"))
# _ is a throw-away variable
(_, day, _), (hour, _, _) = datetime

word1, word2, word3, *word4 = words
print(word4)  # Always a list.
