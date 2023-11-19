'''
Author: Adrian Dolinay

Description: The following script is a tutorial on uploading images to a Tkinter
canvas. The script builds out a single function which allows a user interfacing
with the Tkinter application to upload an image onto a Tkinter canvas.
'''

import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Button
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk, UnidentifiedImageError

'''
Function
'''

def upload_action():

    '''
    Function that prompts a user to upload an image to a Tkinter canvas

    The function does not take any parameters and does not return anything, 
    it is initialized with a Tkinter Button object
    '''

    try:
        #opens a message box for a user to select an image file
        #the path to that file is then stored in the "img_path" variable
        img_path = askopenfilename()
        im = Image.open(img_path)
        #retrieve the dimmensions of the image
        img_width, img_height = im.size
        #if the image is larger than the canvas it will be resized
        #and the aspect ratio will be kept the same
        if img_width > WIDTH or img_height > HEIGHT:
            #loop over the image width and height until it is approximately
            #the same size as the canvas
            while img_width > WIDTH or img_height > HEIGHT:
                img_width *= .99
                img_height *= .99
            im = im.resize((int(img_width),int(img_height)))
            messagebox.showinfo(title='Warning!', 
                                message='The uploaded image is larger than the canvas. It will be resized.')
        
        img = ImageTk.PhotoImage(im)
        canvas.img = img
        canvas.create_image(WIDTH/2, HEIGHT/2, image=img, anchor=tk.CENTER)

    except UnidentifiedImageError:
        messagebox.showinfo(title='Upload Error',
                            message='Image could not be read, please make sure the selected is an image file')

if __name__ == "__main__":

    #set the dimmensions of your application by pixel size
    WIDTH,HEIGHT = 1920,1080

    #calling the Tk class, a top level widget that represents the main window
    #of an application
    window = tk.Tk()
    window.title('Image to Canvas Tutorial')
    #we can specify two percent characters ( %% ) to format our string
    window.geometry('%sx%s' % (WIDTH, HEIGHT))
    window.configure(background='lightgrey')

    #create a canvas, the canvas class is used for placing widgets, drawing graphics
    #or setting images
    canvas = tk.Canvas(window, width = WIDTH, height = HEIGHT,bg='white')
    canvas.pack()

    '''
    Buttons
    '''

    btn = tk.Button(window, text='Upload Image', command=lambda:upload_action())
    btn.pack()


    #mainloop method displays the application and responds to user input until terminated
    window.mainloop()