# The Problem
# James is a DJ at a local radio station. As it's getting to the top of the hour, he needs to find a song to play that will be short enough to fit in before the news block. He's got a database of songs that he'd like you to help him filter in order to do that.

# What To Do
# Create longestPossible(longest_possible in python and ruby) helper function that takes 1 integer argument which is a maximum length of a song in seconds.

# songs is an array of objects which are formatted as follows:

# {'artist': 'Artist', 'title': 'Title String', 'playback': '04:30'}
# You can expect playback value to be formatted exactly like above.

# Output should be a title of the longest song from the database that matches the criteria of not being longer than specified time. If there's no songs matching criteria in the database, return false.

def longest_possible(playback):
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    
    valid_songs = []
    for song in songs:
        duration_seconds = time_to_seconds(song['playback'])
        if duration_seconds <= playback:
            valid_songs.append({
                'title': song['title'],
                'duration': duration_seconds
            })
    
    if not valid_songs:
        return False
    
    longest_song = max(valid_songs, key=lambda x: x['duration'])
    return longest_song['title']