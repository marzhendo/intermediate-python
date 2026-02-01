import functools
# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), 
            ('Just Like That', 5.05), 
            ('Song 3', 6.55), 
            ('Leave The Door Open', 4.02), 
            ('I Can\'t Breath', 4.47), 
            ('Bad Guy', 3.14)]

def longer_than_five_minutes(song):
    """Returns True if the song duration is longer than 5 minutes."""
    return song[1] > 5.0

# Filter songs longer than 5 minutes
long_songs = list(filter(longer_than_five_minutes, playlist))
print(long_songs)  

def minutes_to_seconds(song):
    """Converts song duration from minutes to seconds."""
    # duration = song[1]
    # minutes = int(duration)
    # seconds = (duration - minutes) * 100
    # total_seconds = minutes * 60 + round(seconds)
    return song[1] * 60
# Convert song durations to seconds
song_durations_in_seconds = list(map(minutes_to_seconds, long_songs))
print(song_durations_in_seconds)

def add_durations(total, current):
    """Adds two song durations."""
    return total + current

# Calculate total duration of durations in seconds
total_duration = functools.reduce(add_durations, song_durations_in_seconds)
print(total_duration)  # Output: Total duration in seconds of songs longer than 5 minutes

# Comprehension ver

final_song_durations = sum(song[1] * 60 for song in playlist if song[1] > 5.0)
print(final_song_durations)  # Output: Total duration in seconds of songs longer than 5 minutes using list comprehension
