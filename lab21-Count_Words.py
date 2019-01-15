# lab21-Count_Words.py
import string

count ={}
translator = str.maketrans('', '', string.punctuation)
with open("The_Adventures_of.txt", encoding='utf-8') as f:
    book_raw = f.read().lower()
    book = book_raw.translate(translator)
    book = book.split()
    for word in range(len(book)):
        if book[word] not in count:
            count[book[word]] = 1
        elif book[word] in count:
            count[book[word]] += 1
    top_ten = sorted(count, key=count.get, reverse=True)[:10]
    for i in top_ten:
        print(i + ": " + str(count[i]))
    
