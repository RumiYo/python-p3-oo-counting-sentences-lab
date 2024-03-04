#!/usr/bin/env python3

class MyString:

    def __init__(self, value=""):
        if value != "" and isinstance(value, str):
            self.value = value
        else:
            print("The value must be a string.")
            self.value = None

    def is_sentence(self):
      return self.value[-1] == "."

    
    def is_question(self):
        return self.value[-1] == "?"
    
    def is_exclamation(self):
        return self.value[-1] == "!"
    
    def count_sentences(self):
      value  = self.value
      if value != None:
        value = value.replace("!", ".")
        value = value.replace("?", ".")
        sentence_list = value.split(".")
        filtered_sentence_list = [item for item in sentence_list if item != ""]
        number = len(filtered_sentence_list)
        return number
      else: 
        return 0

