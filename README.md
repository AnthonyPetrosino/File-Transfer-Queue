# File Transfer Queue
This is a Python app that automates manipulating files between local drives, network drives and SFTP-accessible servers. Made for internal use to improve team efficiency.

## To run:
There are two primary ways to run this application.

## 1. Interactive Terminal Mode
* This mode allows you to add, list, and manage file transfer tasks in real-time.
* Open your terminal, navigate to the cli directory within the project, and run the following command: python cli.py
* The application will start and display a > prompt, waiting for your commands.

## 2. Execution Mode
* This mode is designed to be run automatically by your operating system's task scheduler (like Windows Task Scheduler or cron). It executes all the tasks you have scheduled in the csv file.
* The command to execute all scheduled tasks is: python cli.py 1
* This can be done in your terminal or in your task scheduler.
* When the script is run with the argument 1, it processes each task in the csv file and then exits.
