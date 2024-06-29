import pyttsx3 
import time
from plyer import notification
from datetime import datetime
import mysql.connector

# Establish connection to the database
con = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="admin",
    database="tcs"
)
print(con)
mycursor = con.cursor()

# Get the current date and month
today = datetime.today()
formatted_date = today.strftime("%d")
current_month = today.month

# Function to convert text to speech
def speak(audio):
    """Converts text to speech"""
    engine = pyttsx3.init()
    engine.say(audio)
    engine.runAndWait()

# Execute SQL query to fetch employee details with matching birthday
query = "SELECT name FROM employee_detail WHERE emp_dob_date = %s AND emp_dob_month = %s"
mycursor.execute(query, (formatted_date, current_month))
data = mycursor.fetchall()

# Check if any birthdays match
if mycursor.rowcount > 0:
    for row in data:
        name = row[0]
        print(f"Today is {name}'s birthday.")
        notification.notify(
            title="Birthday",
            message=f"Today is {name}'s birthday",
            timeout=10
        )
        speak(f"Today is {name}'s birthday")
else:
    print("Today is no one's birthday")

# Close the cursor and connection
mycursor.close()
con.close()
