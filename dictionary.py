import random

class Dictionary:
    """
    Handles word lookups and random word selection for word transformations.
    """
    def __init__(self, dict_file_name=""):
        """
        Initializes the dictionary by reading words from a file.
        self:  This is a reference to the current instance of the class or constructor.

        Args:
            dict_file_name (str): The name of the dictionary file.
            If no argument is provided for this parameter, the default value will be an empty string (""). 
        """
        self.file_name = dict_file_name
        self.word_dict = set()
        self.word_array = []
        
        if self.file_name:
            # 0pens a file in read mode ("r") and assigns the file object to dict_file. 
            # The with statement ensures file is automatically closed once the block inside is finished executing. 
            try:
                with open(self.file_name, "r") as dict_file: 
                    print(">>...")
                    print("Reading dictionary...")
                    for line in dict_file:              #  loops through each line in the file one by one
                        word = line.strip().lower()
                        #strip removes leading and trailing whitespace and lower turns characters to lowercase
                        self.word_dict.add(word) #adds word to dictionary
                        self.word_array.append(word) # add words to array
                print("Dictionary Initialized...")
                print("...<<")
            except FileNotFoundError as e:
                print(f"Error: Could not open file {self.file_name}")
                print(f"Error: {e}")

  
    def search_word(self, word):
        """
        Checks if a word exists in the dictionary.

        Args:
            word (str): The word to search for.

        Returns:
            bool: True if the word is found, False otherwise.
        """
        return word in self.word_dict

    def get_words(self, word_length):
        """
        Retrieves two random words of a specified length from the dictionary.

        Args:
            word_length (int): The length of words to retrieve.

        Returns:
            list: A list containing two words of the specified length, or an empty list if none are found.
        """
        words = [word for word in self.word_array if len(word) == word_length] #iterates over array to find words with desirable length
        if len(words) < 2:          #iif array has less than 2 words
            return []
        return random.sample(words, 2)

        # random.sample: This function is used to generate a random sample (subset) of unique elements from an iterable (like a list or a string).
        # pick only 2 random words.
