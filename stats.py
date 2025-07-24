def get_book_text(path) :
   with open(path)  as f : 
    book_content = f.read()
    return book_content
def counting_words(book) :
   words_count = book.split()
   return len(words_count)
def counting_character(text):
      text =text.lower()
      dict_stored = {}
      for char in text :
         if char in dict_stored:
            dict_stored[char] += 1
         else :
            dict_stored[char] = 1
      return dict_stored
def sort_character(item_dict):
      return item_dict["num"]
def sort_list(alist):
   sorted_dict = []
   for key,value in alist.items() :
      new_dict = {"char": key, "num": value}
      sorted_dict.append(new_dict)
   sorted_dict.sort(reverse=True,key=sort_character)
   return sorted_dict

      
