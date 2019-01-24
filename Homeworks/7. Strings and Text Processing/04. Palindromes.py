word_list = input().split()
palindromes = []

for word in word_list:
    if word == word[::-1]:
        if word not in palindromes:
            palindromes.append(word)

print(", ".join(sorted(palindromes, key=str.lower)))

