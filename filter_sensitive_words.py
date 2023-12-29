import random
import string
import sys
sys.path.append('./filter_vars')

from filter_vars import words_to_replace, original_string

output_vars = []

def search_and_replace_random_letter(input_string, words_to_replace):

    modified_string = input_string

    for word in words_to_replace:
        if len(word) >= 2 and word in modified_string:
            # Choose a random uppercase letter from the word
            letters = string.ascii_uppercase
            replacement_letter = ''.join(random.sample(letters, 2))

            # Replace the word with the chosen letter
            modified_string = modified_string.replace(word, replacement_letter) 
            output_vars.append((replacement_letter, word))

    return modified_string

result = search_and_replace_random_letter(original_string, words_to_replace)
print(output_vars)
print(result)

