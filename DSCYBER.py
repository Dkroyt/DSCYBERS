import requests
import uuid
import secrets
import tkinter as tk
from tkinter import messagebox

# Automatically generate client ID, client secret, and access token
client_id = str(uuid.uuid4())
client_secret = secrets.token_urlsafe(32)
access_token = secrets.token_urlsafe(32)

# Instagram API endpoint for reporting
report_endpoint = "https://graph.instagram.com/v13.0/{user_id}/reports"

def generate_random_user_id(prefix='user'):
    return f"{prefix}{uuid.uuid4()}"

# Function to report a user
def report_user(user_id):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "reason": "spam or scam",
        "report_type": "spam"
    }
    response = requests.post(report_endpoint.format(user_id=user_id), headers=headers, json=data)
    if response.status_code == 201:
        print(f"Successfully reported {user_id}")
    else:
        print(f"Error reporting {user_id}: {response.text}")

# Function to start reporting
def start_reporting():
    num_reports = int(entry.get())
    for _ in range(num_reports):
        user_id = generate_random_user_id()
        report_user(user_id)
    messagebox.showinfo("Reports", f"Successfully reported {num_reports} users.")

# Create the main window
root = tk.Tk()
root.title("DSCYBER Mass Reporter")

# Create and pack the label
label = tk.Label(root, text="Enter the number of reports:")
label.pack()

# Create and pack the entry
entry = tk.Entry(root)
entry.pack()

# Create and pack the start button
start_button = tk.Button(root, text="Start Reporting", command=start_reporting)
start_button.pack()

# Run the application
root.mainloop()