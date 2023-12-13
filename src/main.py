from Find_stuck_file import is_file_blocked, find_blocked_file_in_specific_dirs, find_blocked_file_in_specific_dirs_prod, find_blocked_file_in_specific_dirs_cleo #The script imports several functions from a custom module Find_stuck_file. These functions (is_file_blocked, find_blocked_file_in_specific_dirs, find_blocked_file_in_specific_dirs_prod, and find_blocked_file_in_specific_dirs_cleo) are likely designed to identify files that are blocked or stuck in different environments or directory structures.
from decouple import config #imports the config function from the decouple library, which is used to manage configuration and environment variables in a clean and organized way.
import requests #imports the requests library, a popular choice for making HTTP requests in Python.
import logging #imports Python’s built-in logging module, allowing the script to log messages for debugging or informational purposes.
import time #provides time-related functions. It's used for time calculations.

""""
The script uses the config function to retrieve configuration values such as specific_directories, excluded_subfolder, and various root_directory paths for different environments (standard, production, and a custom environment named CLEO). These values are likely specified in environment variables or a .env file.
"""

if __name__ == "__main__": 
    specific_directories = config('specific_directories')
    excluded_subfolder = config('excluded_subfolder')
    root_directory = config('PATH_FOLDER')
    root_directory_PROD = config('PATH_FOLDER_PROD')
    root_directory_CLEO = config('PATH_FOLDER_CLEO')
    
    find_blocked_file_in_specific_dirs(root_directory, specific_directories, excluded_subfolder)
    find_blocked_file_in_specific_dirs_prod(root_directory_PROD, specific_directories, excluded_subfolder)
    find_blocked_file_in_specific_dirs_cleo(root_directory_CLEO, specific_directories, excluded_subfolder)
    """
    The health check request is wrapped in a try-except block to catch any exceptions like          connection errors, timeouts, etc.
    If an exception occurs (requests.RequestException), the script logs a debug message with the    details of the exception. This helps in understanding why the health check might have failed.
    """
    try:
        requests.get(
        'https://health.shipenergy.com/ping/578a6943-a0e2-40e1-82ca-459ef28f02b5',
        timeout=10
                 )
    except requests.RequestException as e:
        logging.debug("Failed to ping %s" % e)
