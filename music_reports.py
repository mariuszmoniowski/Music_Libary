from display import *

list_for_def = ["artist name", "album name", "release year", "genre", "length"]

def import_albums_from_file(): #importuje z pliku i dziele go na podzielone albumy
    with open("albums.txt") as my_file:
        file_data = my_file.readlines()
        splited_albums = []
        for row in file_data:
            album_as_list = row.strip().split(',')
            splited_albums.append(album_as_list)
    return splited_albums

def get_albums_based_on_genre(splited_albums, genre_list):
    splited_albums = import_albums_from_file()
    genre = genre_selektor(genre_list)
    return_list = []
    for kategory in splited_albums:
        if kategory[3] == genre[0]:
            return_list.append(kategory)
            print_list_with_lp(return_list)  # blad podczas wyswietlania, powiela wpisy !!
   

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

def define_which_element_from_list_to_use(list_to_choose_from): #decide wchih element of list to use
    print_list_with_lp(list_to_choose_from)
    choice_element = input("\n    Which position are you interested in? \n")
    choice = (int(choice_element)-1)
    return choice

def want_to_find_shortest_longest_album(splited_albums):
    #print_list_with_lp(list_for_def)
    #choice = define_which_element_from_list_to_use(splited_albums)
    time_list = []
    for element in splited_albums:
        time = element[4]
        time_sec = convert_lenght_into_sec(time)
        time_list.append(time_sec)
    choice2 = input("Want to see shortest or longest album? Press 's' for shortest or 'l' for longest ")
    if choice2 == "s":
        choice2 = min
    elif choice2 == "l":
        choice2 = max
    print(choice2(splited_albums))

def want_to_find_all_albums_created_by_given_artist(splited_albums, list_for_def):
    choice = input("Write an artist: ") #define_which_element_from_list_to_use(list_for_def)
    artist_list = []
    for element in splited_albums:
        #artist = element[choice]
        if choice not in artist_list:
            artist_list.append(artist)
    for artist in enumerate(artist_list,1):
        print(artist)
   # choice 

def main_function_selector(choose, print_list_with_lp):
        if choose == 1:
                print_list_with_lp(import_albums_from_file)


def main(): #runs program
    splited_albums = import_albums_from_file()
    is_running = True

    while is_running:
        choose = tasks_select(print_list_with_lp, main_menu_list)
        #quit_func(choose)      #zaczalem kombinowac z funkcja quit ale ze nie dziala to ja zakomentowałem
        if choose == "1":
            is_running = False
            print_list_with_lp(splited_albums)
            input("Press Enter to continue...")
            is_running = True
        if choose == "2":
            is_running = False
            get_albums_based_on_genre(splited_albums, genre_list)
            #print_list_with_lp(genre_list)
            #choose = input("\nChoose genre to find albums by genre: \n")
            input("Press Enter to continue...")
            is_running = True                
        if choose == "3":
            is_running = False
            want_to_find_all_albums_from_given_time_range(splited_albums, convert_lenght_into_sec)
            print_empty_row()
            input("Press Enter to continue...")
            is_running = True        
        if choose == "4":
            is_running = False
            want_to_find_shortest_longest_album(splited_albums)
            print_empty_row
            input("Press Enter to continue...")
            is_running = True        
        if choose == "5":
            is_running = False
            want_to_find_all_albums_created_by_given_artist(splited_albums, list_for_def)
            print_empty_row
            input("Press Enter to continue...")
            is_running = True
        if choose == "6":
            pass
        if choose == "7":
            pass
        if choose == "0" or "q":
                is_running = False
                print("\nSee you later.\n")
                return is_running        
        main_function_selector(choose, import_albums_from_file)
    



main()