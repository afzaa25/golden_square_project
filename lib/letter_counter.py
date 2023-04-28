class LetterCounter:
    def __init__(self, text):
        self.text = text

    def calculate_most_common(self):
        counter = {} # initialises an empty dictionary used to count the occurrences of each letter in self.text.
        most_common = None #used to store the most common letter in self.text.
        most_common_count = 1  #initializes a variable most_common_count to 1 that will be used to store the count of the most common letter in self.text.
        for char in self.text: #starts a loop that goes over every letter in the text
            if not char.isalpha(): #checks if the letter is not from the alphabet
                continue #if the character is not alphabetic, skips to the next iteration of the loop.
            counter[char] = counter.get(char, 1) + 1#increments the count of the character in counter by 1, or initializes it to 1 if it does not yet exist in counter.
            if counter[char] > most_common_count:#checks if the count of the character in counter is greater than the current most_common_count.
                most_common = char #if the count is greater than the current most_common_count, sets most_common to the current character.
                most_common_count = counter[char]#if the count is greater than the current most_common_count, sets most_common_count to the new count.
        return [most_common_count, most_common]# returns a list containing the count of the most common letter in self.text and the most common letter itself.


counter = LetterCounter("Digital Punk")
print(counter.calculate_most_common())