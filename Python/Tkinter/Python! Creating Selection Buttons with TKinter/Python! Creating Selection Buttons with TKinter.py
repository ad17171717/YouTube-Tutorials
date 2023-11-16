'''
Author: Adrian Dolinay

Description: The following script is an introduction to implementing Tkinter buttons.
The script creates three buttons: the first sends a message to a user interacting with
the Tkinter applicaton, the second allows the user to close the application and the 
third gives the user the option to change the background color of the application.
'''

import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Button
from PIL import Image, ImageTk 

'''
Functions
'''

def message():

    '''
    Function that displays a message to a user using Tkinter's messagebox module

    The function does not take any parameters, it is initialized with a Tkinter Button object

    Returns
    -------
    showinfo: Creates and displays an information message box with the specified title and message
    '''

    return messagebox.showinfo(title=None, message='Hello World!')




def background_color():

    '''
    Function that creates a user interface for a user to change the background color of the application

    The function does not take any parameters, it is initialized with a Tkinter Button object

    The function does not return any values, when the color_button object is selected the function
    prompts the user to change the background color for the application. If the color is not available
    the user it prompted to input another color or close out the selection
    '''

    #creating a function within a function to get a user's input
    def get_input():
        value=inputtxt.get("1.0","end-1c")
        
        #if the color the user inputs is not available they will be prompted to
        #input another color
        try:
            window.configure(background=value)
        except:
            messagebox.showinfo(title=None, message='Color not found, please retry')
    
    #creating a temporary frame to display a banner and receive
    #input from a user
    temp_window = tk.Tk()
    temp_window.title('Change the Application Background Color') 
    temp_window.geometry('500x100')

    #set temporary button to receive input
    inputtxt = tk.Text(temp_window, height = 1, width = 20)
    inputtxt.pack()
    temp_button = tk.Button(temp_window, text = 'Input Color',command=lambda:get_input())
    temp_button.pack()
    temp_close_button = tk.Button(temp_window, text = 'Close',command=lambda:temp_window.destroy())
    temp_close_button.pack()

    

if __name__ == "__main__":

    #set the dimmensions of your application by pixel size
    #3840 x 2160 pixel
    WIDTH,HEIGHT = 1920,1080

    #calling the Tk class, a top level widget that represents the main window
    #of an application
    window = tk.Tk()
    window.title('Button Tutorial')
    #we can specify two percent characters ( %% ) to format our string
    window.geometry('%sx%s' % (WIDTH, HEIGHT))
    window.configure(background='lightgrey')

    '''
    Buttons
    '''
    message_button = Button(window, text='Click for Message', command=lambda:message())
    #place your button within the application
    message_button.place(x=WIDTH/2, y=HEIGHT/2)

    #the close button will call the destroy method which will exit the application 
    close_button = Button(window, text='Close Program', command=lambda:window.destroy())
    #configure button to have a custom image
    img = Image.open('close_img.png')
    ph = ImageTk.PhotoImage(img)
    close_button.configure(image=ph)
    close_button.place(x=WIDTH/2, y=HEIGHT/3)

    color_button = Button(window, text='Change Background color', command=lambda:background_color())
    color_button.place(x=WIDTH/2, y=HEIGHT/4)


    #mainloop method displays the application and responds to user input until terminated
    window.mainloop()