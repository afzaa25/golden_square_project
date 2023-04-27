class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title 
        self.contents = contents
        

    def format(self):
        return f"{self.title}: {self.contents}"
    

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return int(self.count_words() / wpm)

    def reading_chunk(self, wpm, minutes):
        #calculate number of words to read
        words_to_read = int(wpm * minutes)
        words_read = 0

        #check if there are more words to read
        if words_to_read <= len(self.contents):
            chunk = self.contents[:words_to_read]
            words_read = words_to_read
        else:
            chunk = self.contents
            words_read = len(self.contents)

        #update the contents and return the chunk
        self.contents = self.contents[words_read:]
        if not self.contents:
            self.contents = ""
        return chunk