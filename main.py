def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = count_characters(text)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    
    # Print only alphabetic characters with proper formatting
    for char in sorted(characters.keys()):
        if char.isalpha():
            print(f"The ''{char}'' character was found {characters[char]} times")
    
    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_characters(text):
    characters = {}
    for char in text:
        lowered = char.lower()
        # Count both letters and spaces
        if lowered.isalpha() or char == " ":
            if lowered not in characters:
                characters[lowered] = 1
            else:
                characters[lowered] += 1
    return characters

main()