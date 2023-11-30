import tkinter as tk

def on_key_press(key):
    print(f"Key pressed: {key}")

def create_keyboard(root, layout):
    for row in layout:
        frame = tk.Frame(root)
        frame.pack()
        for key in row:
            button = tk.Button(frame, text=key, command=lambda k=key: on_key_press(k), width=4)
            button.pack(side='left')

def create_virtual_keyboard():
    # Create the main window
    root = tk.Tk()
    root.title("Virtual Keyboard")

    # Define the layout of the keyboard
    keyboard_layout = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
    ]

    # Create buttons for each key
    create_keyboard(root, keyboard_layout)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_virtual_keyboard()
