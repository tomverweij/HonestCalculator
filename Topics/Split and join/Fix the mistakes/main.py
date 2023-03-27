text = input()
words = text.split()
for word in words:
    for web_word in ['https://', 'http://', 'www.']:
        if word.lower().startswith(web_word):
            print(word)