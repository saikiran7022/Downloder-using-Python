from tkinter import *
from tkinter import ttk
from  tkinter import  filedialog

import pytube.request
from pytube import  YouTube

folder_name=" "

def openLoc():
    global  folder_name
    folder_name = filedialog.askdirectory()
    if( len(folder_name)>1 ):
        locationError.config(text=folder_name,fg="green")

    else:
        locationError.config(text="incorrect path", fg="red")

def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntryvar.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True ).first()

        elif(choice==choices[1]):
            select = yt.streams.filter(progressive=True).last()

        elif(choice==choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste link again!!", fg="red")


        select.download(folder_name)
        ytdError.config(text="Download complete!!")









root = Tk()

root.title("YTD")
root.geometry("350x400")
root.columnconfigure(0,weight=1)


ytdlabel = Label(root, text="Enter the url",font=("jost",16))
ytdlabel.grid()


ytdEntryvar = StringVar()
ytdEntry=Entry(root, width=50,textvariable=ytdEntryvar)
ytdEntry.grid()


ytdError=Label(root,text="Error msg",fg="red",font=("jost,10"))
ytdError.grid()


SaveLabel = Label(root, text="Save the vedio", font=("jost",15,"bold"))
SaveLabel.grid()

saveEntry= Button(root, width=10,bg="red",fg="white",text="choose path",command=openLoc)
saveEntry.grid()

locationError = Label(root, text="Error msg path", fg="red",font=("jost", 10))
locationError.grid()


choices=["720p", "144p", "audio only"]
ytdchoices=ttk.Combobox(root, value=choices)
ytdchoices.grid()

downbtn=Button(root,text="Download",width=10,bg="red",fg="white", command=DownloadVideo )
downbtn.grid()

root.mainloop()
