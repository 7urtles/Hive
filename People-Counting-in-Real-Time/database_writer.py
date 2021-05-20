import sqlite3

def dataHandler(entrances, exits, datetimeIn, datetimeOut, totalUp, totalDown, x, company):
    # Every time someone new enters save the time
    for date in entrances:
        try:
            sqliteConnection = sqlite3.connect('/home/charles/Documents/FSDI_Final/Traffic_Monitor/db.sqlite3')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sql_update_query = """insert into detection_entrance(timeIn) values(?)"""
            cursor.execute(sql_update_query,(datetimeIn,))

            sqliteConnection.commit()
            print("Record Updated successfully ")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
                
    # Every time someone new exits save the time
    for date in exits:
        try:
            sqliteConnection = sqlite3.connect('/home/charles/Documents/FSDI_Final/Traffic_Monitor/db.sqlite3')
            cursor = sqliteConnection.cursor()
            print("Connected to SQLite")

            sql_update_query = """insert into detection_exit(timeOut) values(?)"""
            cursor.execute(sql_update_query,(datetimeOut,))

            sqliteConnection.commit()
            print("Record Updated successfully ")
            cursor.close()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("The SQLite connection is closed")
    try:
    	sqliteConnection = sqlite3.connect('/home/charles/Documents/FSDI_Final/Traffic_Monitor/db.sqlite3')
    	cursor = sqliteConnection.cursor()
    	print("Connected to SQLite")
    	sql_update_query = """Update detection_company set entered = ?, exited = ?, current = ? where company = ?"""
    	cursor.execute(sql_update_query,(totalDown,totalUp,x[0],company))

    	sqliteConnection.commit()
    	print("Record Updated successfully ")
    	cursor.close()

    except sqlite3.Error as error:
    	print("Failed to update sqlite table", error)
        
    finally:
    	if sqliteConnection:
    		sqliteConnection.close()
    		print("The SQLite connection is closed")