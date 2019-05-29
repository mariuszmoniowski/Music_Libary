"""responsible for generating reports from given data and loading file 
(contains main logic of the program)"""

def import_albums_from_file(): #importuje z pliku i dziele go na podzielone albumy
    with open("albums.txt") as my_file:
        file_data = my_file.readlines()
        splited_albums = []
        for row in file_data:
            album_as_list = row.strip().split(',')
            splited_albums.append(album_as_list)
    return splited_albums

def want_to_view_all_imported_albums(splited_albums): #chce wydrukowac podzielone albumy
    for single_album_list in splited_albums:
        #print(single_album_list)
        return single_album_list

def pojedyncze_albumy(splited_albums): #sprawdzam czy da sie dodac album do nowej listy
    aaa = []
    for pojedynczy_album in splited_albums:
        aaa.append(pojedynczy_album)
    return aaa


    
def want_to_find_all_albums_by_genre(single_album_list, genre): #sprawdzam czy da sie 
    new_list = []
    for element in single_album_list:
        new_list.append(element)
    print(new_list)
#artist name,album name,release year,genre,length

def new_list_with_albums(splited_albums, genre): #sprawdzam czy da sie dodac do nowej listy po parametrze
    lista = []
    for album in splited_albums:
        if genre in album:
            lista.append(album)
        print(lista)
    return lista

def get_albums_based_on_genre(splited_albums, genre):
    return_list = []
    for album in splited_albums:
        if album[3] == genre:
            return_list.append(album)

    return return_list

def my_print(my_list):
    for album in my_list:
        print(album)

def main():
    genre = "rock"
    splited_albums = import_albums_from_file()
    #single_album_list = want_to_view_all_imported_albums(splited_albums)    
        
    my_print(splited_albums)


    genre_albums = get_albums_based_on_genre(splited_albums, genre)
    my_print(genre_albums)

    #want_to_view_all_imported_albums(splited_albums)
    #want_to_find_all_albums_by_genre(single_album_list, genre)
    #new_list_with_albums(splited_albums, genre)
    #print(pojedyncze_albumy)
    
main()