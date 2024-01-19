def main():
  file_path = 'books/frankenstein.txt'

  with open(file_path) as f:
    file_contents = f.read()
    words = file_contents.split()
    letters = [*file_contents] 

    def get_word_count(word_lst):
      return len(word_lst)
    
    def get_letter_count(char_lst):
      char_dict = {}

      for i in range(len(char_lst)):
        if char_lst[i].isalpha():

          if char_lst[i].lower() not in char_dict:
            char_dict[char_lst[i].lower()] = 1
          else:
            char_dict[char_lst[i].lower()] += 1
      return char_dict

    def print_report(path, word_count, letter_count):
        print(f"**** Report Start on {path} ****")
        print(f"{word_count} words were found in the specified document.\n")

        sorted_letters = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
       
        for key, value in sorted_letters: 
          print(f"The character '{key}' was found {value} times")
          
    print_report(file_path, get_word_count(words), get_letter_count(letters))

if __name__ == '__main__':
  main()
