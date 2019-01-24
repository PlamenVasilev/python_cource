replacements = input().split()
text = input()

for repl in replacements:
    text = text.replace(repl, '*'*len(repl))

print(text)
