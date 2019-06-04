"""esponsible for printing data on screen"""

def print_list_with_lp(list_to_print):
    for index in range(len(list_to_print)):
        print("{}. {}".format(index+1, list_to_print[index]))
    print("0. Quit")

def tasks_select(print_list_with_lp, list_to_choose):
        print_list_with_lp(list_to_choose)
        choose = input("Choose an action to proceed: ")
        return choose

def quit_func(choose):
        if choose == "0":
                is_running = False
                print("\nSee you later.\n")
                return is_running
                
def print_empty_row():
        print("\n")


main_menu_list = ["I want to view all imported albums", 
"I want to find all albums by genre", 
"I want to find all albums from given time range", 
"I want to find shortest/longest album", 
"I want to find all albums created by given artist", 
"I want to find album by album name", 
"I want to get full report in form of set of given statistics"] 

given_statistics = ["longest album", "shortest album", "oldest album", "youngest album", "all albums count + additional info", "how many albums are given the genres"]

additionat_tasks = ["As a user I want to view all similar music genres albums when searching for particular album", 
"As a user I want to add new album", 
"As a user I want to edit already existing albums", 
"As a user I want to save all new albums to external file"]

genre_list = ["progressive rock", "pop", "rock", "hard rock", "ancient", "hip hop"]