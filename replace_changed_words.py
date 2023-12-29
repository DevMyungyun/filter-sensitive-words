import random
import sys
sys.path.append('./replace_vars')

from replace_vars import original_string, word_mappings

def search_and_replace_multiple(input_string, word_mappings):

    modified_string = input_string

    for search_word, replace_word in word_mappings:
        modified_string = modified_string.replace(search_word, replace_word)

    return modified_string

result = search_and_replace_multiple(original_string, word_mappings)
print(result)

