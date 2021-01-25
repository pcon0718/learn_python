# Combined exercise 8-7 and 8-8
def make_album(artist_name, album_name, songs=None):
    album_info = {'artist': artist_name.title(), 'album': album_name.title(),}
    if songs:
        album_info['song_count'] = songs
    return album_info

album = make_album('u2', 'achtung baby')
print(album)

album = make_album('bon jovi', 'slippery when wet', songs=11)
print(album)
