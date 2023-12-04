import PyPDF2
import pyttsx3
import logging
from tqdm import tqdm
import time



logging.basicConfig(filename='app.log', filemode='w', level=logging.WARNING, format='%(name)s - %(levelname)s - %(message)s')

def write_to_file(file_name, data):
    """
    Writes data to a file.

    Parameters:
    file_name (str): The name of the file to write to.
    data (str): The data to write to the file.

    Returns:
    None
    """
    try:
        with open(file_name, 'a') as f:
            f.write(data)
    except IOError as e:
        logging.error(f"An error occurred while writing to the file {file_name}: {str(e)}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")

def main():
    file_name = input("Enter the name of the PDF file: ")
    try:
        book = open(file_name, 'rb')
    except FileNotFoundError:
        logging.error(f"The file {file_name} does not exist.")
        return
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return

    start_page = input("Enter the start page: ")
    end_page = input("Enter the end page: ")
    if not start_page.isdigit() or not end_page.isdigit() or int(start_page) > int(end_page):
        logging.error("Invalid page range.")
        return

    start_page = int(start_page)
    end_page = int(end_page)
    pdfReader = PyPDF2.PdfReader(book)
    speaker = get_speaker()
    if speaker is None:
        return
    read_pages(pdfReader, start_page, end_page, speaker)

def get_pdf_file(file_name):
    try:
        return open(file_name, 'rb')
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
        return None

def get_pdf_reader(file):
    return PyPDF2.PdfReader(file)

def get_speaker():
    try:
        speaker = pyttsx3.init()
        voices = speaker.getProperty('voices')
        for i, voice in enumerate(voices):
            print(f"{i}. {voice.name}")
        voice_selection = int(input("Select a voice: "))
        speaker.setProperty('voice', voices[voice_selection].id)
        
        current_volume = speaker.getProperty('volume')
        print(f"Current volume is {current_volume}")
        new_volume = float(input("Set the volume (0.0 - 1.0): "))
        speaker.setProperty('volume', new_volume)
        
        return speaker
    except Exception as e:
        logging.error(f"An error occurred while initializing the text-to-speech engine: {str(e)}")
        return None
    
# the read_pages function to add pause/resume and speed control functionality

def read_pages(pdfReader, start_page, end_page, speaker):
    bookmarks = []
    total_pages = end_page - start_page
    with tqdm(total=total_pages) as pbar:
        for num in range(start_page, end_page):
            try:
                page = pdfReader.pages[num]
                text = page.extract_text()
                speaker.say(text)
                speaker.runAndWait()
                pbar.update(1)
                time.sleep(0.1)  # to allow the progress bar to update
                command = input("Enter 'b' to bookmark this page or 'n' to go to the next page: ")
                if command == 'b':
                    bookmarks.append(num)
            except IndexError:
                logging.error(f"The page {num} does not exist in the PDF.")
            except Exception as e:
                logging.error(f"An error occurred while reading page {num}: {str(e)}")
    return bookmarks

# handle exceptions when writing to a file in Python
def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as f:
            f.write(data)
    except IOError:
        print(f"An error occurred while writing to the file {file_name}.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

write_to_file('test.txt', 'Hello! ')


# handle exceptions when closing a file in Python
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except IOError:
        print(f"An error occurred while reading from the file {file_name}.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# handle exceptions when reading a file line by line in Python using a try/except block. 
def read_file_line_by_line(file_name):
    try:
        with open(file_name, 'r') as f:
            for line in f:
                print(line, end='')
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except IOError:
        print(f"An error occurred while reading the file {file_name}.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

read_file_line_by_line('test.txt')



if __name__ == "__main__":
    main()

# the get_speaker function gets the current rate, prints it, and then prompts the user to set a new rate. The new rate is then set for the speech engine.

def get_speaker():
    try:
        speaker = pyttsx3.init()
        voices = speaker.getProperty('voices')
        for i, voice in enumerate(voices):
            print(f"{i}. {voice.name}")
        voice_selection = int(input("Select a voice: "))
        speaker.setProperty('voice', voices[voice_selection].id)
        
        current_volume = speaker.getProperty('volume')
        print(f"Current volume is {current_volume}")
        new_volume = float(input("Set the volume (0.0 - 1.0): "))
        speaker.setProperty('volume', new_volume)
        
        current_rate = speaker.getProperty('rate')
        print(f"Current rate is {current_rate}")
        new_rate = int(input("Set the rate: "))
        speaker.setProperty('rate', new_rate)
        
        return speaker
    except Exception as e:
        logging.error(f"An error occurred while initializing the text-to-speech engine: {str(e)}")
        return None



# import PyPDF2
# import pyttsx3
# import fitz  # PyMuPDF
# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk
# import threading

# # Initialize the text-to-speech engine
# speaker = pyttsx3.init()
# speaker.setProperty('rate', 150)

# # Function to read and speak a page
# def read_page(page_num, pdf_file_path):
#     global speaker
#     with open('A New Beginningy.pdf', 'rb') as book:
#         pdf_reader = PyPDF2.PdfReader(book)
#         if page_num < len(pdf_reader.pages):
#             page = pdf_reader.pages[page_num]
#             text = page.extract_text() if page.extract_text() else "No text on this page."
#             speaker.say(text)
#             speaker.runAndWait()

# # # Function to update the PDF display
# # def update_display(page_num, pdf_file_path):
# #     document = fitz.open(pdf_file_path)
# #     if page_num < len(document):
# #         page = document.load_page(page_num)
# #         pix = page.get_pixmap()
# #         img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
# #         img_resized = img.resize((canvas.winfo_width(), canvas.winfo_height()), Image.Resampling.LANCZOS)
# #         photo = ImageTk.PhotoImage(image=img_resized)
# #         canvas.create_image(0, 0, image=photo, anchor='nw')
# #         canvas.image = photo  # keep a reference!
# #         document.close()

# # # Function to handle the reading and updating in a separate thread
# # def handle_reading(page_num, pdf_file_path):
# #     update_display(page_num, pdf_file_path)
# #     read_page(page_num, pdf_file_path)

# # # Function to browse and open a new PDF file
# # def open_file():
# #     global current_page, pdf_file_path
# #     file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
# #     if file_path:
# #         pdf_file_path = file_path
# #         current_page = 0
# #         update_display(current_page, pdf_file_path)

# # # Function to start reading the PDF
# # def start_reading():
# #     thread = threading.Thread(target=handle_reading, args=(current_page, pdf_file_path))
# #     thread.start()

# # # Set up the GUI
# # root = tk.Tk()
# # root.title("PDF Viewer and Audiobook")

# # # Create a canvas to display the PDF pages
# # canvas = tk.Canvas(root, width=800, height=600)
# # canvas.pack(side=tk.LEFT)

# # # Create buttons for browsing file and starting reading
# # browse_button = tk.Button(root, text="Browse PDF", command=open_file)
# # browse_button.pack()
# # read_button = tk.Button(root, text="Start Reading", command=start_reading)
# # read_button.pack()

# # # Initialize the current page and the PDF file path
# # current_page = 0
# # pdf_file_path = 'A New Beginningy.pdf'  # Initialize with a default PDF path or empty string

# # root.mainloop()



