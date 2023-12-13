import os  #provides functions for interacting with the operating system. It's used here to get file creation times.
import time #provides time-related functions. It's used for time calculations.
from concurrent.futures import ThreadPoolExecutor # ThreadPoolExecutor is used for creating a pool of threads to execute calls asynchronously
from decouple import config #  used for managing configuration (like environment variables) separate from your code
import pandas as pd
from sendMail import send_mail_ETGECMPRD01, send_mail_ECSPROD, send_mail_ETGECMPRD01_cleo


#Defines a function to determine if a file is "stuck" (unchanged for at least 5 minutes)
def is_file_blocked(file_path, five_minute_ago):
    try:
        #Retrieve the file's creation time.
        creation_time = os.path.getctime(file_path)
        #Returns True if the file is older than 5 minutes, else False, along with the file path.
        return creation_time <= five_minute_ago, file_path
    except OSError:
        # In case of an error accessing returns False and the file path.
        return False, file_path

# Defines a function to find "stuck" files in specific directories
def find_blocked_file_in_specific_dirs(root_directory, specific_directories, excluded_subfolder):
    data_to_excel = []
    current_time = time.time()
    # Calculates the time representing "5 minutes ago"
    five_minute_ago = current_time - 5 * 60 # convertir 5 minutes en secondes
    
    # Use ThreadPoolExecutor to parralelize the search.
    with ThreadPoolExecutor() as executor:
        futures = []
        #Recursively traverses the root directory
        for root, dirs, files in os.walk(root_directory):
            # In case when we want the search find the specific dir and similars
            #if not any(specific_dir in root for specific_dir in specific_directories):
                #continue
            
            # Checks if the current directory matches one of the specific directories
            if not os.path.basename(root) in specific_directories:
                continue
            #if  any(excluded_sub in root for excluded_sub in excluded_subfolder):
                #continue
                
            # Ignores the specified subdirectories
            if excluded_subfolder in root:
                continue
            
            # For each file in the directory, schedules a task to check if it's a stuck
            for file in files:
                file_path = os.path.join(root, file)
                futures.append(executor.submit(is_file_blocked, file_path, five_minute_ago))
        # Retrieves results from the future tasks
        results = [future.result() for future in futures]
        # Filters to get only the stuck files
        blocked_files = [res for res in results if res[0]]
        
    if len(blocked_files) > 0:
        print(f"Nombre de fichiers coincés : {len(blocked_files)}")
    
        for is_blocked, file_path in blocked_files:
            print(f"fichier coincé: {os.path.basename(file_path)} dans {file_path}")
            client = file_path.split(os.sep)
            data_to_excel.append([
                #client[6], # Get client name appeared in the file path. It can be changed when the file path is different.
                #file_path[32::],
                os.path.dirname(file_path)[20::],
                os.path.basename(file_path),   
                ])
        # create dataframe
        df = pd.DataFrame(data_to_excel, columns=['folder', 'File'])
    
        # Write the DataFrame to an Excel file without the index
        df.to_excel("src/ETGECMPRD01_excel/EDI Files.xlsx", index=False)
        send_mail_ETGECMPRD01()
    else:
        print("no stuck file(s)")

def find_blocked_file_in_specific_dirs_prod(root_directory_PROD, specific_directories, excluded_subfolder):
    data_to_excel = []
    current_time = time.time()
    # Calculates the time representing "5 minutes ago"
    five_minute_ago = current_time - 5 * 60 # convertir 5 minutes en secondes
    
    # Use ThreadPoolExecutor to parralelize the search.
    with ThreadPoolExecutor() as executor:
        futures = []
        #Recursively traverses the root directory
        for root, dirs, files in os.walk(root_directory_PROD):
            # In case when we want the search find the specific dir and similars
            #if not any(specific_dir in root for specific_dir in specific_directories):
                #continue
            
            # Checks if the current directory matches one of the specific directories
            if not os.path.basename(root) in specific_directories:
                continue
            #if  any(excluded_sub in root for excluded_sub in excluded_subfolder):
                #continue
                
            # Ignores the specified subdirectories
            if excluded_subfolder in root:
                continue
            
            # For each file in the directory, schedules a task to check if it's a stuck
            for file in files:
                file_path = os.path.join(root, file)
                futures.append(executor.submit(is_file_blocked, file_path, five_minute_ago))
        # Retrieves results from the future tasks
        results = [future.result() for future in futures]
        # Filters to get only the stuck files
        blocked_files = [res for res in results if res[0]]
        
    if len(blocked_files) > 0:
        print(f"Nombre de fichiers coincés : {len(blocked_files)}")
    
        for is_blocked, file_path in blocked_files:
            print(f"fichier coincé: {os.path.basename(file_path)} dans {file_path}")
            client = file_path.split(os.sep)
            data_to_excel.append([
                #client[5], # Get client name appeared in the file path. It can be changed when the file path is different.
                os.path.dirname(file_path)[17:], 
                os.path.basename(file_path),
                ])
        # create dataframe
        df = pd.DataFrame(data_to_excel, columns=['Folder','File'])
    
        # Write the DataFrame to an Excel file without the index
        df.to_excel("src/ECSPROD_excel/EDI Files.xlsx", index=False)
        send_mail_ECSPROD()
    else:
        print("no stuck file(s)")

def find_blocked_file_in_specific_dirs_cleo(root_directory_CLEO, specific_directories, excluded_subfolder):
    data_to_excel = []
    current_time = time.time()
    # Calculates the time representing "5 minutes ago"
    five_minute_ago = current_time - 5 * 60 # convertir 5 minutes en secondes
    
    # Use ThreadPoolExecutor to parralelize the search.
    with ThreadPoolExecutor() as executor:
        futures = []
        #Recursively traverses the root directory
        for root, dirs, files in os.walk(root_directory_CLEO):
            # In case when we want the search find the specific dir and similars
            #if not any(specific_dir in root for specific_dir in specific_directories):
                #continue
            
            # Checks if the current directory matches one of the specific directories
            if not os.path.basename(root) in specific_directories:
                continue
            #if  any(excluded_sub in root for excluded_sub in excluded_subfolder):
                #continue
                
            # Ignores the specified subdirectories
            if excluded_subfolder in root:
                continue
            
            # For each file in the directory, schedules a task to check if it's a stuck
            for file in files:
                file_path = os.path.join(root, file)
                futures.append(executor.submit(is_file_blocked, file_path, five_minute_ago))
        # Retrieves results from the future tasks
        results = [future.result() for future in futures]
        # Filters to get only the stuck files
        blocked_files = [res for res in results if res[0]]
        
    if len(blocked_files) > 0:
        print(f"Nombre de fichiers coincés : {len(blocked_files)}")
    
        for is_blocked, file_path in blocked_files:
            print(f"fichier coincé: {os.path.basename(file_path)} dans {file_path}")
            client = file_path.split(os.sep)
            data_to_excel.append([
                #client[5], # Get client name appeared in the file path. It can be changed when the file path is different.
                os.path.dirname(file_path)[20::], 
                os.path.basename(file_path),
                ])
        # create dataframe
        df = pd.DataFrame(data_to_excel, columns=['Folder','File'])
    
        # Write the DataFrame to an Excel file without the index
        df.to_excel("src/ETGECMPRD01_excel_cleo/EDI Files.xlsx", index=False)
        send_mail_ETGECMPRD01_cleo()
    else:
        print("no stuck file(s)")