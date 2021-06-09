import sqlite3

class Setup():
    
    # Variable assignments from sqlite database
    def __init__(self):
        # Establish connection to database
        self.sqliteConnection = sqlite3.connect('/home/charles/Documents/FSDI_Final/Hive/db.sqlite3')
        self.cursor = self.sqliteConnection.cursor()

        # Save camera feed url to variable
        self.camera_feed = self.cursor.execute("SELECT camera_url FROM detection_company;").fetchall()

        # Save company names as list of tuples
        self.company_list = self.cursor.execute("SELECT company FROM detection_company;").fetchall()

        self.camera_list = [("ipcam",), ("webcam",),]
        self.names_list = [self.company_list, self.camera_list]

        self.options_list = ["company", "camera"]
        self.option_selections = []
        self.company_camera = 0

        self.names_list_counter = 0


    # Displays menu options from list of tuples, sends selections back to Run.py
    def create_menu(self):
        for option in self.options_list:
            print("\nPlease choose a {}:".format(option))
            self.selection_number_counter = 1
            
            for list in self.names_list:

                print('-----------------')
                for item in self.names_list[self.names_list_counter]:
                    print("[{}] {}".format(self.selection_number_counter, item[0]))
                    self.selection_number_counter += 1
                print('-----------------')

                self.user_choice = int(input("--> "))-1
                self.option_selections.append(self.names_list[self.names_list_counter][self.user_choice][0])
                if self.names_list_counter == 0:
                    self.company_camera = self.user_choice
                self.names_list_counter += 1
                break
            print("Company Camera: ",self.camera_feed[self.company_camera][0])

        # Add companys ipcamera url to options list
        self.option_selections.append(self.camera_feed[self.company_camera][0])

        print("\n[INFO] Starting {} {} stream.....\n".format(self.option_selections[0], self.option_selections[1], self.option_selections[2]))
        return self.option_selections