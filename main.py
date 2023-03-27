from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from tkinter import *
from tkinter import filedialog
from PIL import Image
from pytesseract import pytesseract

root = Tk()

# Create a canvas to display the selected images
canvas = Canvas(root, width=600, height=300)
canvas.pack()

# added
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# added
pytesseract.tesseract_cmd = path_to_tesseract


class Main_App(MDApp):
    def build(self):
        def browse_images():
            # Open a file dialog to select image files
            rep = 0
            money = 0
            filenames = filedialog.askopenfilenames(initialdir="/", title="Select files",
                                                    filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")))
            # Load and display each selected image on the canvas
            for i, filename in enumerate(filenames):
                if filename.endswith(".jpg") or filename.endswith(".png"):  # Check if file is an image
                    # Open the image
                    im = Image.open(filename)
                    text = pytesseract.image_to_string(im)
                    word = text.split()
                    if (len(word) <= 0):
                        continue
                    if ('Totalt:' in word):
                        num = word.index('Totalt:')
                    else:
                        num = -1
                    count = 0
                    for i in word:
                        for j in i:
                            if (j == '('):
                                count += 1
                    if (count % 2 == 0):
                        count //= 2
                    else:
                        count -= 1
                        count //= 2
                    if (num != -1):
                        money += float(word[num + 1]) * float(count)
                    else:
                        rep += 1

            print("the total money You have earned are", float(money * 0.036))
            print("The total number of Errors in the recognition are:",rep)
            print("It's Done ra Shirdi")
            #return MDLabel(text="It's Done ra Shirdi",halign = 'center')
            return MDLabel(text="It's Done ra Shirdi", halign='center')
            #exit()

        # Create a button to browse and select images
        button = Button(root, text="Select Images", command=browse_images)
        button.pack()

        # Start the main loop
        root.mainloop()


if __name__ == '__main__':
    Main_App().run()