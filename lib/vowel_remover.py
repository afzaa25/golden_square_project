class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0 #initializes counter to 0
        while i < len(self.text): #this starts a loop that runs as long i is less than length of text
            if self.text[i].lower() in self.vowels: #this checks if the text at index i when coverted lowercase  is in vowels
                self.text = self.text[:i] + self.text[i+1:]
            else: #if the character is a vowel, removes the vowel from self.text by concatenating the substring before and after the vowel at index i.
                i += 1 #ncrements the counter variable i by one to move on to the next character in self.text.
        return self.text # returns the modified string with all vowels removed.

example_str = VowelRemover("aeiou")
result_str = example_str.remove_vowels()
print(result_str)