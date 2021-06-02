
def launch_menu():

    # the company_list should really be dynamically made by reading the database.....
    # if so it would auto populate when creating a new company through the Django Admin page
    company_list = ["Yardbar","Kaws"]

    camera_list = ["ipcam", "webcam"]
    list_names = [company_list, camera_list]

    options_list = ["company", "camera"]
    option_selections = []

    list_name_counter = 0
    for option in options_list:
        print("\nPlease choose a", option, ":")
        selection_number_counter = 0
        
        for list in list_names:
            print('-----------------')
            for item in list_names[list_name_counter]:
                print("[",selection_number_counter,"]", item)
                selection_number_counter += 1
            print('-----------------')
            option_selections.append(list_names[list_name_counter][int(input("--> "))])
            list_name_counter += 1
            break

    print("\nLaunching", option_selections[0], option_selections[1],"\n")
    return option_selections