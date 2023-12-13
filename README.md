# Edi File Verification


## Name
Stuck Files Finder Script

## Description
The Stuck Files Finder Script is a Python utility designed to identify files that have remained unchanged for at least 5 minutes in specified directories, excluding certain subdirectories. This script is particularly useful in environments where files are expected to be updated frequently, and any stagnation could indicate a processing or workflow issue.

## Feature
- File Age Checking: Determines if files in specific directories have not been modified in the last 5 minutes.
- Directory Specific Search: Allows users to specify which directories to scan.
- Exclusion of Subdirectories: Option to exclude certain subdirectories from the scan.
- Parallel Processing: Utilizes ThreadPoolExecutor for efficient scanning of files.
- File Status Check: Determines if files are "stuck" by checking if they have remained unchanged for at least 5 minutes.
- Directory Filtering: Scans specific directories while excluding certain subfolders to find stuck files.
- Multi-threading: Uses ThreadPoolExecutor to parallelize file checks, improving efficiency.
- Reporting: Creates an Excel report listing all stuck files, including client name and file path, and then sends an email notification.

## Modules used
- `os`: Interacts with the operating system to retrieve file creation times.
- `time`: Provides time-related functions for time calculations.
- `concurrent.futures.ThreadPoolExecutor`: Executes calls asynchronously using a pool of threads.
- `python-decouple`: Manages configuration and environment variables.
- `pandas`: Utilized for creating dataframes and writing to Excel files.
- `Custom module sendMail`: Contains functions sending email notifications.

## Functions
- is_file_blocked(file_path, five_minute_ago): Checks if a file is older than 5 minutes and considers it "stuck" if true.
- find_blocked_file_in_specific_dirs(root_directory, specific_directories, excluded_subfolder): Searches for stuck files within given directories and creates an 
Excel report for the ETGECMPRD01 environment.
- find_blocked_file_in_specific_dirs_prod(root_directory_PROD, specific_directories, excluded_subfolder): Similar to the above function but tailored for the ECSPROD environment.

## Docker Install
**Clone Repository**
1. `git clone https://git.shipenergy.com/etg-integrations/edi-file-verification.git`

**Moved into commission-schedule-rate-update.git DIR**

2. `$ cd edi-file-verification`

**Build Docker Container**

3. `docker build -t edi-file-verification .`

**Setting up the cronjob**

4. `$ crontab -e`

The script will run every 5 minutes

5. Add `*/15 * * * *  /usr/bin/docker run -d edi-file-verification`

To run the docker container manually you can run the following command:
`docker run edi-file-verification`


## Usage
1. Ensure all required modules are installed.
2. Configure the root_directory, specific_directories, and excluded_subfolder variables as needed for your environment.
3. Run the script. If any stuck files are detected, it will print the count, details of each file, and generate an Excel report in the designated folder.
4. Email notifications will be sent using the configured send_mail functions.

## Requirements
Python 3.x
- pandas library
- python-decouple

Ensure that the SMTP server is configured properly for sending emails through the sendMail module.

