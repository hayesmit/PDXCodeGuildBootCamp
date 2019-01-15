# lab21-Count_Words.py
import string

pairs = {}
count = {}
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
    for p in range(len(book)-1):
        if book[p] + ", " + book[p + 1] not in pairs:
                pairs[book[p] + ", " + book[p + 1]] = 1
        elif book[p] + ", " + book[p + 1] in pairs:
            pairs[book[p] + ", " + book[p + 1]] += 1
    top_ten_pairs = sorted(pairs, key=pairs.get, reverse=True)[:10]
    for i in top_ten_pairs:
        print(i + ": " + str(pairs[i]))
