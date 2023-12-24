from tkinter import*
from pytube import YouTube

root = Tk()
windowSizeX = '800'
windowSizeY= '500'
inputYPos = 60

link = StringVar()

def download():
        print("downloading video")
        url = YouTube(str(link.get()))
        vid = url.streams.get_highest_resolution()
        vid.download()
        Label(root, text="Downloaded Successfully", font="gotham-bold 12").place(x=round((int(windowSizeX)/2)), y=inputYPos+100, anchor="center")
 
 

icon = PhotoImage(file = "spped icon 1.png")

root.geometry(windowSizeX+'x'+windowSizeY)
root.iconphoto(False, icon)

root.resizable(0,0)
root.title("YT Downloader by Ali Almaamouri")


Label(root, text="Downloading Youtube Videos have never been so easy", font="gotham-bold 14").pack()
Label(root, text="Enter Your Youtube Link here", font="gotham-bold 16").place(x=round((int(windowSizeX)/2)), y=inputYPos, anchor="center")

Entry(root, width=60,  textvariable=link).place(x=round((int(windowSizeX)/2)), y=inputYPos+20, anchor="center")
Button(root, text="Download Video", font="gotham-black 16",bg="lime", padx=2, command=download).place(x=round((int(windowSizeX)/2)), y=inputYPos+60, anchor="center")


root.mainloop()
