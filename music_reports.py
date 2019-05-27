"""responsible for generating reports from given data and loading file 
(contains main logic of the program)"""

def import_albums_from_file():
    with open("albums.txt") as file:
        all_imported_albums = file.readlines()
        stripped_albums = [element.strip().split(",") for element in all_imported_albums]
    return stripped_albums

def want_to_view_all_imported_albums(stripped_albums):
    for single_album_list in stripped_albums:
        print(single_album_list)
    return single_album_list
    
def want_to_find_all_albums_by_genre(single_album_list, genre):
    for category in single_album_list:
        if category == genre:
            print(single_album_list)


#artist name,album name,release year,genre,length

def main():
    genre = "rock"
    stripped_albums = import_albums_from_file()
    single_album_list = want_to_view_all_imported_albums(stripped_albums)    
    music_data = import_albums_from_file()
    
    #want_to_view_all_imported_albums(music_data)
    want_to_find_all_albums_by_genre(single_album_list, genre)
    


main()