# Reading Time Function Design recipe

## 1.  Describe the Problem
> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the function signature
> Include the name of the function, its parameters, return value, and side effects.
def estime_of_readting_time():
    parameter:
    text - string representing the words needed to be read

    return:
    float: 

## 3. Create examples as Text


"""
given a text of 200 words it will return a reading time of 1

estimate_reading_time("...200...")
# => 1.0
given a text of 400 words it will return a reading of 2

estimate_reading_time("...400...")
# => 2.0

given a text of 300 words it will return a reading of 1.5

estimate_reading_time("...150...")
# => 1.5

given an empty list
it will raise an error

estimate_reading_time("")
#raises an error "cant't estiamte reading tiem for an empty test


