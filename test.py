import tkinter as tk

# Function to handle button clicks

def button_click(button_text):    
    global selected_button    
    selected_button = button_text
    root.destroy() # Close the main window
    
# Create the main Tkinter window

root = tk.Tk()
root.title("Button Example")

# Create buttons

button_texts = ["Pressures A", "Pressures B", "Low Temperatures", "High Temperatures A", "High Temperatures B", "Engine Speed"]
buttons = []

for button_text in button_texts:    
    button = tk.Button(root, text=button_text, command=lambda text=button_text: button_click(text))    
    button.pack()    
    buttons.append(button)

selected_button = None 

# Run the main loop
root.mainloop()

if selected_button is not None:
    print("Selected button text:", selected_button)
else:
    print("No button selected")