name = input()

def normalize(new_name):
    return (new_name.
            replace('é', 'e').
            replace('ë', 'e').
            replace('á', 'a').
            replace('å', 'aa').
            replace('œ', 'oe').
            replace('æ', 'ae'))

print(normalize(name))
