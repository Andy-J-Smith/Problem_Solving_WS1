# Write code that takes a string as input and returns the string reversed

from itertools import count
from turtle import title


def backward_text():
    result_word = ''
    input_word = input("Enter word that you wish to spell backwards: ")
    for index in range(len(input_word)-1,-1,-1):
        result_word += input_word[index]
    return result_word

result = backward_text()
print(result)

    

# Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one space.

def proper_case():
    proper_sentence = ''
    input_sentence = input("Enter the sentence a sentence: ")
    #Adding the first letter(zero index) to proper_sentence(capitalized)
    proper_sentence += input_sentence[0].upper()
    for word in range(1,len(input_sentence)):
        if input_sentence[word-1] == " ":
            proper_sentence += input_sentence[word].upper()
        else:
            proper_sentence += input_sentence[word]

        print(input_sentence[word])
    return proper_sentence

# result1 = proper_case()
# print(result1)

# my_word = "hello andy"
# #this returns each letter
# for i in my_word:
#     print(i)

# #range return an integer
# for number in range(0,10):
#     print(number)

# my_list = ["bears", "packer"]
# #prints "bears" "packers"
# for team in my_list:
#     print(team)

# for nfl in range(0,len(my_list)):
#     print(my_list[nfl])


# Compress a string of characters


def compress():
    index = 0
    compressed = ''
    input_comp = input("enter letters")
    len_str = len(input_comp)
    while index != len_str:
        count = 1
        while (index < len_str-1) and (input_comp[index] == input_comp[index+1]):
            count = count + 1
            index = index + 1
        if count == 1:
            compressed += str(input_comp[index])
        else: 
            compressed += str(input_comp[index]) + str(count)
        index = index + 1
    return compressed
  

print(compress())





