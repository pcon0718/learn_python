favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# looping through a dictionary's key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is: {language.title()}")

coders = ['phil', 'eric', 'nancy', 'sarah']

print()

for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Greetings {coder.title()}, you have already answered this question.")
    else:
        print(f"Greetings {coder.title()}, you should answer this question.")