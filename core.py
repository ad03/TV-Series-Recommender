#######################################################################
#                  Simple GUI TV-Series recommender                   #
#                                                                     #
#  A python based simple GUI application to recommend TV-Series based #                                                               
#  on emotion chosen by user.                                         #
#                                                                     #
#  * GUI is made using Tkinter                                        #
#  * BeauifulSoup is used for parsing data pulled from IMDb websites  #
#  Author: Arnav Anand                                                #
#######################################################################


#Import Tkinter module for GUI design
#Tkinter module documentation:
#https://docs.python.org/2/library/tk.html
import Tkinter as tK
import tkMessageBox
from Tkinter import *

#Import Requests module for requesting data from web server
#Requests module documentation:
#http://docs.python-requests.org/en/master/
import requests as req

#Import system module for exit function
import sys

#Import BeautifulSoup for scrapping data from IMDb webstite
#BeautifulSoup Documentation:
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup as Soup

#Method to invoke when find button is pressed by user
#Choice represents the radio button selected by the user
def buttonPressed(choice):
    #URL to be downloaded on basis of user input
    if choice.get()==1:
        url = 'https://www.imdb.com/search/title?title_type=tv_series,tv_miniseries&genres=action,crime&adult=include'
    elif choice.get()==2:
        url = 'https://www.imdb.com/search/title?title_type=tv_series,tv_miniseries&genres=comedy,thriller&adult=include' 
    elif choice.get()==3:
        url = 'https://www.imdb.com/search/title?title_type=tv_series,tv_miniseries&genres=comedy,romance&adult=include'
    elif choice.get()==4:
        url = 'https://www.imdb.com/search/title?title_type=tv_series,tv_miniseries&genres=mystery,thriller&adult=include'
    elif choice.get()==5:
        url = 'https://www.imdb.com/search/title?title_type=tv_series&sort=year,desc'

    #Download page using requests module
    page = req.get(url)

    #Creating parse tree using BeautifulSoup
    soup = Soup(page.content, 'html.parser')

    #Finding the HTML tag which conatins list of titles to be displayed
    pageContent = soup.find(id= "pagecontent")
    
    #Finding all tags which contains TV Series titles. 
    items = pageContent.find_all(class_= "lister-item-header")
    
    #Keeps track of number of Titles to be displayed
    count = 0
    
    #Initially empty output string
    output = ''
    
    #Iterating through all found tags containing TV Series titles
    for i in items:
        #Extract TV Series title
        title = i.find('a').get_text()
        
        #Extract TV Series Date
        date = i.find(class_="lister-item-year text-muted unbold").get_text()
        
        #Appen Title and Date to Output string
        output += '\n'
        output += title
        output += ' '
        
        if choice.get()!=5:
            output += date
        count += 1

        #Displaying only 15 titles
        if count == 15:
            break

    #Creating Message Tkinter widget to display output
    msg = tK.Message(root,text=output,anchor=W,width=400)

    #Setting geometry of Mesage widget
    msg.grid(row=8,column=0,pady=8,columnspan=4)

#Method to invoke when exit button is pressed
def exit():
    sys.exit()

#The root window for GUI interface
root = tK.Tk();

#Title of the application
root.title('TV-Series recommender')


#A label widget diplaying welcome message
message = 'Hey there! how you feeling today'
label = tK.Label(root, text=message,font=("Helvetica", 16))


#Variable to indicate the selected radio button
v=tK.IntVar()

#Four radio button widgets 
radioButton1 = tK.Radiobutton(root,text='Happy',variable=v,value=1)
radioButton2 = tK.Radiobutton(root,text='Sad',variable=v,value=2)
radioButton3 = tK.Radiobutton(root,text='Angry',variable=v,value=3)
radioButton4 = tK.Radiobutton(root,text='Surprised',variable=v,value=4)
radioButton5 = tK.Radiobutton(root,text='Latest TV Series',variable=v,value=5)

#Two button widgets
findButton = tK.Button(root,text='Find',command=lambda:buttonPressed(v))
exitButton = tK.Button(root,text='Quit',command=exit)

#Defining geometry of every Tkinter widget
label.grid(row=1,columnspan=4,pady=15,padx=30)
radioButton1.grid(row=2,sticky=W,padx=20)
radioButton2.grid(row=3,sticky=W,padx=20)
radioButton3.grid(row=4,sticky=W,padx=20)
radioButton4.grid(row=5,sticky=W,padx=20)
radioButton5.grid(row=6,sticky=W,padx=20)
findButton.grid(row=7,column=0,columnspan=2,pady=15)
exitButton.grid(row=7,column=1,columnspan=2,pady=15)

#Displaying the root window
root.mainloop()