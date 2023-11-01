import tkinter as tk
import pyshorteners
import logging
import os
from tkinter import messagebox
import pyperclip  # Import pyperclip

# Configure the logging settings
log_file = 'shortened_urls.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# Create log file if it doesn't exist
if not os.path.isfile(log_file):
    open(log_file, 'w').close()

def shorten_url():
    original_url = url_entry.get().strip()
    if original_url:
        try:
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(original_url)
            short_url_label.config(text=f"Shortened URL: {short_url}")
            history_listbox.insert(0, short_url)
            pyperclip.copy(short_url)  # Copy shortened URL to clipboard using pyperclip
            # Log the shortened URL
            logging.info(f'Shortened: {original_url} -> {short_url}')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to shorten URL: {str(e)}")
            logging.error(f'Error occurred: {str(e)}')
    else:
        messagebox.showwarning("Warning", "Please enter a valid URL.")

root = tk.Tk()
root.title("URL Shortener")

label = tk.Label(root, text="Enter the URL:")
label.pack()

url_entry = tk.Entry(root, width=40)
url_entry.pack()

shorten_button = tk.Button(root, text="Shorten", command=shorten_url)
shorten_button.pack()

short_url_label = tk.Label(root, text="")
short_url_label.pack()

history_label = tk.Label(root, text="Shortened URLs History:")
history_label.pack()

history_listbox = tk.Listbox(root, width=40, height=10)
history_listbox.pack()

root.mainloop()
