import os
import shutil
import datetime
import pyodbc
import time

# SERVER_NAME = 'localhost\SQLEXPRESS'
# DATABASE_NAME = 'DB'
BACKUP_DIRECTORY = 'D:/OneDrive/bck/'

DATABASE_NAME = "DATABASE NAME"
SERVER_NAME = "HOST"
DB_USERNAME = "USername"
DB_PASSWORD = "Password"


# Connect to the SQL Server instance
cnxn = pyodbc.connect(f"Driver={{SQL Server}};Server={SERVER_NAME};Database={DATABASE_NAME};UID={DB_USERNAME};PWD={DB_PASSWORD};")
# Create a cursor to execute SQL commands
cursor = cnxn.cursor()

while True:
    # Get the current date and time
    now = datetime.datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H-%M-%S')

    # Construct the backup file name
    backup_file_name = f'{DATABASE_NAME}_{date_str}_{time_str}.bck'

    # Construct the backup command
    
    backup_command = f'BACKUP DATABASE [{DATABASE_NAME}] TO DISK = N\'{BACKUP_DIRECTORY}{backup_file_name}\''
    print("Backup started successfull")

    # Execute the backup command
    # Set autocommit to True to disable transactions
    cnxn.autocommit = True
    # Execute the backup
    cursor = cnxn.cursor()
    cursor.execute(backup_command)
    print("Running backup command:",backup_command)
    cnxn.commit()
    print("Successfully created file:",backup_file_name)
    # Sleep for 2 hours
    time.sleep(7200)

    # Delete files older than 3 days
    for file_name in os.listdir(BACKUP_DIRECTORY):
        file_path = os.path.join(BACKUP_DIRECTORY, file_name)
        if os.stat(file_path).st_mtime < time.time() - 6 * 60 * 60:    
            print("Deleting files older than 6hrs...")        
            os.remove(file_path)
            print("Deleted file:",file_path)