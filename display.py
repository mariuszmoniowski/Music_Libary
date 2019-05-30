"""esponsible for printing data on screen"""

def print_list_with_lp(list_to_print):
    for index in range(len(list_to_print)):
        print("{}. {}".format(index+1, list_to_print[index]))
