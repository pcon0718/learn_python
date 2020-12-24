favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# looping through a dictionary's key-value pairs
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is: {language.title()}")

print()

for name in favorite_languages.keys():
    print(name.title())

print()

# check if Erin is in the dictionary:
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll.\n")

# Loop through dictionary. If name in dictionary = name in list, then print out sentence.

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    # If name in dictionary = name in list, then print out sentence.
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")