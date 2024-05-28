import os
from tkinter import*
from tkinter import ttk
from tkinter.filedialog import asksaveasfile, askdirectory, asksaveasfilename
from pytube import YouTube

root = Tk()
windowSizeX = '800'
windowSizeY= '500'
inputYPos = 60

link = StringVar()

fileTypes = ['mp4', 'mp3' ]

defaultPath = "Downloads"
fileDir = ''

def download(fileType):
        print("downloading video")
        #dir = asksaveasfile()
        #print(dir)
        
        #print(fileDir)
        fileName = ''

        fileDir= asksaveasfilename(defaultextension='mp4', filetypes=[("video file", '.mp4')]) if fileType=='mp4' else  asksaveasfilename(defaultextension='mp3', filetypes=[("audio file", '.mp3')])

        pathLen = len(fileDir)
        choesntDir = False


        if fileDir:
                
                for i in range(pathLen-1, 0, -1):
                        print(i)
                        if fileDir[i] == '/':
                                fileName = fileDir[(i+1):]
                                fileDir = fileDir[:(i)]
                                choesntDir = True
                                #print(fileDir[:(i)])
                                #print(fileName)
                                break
        else:
                fileDir = defaultPath
                print("no path chosen")        

        try: 
                url = YouTube(str(link.get()))
                #vidTitle = url.title

                if fileType == 'mp4':
                        vid = url.streams.get_highest_resolution()
                        print(fileName)
                        if fileName != '' or choesntDir:
                                vid.download(output_path=fileDir, filename=fileName)
                        else:
                                print("no path")
                                vid.download(output_path=fileDir)
                        
                else:
                        #fName = f"{vidTitle} audio.mp3"
                        #print(fName)
                        vid = url.streams.filter(only_audio=True).first()
                        if fileName != '' or choesntDir:
                                vid.download(output_path=fileDir, filename=fileName)
                        else:
                                print("no path")
                                vid.download(output_path=fileDir)
                
                Label(root, text="Downloaded Successfully", font="gotham-bold 12").place(x=round((int(windowSizeX)/2)), y=inputYPos+140, anchor="center")
                choesntDir = False
                
        except KeyError:
                
                print("error downloading video")                
        




icon = PhotoImage(file = "spped icon 1.png")

root.geometry(windowSizeX+'x'+windowSizeY)
root.iconphoto(False, icon)

root.resizable(0,0)
root.title("YT Downloader by Ali Almaamouri")


Label(root, text="Downloading Youtube Videos have never been so easy", font="gotham-bold 14").pack()
Label(root, text="Enter Your Youtube Link here", font="gotham-bold 16").place(x=round((int(windowSizeX)/2)), y=inputYPos+30, anchor="center")


fileTypeOptions = ttk.Combobox(root, values = fileTypes)
fileTypeOptions.set('mp4')
fileTypeOptions.place(x=round((int(windowSizeX)/3)), y=inputYPos, anchor="center")


Entry(root, width=60,  textvariable=link).place(x=round((int(windowSizeX)/2)), y=inputYPos+60, anchor="center")
Button(root, text="Download Video", font="gotham-black 16",bg="lime", padx=2, command=lambda: download(fileTypeOptions.get())).place(x=round((int(windowSizeX)/2)), y=inputYPos+100, anchor="center")
#Button(root, text="Select Directory", font="gotham-black 12",bg="blue", padx=2, command= selectDir).place(x=round((int(windowSizeX)/1.25)), y=inputYPos+100, anchor="center")



root.mainloop()
