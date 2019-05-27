"""responsible for generating reports from given data and loading file 
(contains main logic of the program)"""

def import_albums_from_file():
    with open("albums.txt") as file:
        all_imported_albums = file.readlines()
        stripped_albums = [element.strip().split(",") for element in all_imported_albums]
    return stripped_albums

def want_to_view_all_imported_albums(stripped_albums):
    for single_album in stripped_albums:
        print(single_album)
    
def want_to_find_all_albums_by_genre(music_data, genre):
    pass 


#artist name,album name,release year,genre,length

def main():
    music_data = import_albums_from_file()
    want_to_view_all_imported_albums(music_data)
    genre = "rock"
    
    want_to_find_all_albums_by_genre(music_data, genre)
    


main()