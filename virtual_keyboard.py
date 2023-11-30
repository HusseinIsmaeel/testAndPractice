import tkinter as tk

def on_key_press(key, text_widget):
    text_widget.insert('end', key)

# Global variable to store the current language
current_language = 'English'

# Keyboard layouts for each language
keyboard_layouts = {
    'English': [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
    ],
    'Arabic': [
        ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'د'],
        ['ش', 'س', 'ي', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ك', 'ط'],
        ['ئ', 'ء', 'ؤ', 'ر', 'ى', 'ة', 'و', 'ز', 'ظ'],
        ['ذ', 'ِ', 'ُ', 'َ', 'ٌ', 'ٍ', 'ً', 'إ']
    ]
}

def on_key_press(key, text_widget):
    text_widget.insert('end', key)

def create_keyboard(root, layout, text_widget):
    for row in layout:
        frame = tk.Frame(root)
        frame.pack()
        for key in row:
            button = tk.Button(frame, text=key, command=lambda k=key: on_key_press(k, text_widget), 
                               width=4, bg='white', fg='black', font=('Helvetica', '16'), 
                               relief='flat', activebackground='gray')
            button.pack(side='left')

def switch_language(root, text_widget):
    global current_language
    # Switch the language
    current_language = 'Arabic' if current_language == 'English' else 'English'
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()
    # Create the new keyboard
    create_keyboard(root, keyboard_layouts[current_language], text_widget)
    # Create the switch language button
    switch_button = tk.Button(root, text="Switch Language", command=lambda: switch_language(root, text_widget))
    switch_button.pack()

def create_virtual_keyboard():
    global current_language
    # Create the main window
    root = tk.Tk()
    root.title("Virtual Keyboard")

    # Create a Text widget to display the pressed keys
    text_widget = tk.Text(root, height=2, width=30)
    text_widget.pack()

    # Create the initial keyboard
    create_keyboard(root, keyboard_layouts[current_language], text_widget)

    # Create the switch language button
    switch_button = tk.Button(root, text="Switch Language", command=lambda: switch_language(root, text_widget))
    switch_button.pack()

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    create_virtual_keyboard()










# import tkinter as tk


# def create_keyboard(root, layout, text_widget):
#     for row in layout:
#         frame = tk.Frame(root)
#         frame.pack()
#         for key in row:
#             button = tk.Button(frame, text=key, command=lambda k=key: on_key_press(k, text_widget), 
#                                width=4, bg='black', fg='white', font=('Helvetica', '16'), 
#                                relief='flat', activebackground='gray')
#             button.pack(side='left')

# # def create_keyboard(root, layout, text_widget):
# #     for row in layout:
# #         frame = tk.Frame(root)
# #         frame.pack()
# #         for key in row:
# #             button = tk.Button(frame, text=key, command=lambda k=key: on_key_press(k, text_widget), width=4)
# #             button.pack(side='left')

# def create_virtual_keyboard():
#     # Create the main window
#     root = tk.Tk()
#     root.title("Virtual Keyboard")

#     # Create a Text widget to display the pressed keys
#     text_widget = tk.Text(root, height=2, width=30)
#     text_widget.pack()

#     # Define the layout of the keyboard
#     keyboard_layout = [
#         ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
#         ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
#         ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
#         ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
#     ]

#     # Define the layout of the keyboard
#     keyboard_layout = [
#         ['ض', 'ص', 'ث', 'ق', 'ف', 'غ', 'ع', 'ه', 'خ', 'ح', 'ج', 'د'],
#         ['ش', 'س', 'ي', 'ب', 'ل', 'ا', 'ت', 'ن', 'م', 'ك', 'ط'],
#         ['ئ', 'ء', 'ؤ', 'ر', 'ى', 'ة', 'و', 'ز', 'ظ'],
#         ['ذ', 'ِ', 'ُ', 'َ', 'ٌ', 'ٍ', 'ً', 'إ']
#     ]

#     # Create buttons for each key
#     create_keyboard(root, keyboard_layout, text_widget)

#     # Start the GUI event loop
#     root.mainloop()

# if __name__ == "__main__":
#     create_virtual_keyboard()