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

def get_albums_based_on_genre(splited_albums, genre):
    return_list = []
    for album in splited_albums:
        if album[3] == genre:
            return_list.append(album)
    return return_list

def want_to_find_all_albums_from_given_time_range(splited_albums, convert_lenght_into_sec): 
    #user_lenght = ask_for_time_range()
    from_time = convert_lenght_into_sec(input("Enter time range 'FROM' (mm:ss): "))
    to_time = convert_lenght_into_sec(input("Enter time range 'TO' (mm:ss): "))
    for element in splited_albums:
        time = element[4]
        album_lenght = convert_lenght_into_sec(time) 
        if album_lenght in range(from_time,to_time+1):
            print(element)

def convert_lenght_into_sec(time): #it takes any time in format mm:ss and convert it to seconds
    time_sec = time.split(':')
    time_sec = (int(time_sec[0]) * 60) + int(time_sec[1])
    return time_sec

def my_print(my_list): #it prints every element in lists
    for album in my_list:
        print(album)

def define_which_element_from_list_to_use(splited_albums): #decide wchih element of list to use
    choice_element = input("\n|1: artist name |2: album name |3: release year |4: genre |5: length |\n    Which element of album are you interested in? (1,2,3,4,5): ")
    choice = (int(choice_element)-1)
    return choice

def want_to_find_shortest_longest_album(splited_albums, convert_lenght_into_sec):
    choice = define_which_element_from_list_to_use(splited_albums)
    time_list = []
    for element in splited_albums:
        time = element[choice]
        time_sec = convert_lenght_into_sec(time)
        time_list.append(time_sec)
    choice2 = input("Want to see shortest or longest album? press 's' for shortest or 'l' for longest ")
    if choice2 == "s":
        choice2 = min
    elif choice2 == "l":
        choice2 = max
    print(choice2(splited_albums))








def main(): #runs program
    genre = "rock"
    splited_albums = import_albums_from_file()
    #single_album_list = want_to_view_all_imported_albums(splited_albums)    
        
    #my_print(splited_albums)


    #genre_albums = get_albums_based_on_genre(splited_albums, genre)
    #my_print(genre_albums)
    #want_to_view_all_imported_albums(splited_albums)
    #want_to_find_all_albums_by_genre(single_album_list, genre)
    #new_list_with_albums(splited_albums, genre)
    #print(pojedyncze_albumy)
    #want_to_find_all_albums_from_given_time_range(splited_albums, convert_lenght_into_sec)
    #define_which_element_from_list_to_use(splited_albums)
    want_to_find_shortest_longest_album(splited_albums, convert_lenght_into_sec)


main()