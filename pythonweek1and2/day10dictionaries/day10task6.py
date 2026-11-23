word = input("Enter a word: ").lower()

counts = {}

for char in word:
    counts[char] = counts.get(char, 0) + 1

print("\nCharacter frequencies:")

for char, quantity in counts.items():
    print(f"{char}: {quantity}")