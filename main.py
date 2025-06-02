import sys
from stats import *

top = len(sys.argv)
if top != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    booook = sys.argv[1]

#path = "books/frankenstein.txt"
#def get_book_text(path):
    #with open(path) as f:
       #book_content = f.read()
        #return(book_content)

#def main():
    #path = "books/frankenstein.txt"
    #book_text = get_book_text(path)
    #print(book_text)

#main()

def word_count():
    i = 0
    book_text = get_book_text(booook)
    splitted_text = book_text.split()
    for word in splitted_text:
        i += 1
        final_result = f"Found {i} total words"
    print(final_result)
    return (final_result)

print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
word_count()
print("--------- Character Count -------")
#print(word_count())

text = get_book_text(booook)
symbols = count_characters(text)
sortyed = sort_function(symbols)
for item in sortyed:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")


print("============= END ===============")