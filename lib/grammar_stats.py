class GrammarStats:
    def __init__(self):
        # self.total_checked = 0
        self.good_count = 0

    def check(self, text):
        # Check if text starts with a capital letter and ends with a sentence-ending punctuation mark
        if text[0].isupper() and text[-1] in ['.', '!', '?']:
            self.good_count += 1
            return True
        else:
            return False

    # def percentage_good(self):
    #     # Calculate percentage of good texts out of total checked
    #     if self.total_checked == 0:
    #         return 0
    #     else:
    #         return int(self.good_count / self.total_checked * 100)