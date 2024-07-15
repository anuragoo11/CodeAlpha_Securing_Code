import tkinter as tk
import re
import hashlib

def validate_input(user_input):
    """Validate the user input to ensure it is alphanumeric."""
    if not re.match("^[a-zA-Z0-9_]*$", user_input):
        raise ValueError("Invalid input: Only alphanumeric characters and underscores are allowed")

def hash_input(user_input):
    """Hash the user input using SHA-256."""
    m = hashlib.sha256()
    m.update(user_input.encode('utf-8'))
    return m.hexdigest()

def submit_form():
    """Handle form submission."""
    user_input = entry.get()
    try:
        validate_input(user_input)
        hashed_input = hash_input(user_input)
        result_label.config(text=f"Hashed input: {hashed_input}")
    except ValueError as e:
        result_label.config(text=f"Error: {e}")

# Create the main application window
root = tk.Tk()
root.title("Secure Tkinter App")

# Create and pack the entry widget for user input
entry = tk.Entry(root)
entry.pack()

# Create and pack the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.pack()

# Create and pack the label to display results or errors
result_label = tk.Label(root, text="")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
