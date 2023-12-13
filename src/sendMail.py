from exchangelib import (
    IMPERSONATION,
    OAUTH2,
    Account,
    Configuration,
    HTMLBody,
    Identity,
    FileAttachment
)
from exchangelib import Message as OutlookMessage
from exchangelib import OAuth2Credentials, Version
from exchangelib.version import EXCHANGE_O365
from decouple import config
import os

def send_mail_ETGECMPRD01():
    # Configuring OAuth2 credentials for email operations
    credentials = OAuth2Credentials(
    client_id=config('CLIENT_ID'),
    client_secret=config('CLIENT_SECRET'),
    tenant_id=config('TENANT_ID'),
    identity=Identity(primary_smtp_address=config('EMAIL_USER')),)

    # Configuring the email account with OAuth2 credentials and Exchange settings
    configuration = Configuration(credentials=credentials,auth_type=OAUTH2,server=config('EMAIL_HOST'),version=Version(EXCHANGE_O365),)
    account = Account(primary_smtp_address=config('EMAIL_USER'),config=configuration,access_type=IMPERSONATION,autodiscover=False,)

    # HTML content for the email body, including both French and English sections
    corps_email = "<html><body><p>See attached file for the list of EDI files TMW didn’t send to ECS Liaison FTP. </p><p>These files are located on the ETG-ECM-PRD-01 server (10.10.3.25) in the C:\EDI\TP folder</p><p>The problem must be identified and solved as soon as possible.</p><p>You can use the Incidents Database to see if a potential solution is there.</p><p>If the problem persists or can’t be resolved quickly, make sure to warn the people in the EDI SUPPORT Teams conversation.</p>"
    
    
        # Create an email message with the OutlookMessage class, specifying account, subject, body, and recipients
    message = OutlookMessage(
            account=account,    # The email account to send from
            subject="URGENT | ACTION NEEDED | EDI FILE NOT SENT TO ECS LIAISON",  # The subject of the email
            body=HTMLBody(corps_email),     # The HTML body of the email
            to_recipients=[config("RECIPIENT")])    # The recipient(s) of the email
    
        # Check if the Excel file exists
    if os.path.isfile("src/ETGECMPRD01_excel/EDI Files.xlsx"):
        
            # Open the Excel file in binary read mode
        with open("src/ETGECMPRD01_excel/EDI Files.xlsx", 'rb') as f:
                file_content = f.read()
        
        # Create a file attachment with the content read from the file
        attachment= FileAttachment(name=os.path.basename("src/ETGECMPRD01_excel/EDI Files.xlsx"), content=file_content)
        
        # Attach the file to the message
        message.attach(attachment)
        
         # Send the email message with the attachment
        message.send()

def send_mail_ECSPROD():
        # Configuring OAuth2 credentials for email operations
    credentials = OAuth2Credentials(
    client_id=config('CLIENT_ID'),
    client_secret=config('CLIENT_SECRET'),
    tenant_id=config('TENANT_ID'),
    identity=Identity(primary_smtp_address=config('EMAIL_USER')),)

    # Configuring the email account with OAuth2 credentials and Exchange settings
    configuration = Configuration(credentials=credentials,auth_type=OAUTH2,server=config('EMAIL_HOST'),version=Version(EXCHANGE_O365),)
    account = Account(primary_smtp_address=config('EMAIL_USER'),config=configuration,access_type=IMPERSONATION,autodiscover=False,)

    # HTML content for the email body, including both French and English sections
    corps_email = "<html><body><p>See attached file for the list of EDI files ECS Liaison didn’t process.</p><p>These files are located on the ECS PROD server (10.1.1.11) in the C:\FTP folder.</p><p>The problem must be identified and solved as soon as possible.</p><p>You can use the Incidents Database to see if a potential solution is there.</p><p>If the problem persists or can’t be resolved quickly, make sure to warn the people in the EDI SUPPORT Teams conversation.</p>"
    
    
        # Create an email message with the OutlookMessage class, specifying account, subject, body, and recipients
    message = OutlookMessage(
            account=account,    # The email account to send from
            subject="URGENT | ACTION NEEDED | EDI FILE NOT PROCESSED BY ECS LIAISON",  # The subject of the email
            body=HTMLBody(corps_email),     # The HTML body of the email
            to_recipients=[config("RECIPIENT")])    # The recipient(s) of the email
    
        # Check if the Excel file exists
    if os.path.isfile("src/ECSPROD_excel/EDI Files.xlsx"):
        
            # Open the Excel file in binary read mode
        with open("src/ECSPROD_excel/EDI Files.xlsx", 'rb') as f:
                file_content = f.read()
        
        # Create a file attachment with the content read from the file
        attachment= FileAttachment(name=os.path.basename("src/ECSPROD_excel/EDI Files.xlsx"), content=file_content)
        
        # Attach the file to the message
        message.attach(attachment)
        
         # Send the email message with the attachment
        message.send()

def send_mail_ETGECMPRD01_cleo():
    # Configuring OAuth2 credentials for email operations
    credentials = OAuth2Credentials(
    client_id=config('CLIENT_ID'),
    client_secret=config('CLIENT_SECRET'),
    tenant_id=config('TENANT_ID'),
    identity=Identity(primary_smtp_address=config('EMAIL_USER')),)

    # Configuring the email account with OAuth2 credentials and Exchange settings
    configuration = Configuration(credentials=credentials,auth_type=OAUTH2,server=config('EMAIL_HOST'),version=Version(EXCHANGE_O365),)
    account = Account(primary_smtp_address=config('EMAIL_USER'),config=configuration,access_type=IMPERSONATION,autodiscover=False,)

    # HTML content for the email body, including both French and English sections
    corps_email = "<html><body><p>See attached file for the list of EDI files Cleo didn’t process. </p><p>These files are located on the ETG-ECM-PRD-01 server (10.10.3.25) in the C:\Cleo-EDI folder.</p><p>The problem must be identified and solved as soon as possible.</p><p>You can use the Incidents Database to see if a potential solution is there.</p><p>If the problem persists or can’t be resolved quickly, make sure to warn the people in the EDI SUPPORT Teams conversation.</p>"
    
    
        # Create an email message with the OutlookMessage class, specifying account, subject, body, and recipients
    message = OutlookMessage(
            account=account,    # The email account to send from
            subject="RE: URGENT | ACTION NEEDED | EDI FILE NOT PROCESSED BY CLEO",  # The subject of the email
            body=HTMLBody(corps_email),     # The HTML body of the email
            to_recipients=[config("RECIPIENT")])    # The recipient(s) of the email
    
        # Check if the Excel file exists
    if os.path.isfile("src/ETGECMPRD01_excel_cleo/EDI Files.xlsx"):
        
            # Open the Excel file in binary read mode
        with open("src/ETGECMPRD01_excel_cleo/EDI Files.xlsx", 'rb') as f:
                file_content = f.read()
        
        # Create a file attachment with the content read from the file
        attachment= FileAttachment(name=os.path.basename("src/ETGECMPRD01_excel_cleo/EDI Files.xlsx"), content=file_content)
        
        # Attach the file to the message
        message.attach(attachment)
        
         # Send the email message with the attachment
        message.send()