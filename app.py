import os
import shutil
import tkinter as tk
import glob
from pathlib import Path


window = tk.Tk()
window.title('Organiser')
window.geometry("480x360")

#Label - Location
label1=tk.Label(text="please enter the location: ")
label1.pack()
#grid(column=0, row=1)		---- cannot use grid() with pack()

#Entry - Location
entry1=tk.Entry()
entry1.pack()
entry1=tk.StringVar()		#---- maybe we cannot use this with entry() variable
#grid(column=2, row=1)		---- cannot use grid() with pack()


#Function Submit
def Submit():
	Sorter(all=i1.get(),Docs=i2.get(),Images=i3.get(),Videos=i4.get(),WebPages=i9.get(),ArchiveFiles=i5.get(),AudioFiles=i6.get(),Setups=i7.get(), ShellScripts=i8.get(), XML=i10.get())

#for i in range(0 to 7)		---- tried using for loop, unable, try again
i1=tk.IntVar()
i2=tk.IntVar()
i3=tk.IntVar()
i4=tk.IntVar()
i5=tk.IntVar()
i6=tk.IntVar()
i7=tk.IntVar()
i8=tk.IntVar()
i9=tk.IntVar()
i10=tk.IntVar()
# Actual Organiser

DIRECTORIES = {
"WebPages":["html5", "html", "htm", "xhtml"],
"Images":["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg","heif", "psd"],
"Videos":["avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng", "qt", "mpg", "mpeg", "3gp", "mkv"],
"Documents":["txt", "in", "out","pdf","oxps", "epub", "pages", "docx", "doc", "fdf", "ods","odt", "pwi", "xsn", "xps", "dotx", "docm", "dox","rvg", "rtf", "rtfd", "wpd", "xls", "xlsx", "ppt","pptx"],
"ArchiveFiles":["a", "ar", "cpio", "iso", "tar", "gz", "rz", "7z","dmg", "rar", "xar", "zip"],
"AudioFiles":["aac", "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3",".msv", "ogg", "oga", "raw", "vox", "wav", "wma"],
"XML":["xml"],
"Setups":["exe"],
"ShellScripts":["sh"],
}

WebPages=["html5", "html", "htm", "xhtml"]
Images=["jpeg", "jpg", "tiff", "gif", "bmp", "png", "bpg", "svg","heif", "psd"]
Videos=["avi", "flv", "wmv", "mov", "mp4", "webm", "vob", "mng","qt", ".mpg", ".mpeg", ".3gp", ".mkv"]
Documents=["txt", "in", "out","pdf","oxps", "epub", "pages", "docx", "doc", "fdf", "ods","odt", "pwi", "xsn", "xps", "dotx", "docm", "dox","rvg", "rtf", "rtfd", "wpd", "xls", "xlsx", "ppt","pptx"]
ArchiveFiles=["a", "ar", "cpio", "iso", "tar", "gz", "rz", "7z","dmg", "rar", "xar", "zip"] 
AudioFiles=["aac", "aa", "aac", "dvf", "m4a", "m4b", "m4p", "mp3","msv", "ogg", "oga", "raw", "vox", "wav", "wma"]
# PLAINTEXT_LIST=[] 
# PYTHON_LIST=[".py"]
XML=["xml"]
Setups=["exe"]
ShellScripts=["sh"]


FILE_FORMATS = {file_format: directory 
                for directory, file_formats in DIRECTORIES.items() 
                for file_format in file_formats} 

os.getcwd() #os.getcwd() gets current working directory
path = str(input("Enter Path of the folder you want to organise: "))
files = glob.glob(path + '/*')

def Sorter(**kwargs):
	for file in files:
			if Path(file).is_dir():
				continue
			# print(file)
			file_extension = file.split(".")[-1].lower()
			if file_extension in FILE_FORMATS:
				to_move_path = Path(FILE_FORMATS[file_extension]) 
				if kwargs['all']==1:
					os.makedirs(to_move_path, exist_ok=True)
					shutil.move(file, to_move_path)
				if kwargs['Docs']==1:
					if file_extension in Documents:
						os.makedirs(to_move_path, exist_ok=True)
						shutil.move(file, to_move_path)
				if kwargs['Images']==1:
					if file_extension in Images:
						os.makedirs(to_move_path, exist_ok=True)
						shutil.move(file, to_move_path)
				if kwargs['Videos']==1:
					if file_extension in Videos:
						os.makedirs(to_move_path, exist_ok=True)
						shutil.move(file, to_move_path)
				if kwargs['WebPages']==1:
					if file_extension in WebPages:
						os.makedirs(to_move_path, exist_ok=True)
						shutil.move(file, to_move_path)
				if kwargs['ArchiveFiles']==1:
					if file_extension in ArchiveFiles:
						os.makedirs(to_move_path, exist_ok=True)
						shutil.move(file, to_move_path)
				if kwargs['AudioFiles']==1:
					if file_extension in AudioFiles:
						os.makedirs(to_move_path, exist_ok=True)
						shutil.move(file, to_move_path)
				if kwargs['XML']==1:
					if file_extension in XML:
						os.makedirs(to_move_path, exist_ok=True)
						shutil.move(file, to_move_path)
				if kwargs['Setups']==1:
					if file_extension in Setups:
						os.makedirs(to_move_path, exist_ok=True)
						shutil.move(file, to_move_path)
				if kwargs['ShellScripts']==1:
					if file_extension in ShellScripts:
						os.makedirs(to_move_path, exist_ok=True)
						shutil.move(file, to_move_path)
		
#Check_Box1
c1=tk.Checkbutton(window, text="All", variable=i1)
c1.pack()
c2=tk.Checkbutton(window, text="Documents", variable=i2)
c2.pack()
c3=tk.Checkbutton(window, text="Images", variable=i3)
c3.pack()
c4=tk.Checkbutton(window, text="Videos", variable=i4)
c4.pack()
c5=tk.Checkbutton(window, text="Archives", variable=i5)
c5.pack()
c6=tk.Checkbutton(window, text="Audio", variable=i6)
c6.pack()
c7=tk.Checkbutton(window, text="Exe", variable=i7)
c7.pack()
c8=tk.Checkbutton(window, text="ShellScripts", variable=i7)
c8.pack()
c9=tk.Checkbutton(window, text="WebPages", variable=i7)
c9.pack()
c10=tk.Checkbutton(window, text="WebPages", variable=i7)
c10.pack()


#Button
b1=tk.Button(window, text="Submit", command=Submit)
b1.pack()


window.mainloop()