def unique_word(file):
    unique = set()
    for line in file:
        words = line.split()
        unique.update(words)
    return unique