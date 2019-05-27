"""responsible for generating reports from given data and loading file 
(contains main logic of the program)"""

import csv, time

class Album:
  def __init__(self, artist_name,album_name,release_year,genre,length ):
    #artist name,album name,release year,genre,length 
    self.artist_name = artist_name
    self.album_name = album_name
    self.release_year = release_year
    self.genre = genre
    self.length = length
  def print_album(self):
      print("Artist name => " + str(self.artist_name) + ", Album name => " + str(self.album_name)
       + ", Release year => " + str(self.release_year) + ", Genre => " + str(self.genre)
        + ", Length => " + str(self.length))

def album_init(file_name):
    album_list = []
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            album_list.append(Album(row[0],row[1],row[2],row[3],row[4]))
    return album_list
            


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
    """
    genre = "rock"
    stripped_albums = import_albums_from_file()
    single_album_list = want_to_view_all_imported_albums(stripped_albums)    
    music_data = import_albums_from_file()
    
    #want_to_view_all_imported_albums(music_data)
    want_to_find_all_albums_by_genre(single_album_list, genre)
    """
    album_list = album_init("albums.txt")
    #print("album_list: " + str(album_list))

    print("1) Genre = rock: ")

    for album in album_list:
        if album.genre == "rock":
            album.print_album()
    

    print("2)  Time range: ")
    time_format = "%M:%S"
    time_from = "100:00"
    time_to = "200:00"
    """
    for album in album_list:
        if time.strptime(time_from, time_format) >= time.strptime(album.length, time_format) and time.strptime(time_to, time_format) <= time.strptime(album.length, time_format) :
            album.print_album()
    """
    for album in album_list:
        
        if album.length >= time_from  and album.length <= time_to :
            album.print_album()

main()