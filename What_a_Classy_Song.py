# Your job is to create a class called Song.
#
# A new Song will take two parameters, title and artist.
#
# mount_moose = Song('Mount Moose', 'The Snazzy Moose')
#
# mount_moose.title => 'Mount Moose'
# mount_moose.artist => 'The Snazzy Moose'
# You will also have to create an instance method named howMany() (or how_many()).
#
# The method takes an array of people who have listened to the song that day. The output should be how many new listeners the song gained on that day out of all listeners. Names should be treated in a case-insensitive manner, i.e. "John" is the same as "john".
#
# Example
# mount_moose = Song('Mount Moose', 'The Snazzy Moose')
#
# # day 1 (or test 1)
# mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn']) => 5
# # These are all new since they are the first listeners.
#
# # day 2
# mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']); => 2
# # Luke and Amanda are new, john already listened to it the previous day
# Also if the same person listened to it more than once a day it should only count them once.
#
# Example
# mount_moose = Song('Mount Moose', 'The Snazzy Moose')
#
# # day 1
# mount_moose.how_many(['John', 'joHN', 'carl']) => 2
# Good luck!

class Song:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist
        self.s = set()

    def how_many(self, l: list) -> int:
        c = 0
        for i in l:
            if i.lower() not in self.s:
                c += 1
                self.s.add(i.lower())
        return c