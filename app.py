import os
import shutil
import tkinter as tk
import glob
from pathlib import Path
from tkinter import filedialog

window = tk.Tk()
window.title('Organiser')
window.geometry("480x360")

# +++++ Title Label +++++

label1=tk.Label(text="Browse to the directory to organise")
label1.pack()


# ++++++ Browse Button Function ++++++

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    # print(filename)


# +++++ Browse Button GUI elements +++++

folder_path = tk.StringVar()
lbl1 = tk.Label(master=window,textvariable=folder_path)
lbl1.pack()
button2 = tk.Button(text="Browse", command=browse_button)
button2.pack()

# +++++ Quit or continue prompt ++++
def quit_prompt():
	if askquestion(title="Quit?", message="Files have been sorted! you wanna quit?") =='yes':
		window.quit()
		exit()

# Exception handling
def enter_folder_dir():
	showwarning(title="Error", message="Please Select a folder first")

# +++++ Submit Function that calls the organiser on press +++++

def Submit():
	try:
		Sorter(path=filename, all=i1.get(),Docs=i2.get(),Images=i3.get(),Videos=i4.get(),WebPages=i9.get(),ArchiveFiles=i5.get(),AudioFiles=i6.get(),Setups=i7.get(), ShellScripts=i8.get(), XML=i10.get())
		quit_prompt()
	except Exception as e:
		enter_folder_dir()


# +++++ Variables/Declaration for the File Organiser +++++

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


# +++++ Organiser Function +++++

def Sorter(**kwargs):
	for file in files:
			if Path(file).is_dir():
				continue
			# print(file)
			file_extension = file.split(".")[-1].lower()
			if file_extension in FILE_FORMATS:
				to_move_path = path +'/'+ FILE_FORMATS[file_extension]
				# print(to_move_path)
				dest = Path(to_move_path)
				# print(dest)
				if kwargs['all']==1:
					os.makedirs(dest, exist_ok=True)
					shutil.move(file, dest)
				if kwargs['Docs']==1:
					if file_extension in Documents:
						os.makedirs(dest, exist_ok=True)
						shutil.move(file, dest)
				if kwargs['Images']==1:
					if file_extension in Images:
						os.makedirs(dest, exist_ok=True)
						shutil.move(file, dest)
				if kwargs['Videos']==1:
					if file_extension in Videos:
						os.makedirs(dest, exist_ok=True)
						shutil.move(file, dest)
				if kwargs['WebPages']==1:
					if file_extension in WebPages:
						os.makedirs(dest, exist_ok=True)
						shutil.move(file, dest)
				if kwargs['ArchiveFiles']==1:
					if file_extension in ArchiveFiles:
						os.makedirs(dest, exist_ok=True)
						shutil.move(file, dest)
				if kwargs['AudioFiles']==1:
					if file_extension in AudioFiles:
						os.makedirs(dest, exist_ok=True)
						shutil.move(file, dest)
				if kwargs['XML']==1:
					if file_extension in XML:
						os.makedirs(dest, exist_ok=True)
						shutil.move(file, dest)
				if kwargs['Setups']==1:
					if file_extension in Setups:
						os.makedirs(dest, exist_ok=True)
						shutil.move(file, dest)
				if kwargs['ShellScripts']==1:
					if file_extension in ShellScripts:
						os.makedirs(dest, exist_ok=True)
						shutil.move(file, dest)


# +++++ Variable Declaration for storing Checkbox Values

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
		
# ++++++ Check_Boxes ++++++

c1=tk.Checkbutton(window, text="All", variable=i1)
c1.pack()
c1.select()
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
c8=tk.Checkbutton(window, text="ShellScripts", variable=i8)
c8.pack()
c9=tk.Checkbutton(window, text="WebPages", variable=i9)
c9.pack()
c10=tk.Checkbutton(window, text="WebPages", variable=i10)
c10.pack()


# +++++++Submit Button+++++++

SubmitButton=tk.Button(window, text="Submit", command=Submit)
SubmitButton.pack()

window.mainloop()