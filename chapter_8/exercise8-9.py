def make_album(artist_name, album_name, songs=None):
    album_dict = {'artist': artist_name.title(), 'album': album_name.title(),}
    if songs:
        album_dict['song_count'] = songs
    return album_dict

while True:
    print("\nEnter in the necessary info: ")

    artist = input("Artist name: ")
    album = input("Album name: ")
    number_of_songs = input("Number of songs: ")

    album_info = make_album(artist, album, number_of_songs)
    print(album_info)

    