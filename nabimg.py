# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 04:10:32 2018

Nab Images

Given HTML code, parse links with image extensions and download to directory

Also Exploring tkinter!

To Add:
    Progress Bar
    Clear Fields
    HTML Explorer
    Integration Into Browser OMG

@author: vince
"""
from tkinter import *
from tkinter import filedialog
import os
import urllib.request

#import urllib.request
#from urllib.parse import urlparse
#from bs4 import BeautifulSoup

class getjob():
    def __init__(self, links=None, savedir=None):
        self.links = []
        self.savedir = os.getcwd()
        self.set_title = 'Default'
        self.author = 'Uknown'
        #add other job info
        
    def __str__(self):
        return ''.join(['Save Directory: ', str(self.savedir), '\n', 'Number of Files: ', str(len(self.links)), '\n', 
                        'Author: ', self.author, '\n', 'Set: ', self.set_title])

def getlinks(raw_html):
    '''
    Takes raw html and returns image links and simple unordered list.
    
    input: string
    output: list
    '''
    image_formats = ['jpg', 'jpeg', 'png', 'gif']
    
    def checkformat(url):
        for imgtype in image_formats:
            if imgtype in url:
                return True
            return False
    
    linklist = []
    
    for group in raw_html.split(' '):
        if 'href' in group and checkformat(group) :
            img_url = group.split("'")[1]
            linklist.append(img_url)
        
#    print(linklist) #debug
    return linklist

def downloadimages(job):
#    print(job) #debug
    counter = 0
    for item in job.links:
        #Generate Unique Name
        ulen =len(item)
        itemname = job.author + '_' + job.set_title + '_' + str(counter) + item[ulen-4:ulen]
        savepath = job.savedir + "\\" + itemname
        
        #Retrieve Image
        urllib.request.urlretrieve(item,filename=savepath)
        
        counter += 1
#        print(itemname) #debug


def main():
    print('Hello.  Beginning')    
    
    #Self Callback Functions
    def start_callback():
        newjob.links = getlinks(raw_html.get())
        newjob.set_title = set_title.get()
        newjob.author = author.get()
        downloadimages(newjob)
    
    def browse_callback():
        newjob.savedir = filedialog.askdirectory()
        
    
    #Start Job Object
    newjob = getjob()
    
    #Build tkinter window
    mwindow = Tk()
    mwindow.title('Nab Images')
    
    #Start/Close/Browse Buttons
    startbutton = Button(mwindow, text='Start', width=25, command=start_callback)
    closebutton = Button(mwindow, text='Close', width=25, command=mwindow.destroy)
    browsebutton = Button(mwindow, text='Browse', width=25, command=browse_callback)
    
    startbutton.grid(row=3, column=0)
    closebutton.grid(row=3, column=1)
    browsebutton.grid(row=3, column=2)
    
    #Input Fields
    Label(mwindow, text='Model Name').grid(row=0)
    Label(mwindow, text='Set Title').grid(row=1)
    Label(mwindow, text='HTML').grid(row=2)
    
    author = Entry(mwindow)
    set_title = Entry(mwindow)
    raw_html = Entry(mwindow)
    
    author.grid(row=0, column=1)
    set_title.grid(row=1, column=1)
    raw_html.grid(row=2, column=1)


    mwindow.mainloop()


if __name__ == '__main__':
    main()