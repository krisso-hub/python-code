
favorite_language = {
    'john': ['python', 'ruby', 'go'],
    'janet': 'java',
    'johnson': ['javascrpt', 'nodejs', 'c#', 'php']
}

for name, languages in favorite_language.items():
    print(f"\n{name.title()}'s favourite laguages are: ")
    for language in languages:
        print(f"\t{language.title()}")