import sqlite3

def dataHandler(entrances, exits, datetimeIn, datetimeOut, totalUp, totalDown, people_inside, company):
    # Connect to Database
    sqliteConnection = sqlite3.connect('/home/charles/Documents/FSDI_Final/Hive/db.sqlite3')
    cursor = sqliteConnection.cursor()

    # Update entrance times
    for date in entrances:
        try:
            sql_update_query = """insert into detection_movement(company, timeIn) values(?,?)"""
            cursor.execute(sql_update_query,(company, datetimeIn,))
            sqliteConnection.commit()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)
            
                
    # Update exit times
    for date in exits:
        try:
            sql_update_query = """insert into detection_movement(company, timeOut) values(?,?)"""
            cursor.execute(sql_update_query,(company, datetimeOut,))
            sqliteConnection.commit()

        except sqlite3.Error as error:
            print("Failed to update sqlite table", error)


    # Update Current Counts
    try:
    	sql_update_query = """Update detection_company set entered = ?, exited = ?, current = ? where company = ?"""
    	cursor.execute(sql_update_query,(totalDown,totalUp,people_inside[0],company))
    	sqliteConnection.commit()

    except sqlite3.Error as error:
    	print("Failed to update sqlite table", error)
        

    # Close Connection to Database
    finally:
    	if sqliteConnection:
    		sqliteConnection.close()