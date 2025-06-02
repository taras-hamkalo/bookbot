

def get_book_text(path):
    with open(path) as f:
        book_content = f.read()
        return(book_content)





#def word_count():
#    i = 0
#    book_text = get_book_text(path)
#    splitted_text = book_text.split()
#    for word in splitted_text:
#        i += 1
#        final_result = f"{i} words found in the document"
#    print(final_result)
#    return (final_result)

def count_characters(book_content):
    count_characters1 = {}
    book_content_lower = book_content.lower()
    for i in book_content_lower:
        if i not in count_characters1:
            count_characters1[i]=1
        else:
            count_characters1[i] += 1
    return(count_characters1)    




def sort_on(single_dict):
    return single_dict["num"]

def sort_function(character_dict):
    list_of_dicts = []
    for char in character_dict:
        list_of_dicts.append({"char":char,"num":character_dict[char]})
    sorted_list = sorted(list_of_dicts, reverse=True, key=sort_on)
    return (sorted_list)

   

    
