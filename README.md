README - Inbox Sender Extractor

This script allows you to extract the list of senders from your email inbox using IMAP protocol. It connects to an IMAP server, prompts you for your email credentials, and retrieves the sender information from your inbox. The script then saves the list of senders to a file.

Installation

Ensure that you have Python 3 installed on your system.
Install the required dependencies by running the following command:

@cmd : pip install imaplib colorama

Usage

Run the script by executing the following command:

@cmd :  python inbox_sender_extractor.py

The script will display a banner and prompt you to enter your email and password.

Enter your email address and password when prompted. If the email or password is incorrect, an error message will be displayed, and you will be prompted to re-enter the details.

The script will connect to the IMAP server and start processing your inbox.

During the processing, an animated progress indicator will be displayed to indicate that the script is working. The number of senders found will be shown dynamically.

Once the script has completed processing, it will prompt you to enter the name of the file to save the senders.

Enter the desired name for the file. The senders' list will be saved in the specified file.

The script will display the number of inbox senders found and the name of the file where the senders were saved.

Note: Make sure to enable IMAP access for your email account before using this script. The steps to enable IMAP access may vary depending on your email provider.
