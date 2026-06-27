#Word Frequency Counter — Reads a passage, counts how often each word appears using a dictionary, displays top 5 most frequent words using sorted() + comprehensions.using Lists, tuples, dictionaries, sets, comprehensions in python
# Word Frequency Counter

# Input passage
passage = input("Enter a passage:\n")

# Convert to lowercase and split into words
words = passage.lower().split()

# Dictionary to store word frequencies
word_count = {}

# Count frequencies
for word in words:
    word = word.strip(".,!?;:'\"()[]{}")
    if word:
        word_count[word] = word_count.get(word, 0) + 1

# Sort dictionary by frequency (highest first)
sorted_words = sorted(
    word_count.items(),
    key=lambda item: item[1],
    reverse=True
)

# Top 5 frequent words
top_5 = sorted_words[:5]

print("\n--- Top 5 Most Frequent Words ---")
for word, count in top_5:
    print(f"{word}: {count}")

# List comprehension
word_list = [word for word in word_count.keys()]

# Set comprehension (unique words)
unique_words = {word for word in words}

# Tuple comprehension style
word_tuples = [(word, count) for word, count in top_5]

print("\nTotal Words:", len(words))
print("Unique Words:", len(unique_words))
print("Top 5 as Tuples:", word_tuples)
