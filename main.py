import tkinter as tk
from tkinter import ttk
from pyngrok import ngrok
import webbrowser

# Initialize API key with an empty string
api_key = ""

# Dictionary to store ngrok tunnels
tunnels = {}

def create_tunnel():
    selected_port = port_combobox.get()

    # Check for empty API key
    if not api_key:
        tk.messagebox.showerror("Error", "API key is empty. Please set an API key.")
        return

    try:
        selected_port = int(selected_port)
    except ValueError:
        tk.messagebox.showerror("Error", "Invalid port. Please select a valid port.")
        return

    # Use the user-provided API key
    ngrok.set_auth_token(api_key)

    try:
        tunnel = ngrok.connect(selected_port)
        tunnels[selected_port] = tunnel
    except:
        tk.messagebox.showerror("Error", "Invalid API key. Please select an API key.")

    list_active_tunnels()

def open_tunnel_in_browser():
    selected_item = tunnel_list.get(tk.ACTIVE)
    if selected_item:
        # Extract the tunnel URL from the selected list item
        tunnel_url = selected_item.split(": ")[1]

        # Open the tunnel URL in the default web browser
        webbrowser.open(tunnel_url)

def list_active_tunnels():
    tunnel_list.delete(0, tk.END)
    for local_port, tunnel in tunnels.items():
        tunnel_list.insert(tk.END, f"Port {local_port}: {tunnel.public_url}")

def exit_program():
    for tunnel in tunnels.values():
        ngrok.disconnect(tunnel.public_url)
    root.destroy()

def set_api_key():
    global api_key
    api_key = api_key_entry.get()
    api_key_entry.delete(0, tk.END)  # Clear the entry field

# Create the main window
root = tk.Tk()
root.title("ngrok Tunnel Manager")
root.geometry("500x500")
# Create GUI components
api_key_label = tk.Label(root, text="API Key:")
api_key_entry = tk.Entry(root)
api_key_button = tk.Button(root, text="Set API Key", command=set_api_key)
port_label = tk.Label(root, text="Select a port:")
port_combobox = ttk.Combobox(root, values=[
    "4020",  # Visual Studio (MSVSMON)
    "9229",  # Visual Studio Code (VSCode) - Node.js Debugging
    "9222",  # Visual Studio Code (VSCode) - Chrome Debugging
    "5678",  # Python - Python Debugging
    "5005",  # Java - Java Debugging
    "5000",  # C# .NET - .NET Core Debugging
    "4020",  # C# .NET - .NET Framework Debugging
    "9229",  # JavaScript/Node.js - Node.js Debugging
    "1234",  # Ruby - Ruby Debugging
    "9000",  # PHP - Xdebug
    "2375",  # Docker - Docker Remote API
    "27017",  # MongoDB - MongoDB Debugging
    "3306",  # MySQL - MySQL Debugging
    "5432",  # PostgreSQL - PostgreSQL Debugging
    "6379",  # Redis - Redis Debugging
    "9200",  # Elasticsearch - Elasticsearch Debugging
    "8000",  # Apache Tomcat - Tomcat Debugging
    "3000",  # Node.js (General) - Express.js Default
])
port_combobox.set("Custom")
create_button = tk.Button(root, text="Create ngrok tunnel", command=create_tunnel)
open_button = tk.Button(root, text="Open Tunnel in Browser", command=open_tunnel_in_browser)
tunnel_list = tk.Listbox(root)
exit_button = tk.Button(root, text="Exit", command=exit_program)

# Place GUI components on the window
api_key_label.pack(pady=10)
api_key_entry.pack()
api_key_button.pack()
port_label.pack(pady=10)
port_combobox.pack(pady=5)
create_button.pack(pady=10)
open_button.pack(pady=10)
tunnel_list.pack(padx=10, pady=5)
exit_button.pack(pady=10)

root.mainloop()

# Disconnect all ngrok tunnels before exiting
for tunnel in tunnels.values():
    ngrok.disconnect(tunnel.public_url)
