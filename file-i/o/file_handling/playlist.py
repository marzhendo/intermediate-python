liked_songs = {
    'Close in the Distace': 'Jason Charles Miller',
    'Nina': '.Feast',
    'Judas': 'Lady Gaga',
    'Photograph': 'Ed Sheeran'
}

def write_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, "w") as file:
        file.write("Liked Songs:\n")
        for song, artist in liked_songs.items():
            file.write(f"{song} - {artist}\n")

def read_liked_songs_from_file(file_name):
    with open(file_name, "r") as file:
        print(file.read())

def append_liked_songs_to_file(liked_songs, file_name):
    with open(file_name, "a") as file:
        file.write("\n")
        for song, artist in liked_songs.items():
            file.write(f"{song} - {artist}\n")


write_liked_songs_to_file(liked_songs, "playlist.txt")