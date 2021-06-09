import sqlite3

class DataUpdater():
    
    def __init__(self, entrances, exits, datetimeIn, datetimeOut, totalUp, totalDown, people_inside, company):
        self.entrances = entrances
        self.exits = exits,
        self.datetimeIn = datetimeIn
        self.datetimeOut = datetimeOut
        self.totalUp = totalUp
        self.totalDown = totalDown
        self.people_inside = people_inside
        self.company = company
        self.sqliteConnection = sqlite3.connect('/home/charles/Documents/FSDI_Final/Hive/db.sqlite3')
        self.cursor = self.sqliteConnection.cursor()


    def updateData(self):
        # Connect to Database
        
        # Update entrance times
        for date in self.entrances:
            try:
                sql_update_query = """insert into detection_movement(company, timeIn) values(?,?)"""
                self.cursor.execute(sql_update_query,(self.company, self.datetimeIn,))
                self.sqliteConnection.commit()

            except sqlite3.Error as error:
                print("Failed to update sqlite table", error)
                
                    
        # Update exit times
        for date in self.exits:
            try:
                sql_update_query = """insert into detection_movement(company, timeOut) values(?,?)"""
                self.cursor.execute(sql_update_query,(self.company, self.datetimeOut,))
                self.sqliteConnection.commit()

            except sqlite3.Error as error:
                print("Failed to update sqlite table", error)


        # Update Current Counts
        try:
            sql_update_query = """Update detection_company set entered = ?, exited = ?, current = ? where company = ?"""
            self.cursor.execute(sql_update_query,(self.totalDown,self.totalUp,self.people_inside[0],self.company))
            self.sqliteConnection.commit()
            print("--Database Updated--")

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            

        # Close Connection to Database
        finally:
            if self.sqliteConnection:
                self.sqliteConnection.close()