favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Loop through values
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():
    print(f"\t{language.title()}")

# Loop through values, and show only the unique items
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f"\t{language.title()}")
