from stats import get_book_text,counting_words,counting_character,sort_character,sort_character,sort_list
import sys
if len(sys.argv) != 2 :
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
   
    text = get_book_text(sys.argv[1])
    num_words = counting_words(text)
    result_counting = counting_character(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    for item in sort_list(result_counting):
        if item["char"].isalpha():
            print(f"{item["char"]}: {item['num']}")

main()
