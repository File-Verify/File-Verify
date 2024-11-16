import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib


def calculate_checksum(file_path, algorithm):
    """Calculate the checksum of the given file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except Exception as e:
        return f"Error: {e}"


def browse_file(entry):
    """Open file dialog and set the file path in the entry widget."""
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)


def verify_file():
    """Verify the file against the provided checksum."""
    file_path = file_entry.get()
    checksum_to_compare = checksum_entry.get()
    algorithm = algo_var.get()

    if not file_path or not checksum_to_compare:
        messagebox.showerror("Error", "Please provide both file path and checksum.")
        return

    computed_checksum = calculate_checksum(file_path, algorithm)

    if computed_checksum == checksum_to_compare:
        messagebox.showinfo("Result", "Checksum matches!")
    else:
        messagebox.showwarning("Result", "Checksum does not match!")


def compute_checksum():
    """Compute and display the checksum for the selected file."""
    file_path = file_entry.get()
    algorithm = algo_var.get()

    if not file_path:
        messagebox.showerror("Error", "Please select a file.")
        return

    computed_checksum = calculate_checksum(file_path, algorithm)
    checksum_entry.delete(0, tk.END)
    checksum_entry.insert(0, computed_checksum)


# Create the main window
root = tk.Tk()
root.title("File Verification Tool")
root.geometry("500x250")

# File selection
file_frame = tk.Frame(root)
file_frame.pack(pady=10, padx=10, fill="x")

tk.Label(file_frame, text="File:").pack(side="left")
file_entry = tk.Entry(file_frame, width=40)
file_entry.pack(side="left", padx=5, fill="x", expand=True)
tk.Button(file_frame, text="Browse", command=lambda: browse_file(file_entry)).pack(side="left")

# Algorithm selection
algo_frame = tk.Frame(root)
algo_frame.pack(pady=10, padx=10, fill="x")

tk.Label(algo_frame, text="Algorithm:").pack(side="left")
algo_var = tk.StringVar(value="md5")
algo_options = ["md5", "sha256"]
tk.OptionMenu(algo_frame, algo_var, *algo_options).pack(side="left")

# Checksum input
checksum_frame = tk.Frame(root)
checksum_frame.pack(pady=10, padx=10, fill="x")

tk.Label(checksum_frame, text="Checksum:").pack(side="left")
checksum_entry = tk.Entry(checksum_frame, width=40)
checksum_entry.pack(side="left", padx=5, fill="x", expand=True)

# Action buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Compute Checksum", command=compute_checksum).pack(side="left", padx=5)
tk.Button(button_frame, text="Verify File", command=verify_file).pack(side="left", padx=5)

# Start the GUI event loop
root.mainloop()
