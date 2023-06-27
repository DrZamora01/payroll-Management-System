# payroll-Management-System

#  Python Program 6: Bootstrap

This program focuses on injecting proper styling and navigation to web apps while incorporating database querying. The main goal is to create a web application that allows users to view weekly pay calculations for employees filtered by department and update the hours worked for a given employee. The program utilizes a SQLite database named `payroll.db` that consists of two tables: `employees` and `pay_data`.

## Setup Instructions

To run the program locally on your system, follow the steps below:

1. Download the `payroll.zip` file from this [link](#).
2. Unzip the file to obtain the `payroll.db` database file.
3. Ensure you have Python installed on your machine.
4. Install the necessary dependencies by running the following command:
   ```
   pip install flask
   ```
5. Download the program files from the program repository.
6. Place the `payroll.db` file in the same directory as the program files.

## Running the Program

1. Open a terminal or command prompt.
2. Navigate to the directory containing the program files.
3. Execute the following command:
   ```
   python program6.py
   ```
4. The program will start running, and you should see output similar to the following:
   ```
    * Running on http://localhost:8080/ (Press CTRL+C to quit)
   ```
5. Open a web browser and enter the following URL:
   ```
   http://localhost:8080/
   ```
6. The application will open, and you can now navigate through the different functionalities using the provided links in the Bootstrap navigation bar.

## Program Features

1. Bootstrap Navigation Bar: The program includes a Bootstrap navigation bar with three working links: Home, View by Department, and Edit Employee Data.

2. Home Page: Clicking the Home link in the navigation bar will display a simple message indicating successful login.

3. View by Department: Clicking the View by Department link in the navigation bar will show a page containing all employees from a selected department and their corresponding weekly pay calculations.

4. Edit Employee Data: Clicking the Edit Employee Data link in the navigation bar will open a page where you can enter the employee ID and the updated hours worked for that employee. Submitting the form will update the hours worked in the database and notify the user of the successful operation.

Note: The program maintains the original database structure provided. Renaming any elements in the database may cause the program to fail.

## Troubleshooting



