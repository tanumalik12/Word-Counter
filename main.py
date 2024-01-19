def word_counter(text):    # This function takes a string as input and returns the number of words in the string. 
    if not text:
        return 0           # If the input is empty, return 0.
    words = text.split()   # split the text into words using whitespace as delimitter.
    num_words = len(words) # Count the number of words.
    return num_words
text = input("Enter a sentence or paragraph:") # Prompt the user to enter some text.
num_words = word_counter(text) # Count the number of words in the input. 
print("Number of words:", num_words) # Print the result