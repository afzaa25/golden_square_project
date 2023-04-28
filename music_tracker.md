# Music Tracker class Design Recipe

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

> As a user
> So that I can keep track of my music listening.
> I want to add tracks I’ve listened to and see a list of them


## 2. Design the class interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python

class MusicTracker():
    def __init__(self):
        ## initialise empty list for music entries
    
    def add(self, track):
        #Parameter
            #track: a string representing a track
        #Side effects:
            #appends the track to the music list
            #throws an error if nothing has been set
    pass

    def music_list(self):
        #return - 
            #returns a list of tracks
    pass


```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

# EXAMPLE

```python

"""
initially there are no songs
"""
music_tracker = MusicTracker()
music_tracker.music_list # => []


"""
Given an empty string
it raises an error
"""
music_tracker = MusicTracker()
music_tracker.add('')
#this is will raise an error with a message

"""
when a song is added
it will be reflected in the list of songs
"""
music_tracker = MusicTracker()
music_tracker.add('Calm Down by Rema')
music_tracker.music_list #=> ['Calm Down by Rema']

"""
when multiple songs are added
it will be reflected in the list of songs
"""
music_tracker = MusicTracker()
music_tracker.add('Calm Down by Rema')
music_tracker.add('Peru by Fireboy DML')
music_tracker.add('Unforgettable by French Montana, Swae Lee')
music_tracker.music_list #=> ['Calm Down by Rema', 'Peru by Fireboy DML', 'Unforgettable by French Montana, Swae Lee']
```

## 4. Implement the behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._