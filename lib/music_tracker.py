class MusicTracker():
    def __init__(self):
        self._music_entry = []

    def add(self, track):
        if track == '':
            raise Exception("You have not set a song.")
        else:
            self._music_entry.append(track)

    def music_list(self):
        return self._music_entry



