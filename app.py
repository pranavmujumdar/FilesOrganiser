import os
import shutil

import os
import shutil
import tkinter

os.getcwd() #os.getcwd() gets current working directory
path = input("Enter Path of the folder you want to organise: ")
#scan directory for files
# os.scandir(path)
#all the lists of known extensions

HTML_LIST=[".html5", ".html", ".htm", ".xhtml"]
IMAGES_LIST=[".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",".heif", ".psd"]
VIDEOS_LIST=[".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",".qt", ".mpg", ".mpeg", ".3gp", ".mkv"]
DOCUMENTS_LIST=[".txt", ".in", ".out",".pdf",".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt","pptx"]
ARCHIVES_LIST=[".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",".dmg", ".rar", ".xar", ".zip"] 
AUDIO_LIST=[".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"]
# PLAINTEXT_LIST=[] 
PYTHON_LIST=[".py"]
XML_LIST=[".xml"]
EXE_LIST=[".exe"]
SHELL_LIST=[".sh"]

for entry in os.listdir(path):
	print(entry)
	for i in DOCUMENTS_LIST:
		# iterate through the lists to 
		if(entry.endswith(i)):
			# scan the folder for directory "Text"
			dest=path+'\\Text'
			# if exists, move
			os.makedirs(dest, exist_ok=True)
			# else Create folder and move
			# dest=path+'\\Text'
			shutil.move(entry, dest)
		
	# for i in IMAGES_LIST:
	# 	# iterate through the lists to 
	# 	if(entry.endswith(i)):
	# 		# scan the folder for directory "Text"
	# 		dest=path+'\\Images'
	# 		# if exists, move
	# 		os.makedirs(dest, exist_ok=True)
	# 		# else Create folder and move
	# 		shutil.move(entry, dest)

	# for i in VIDEOS_LIST:
	# 	# iterate through the lists to 
	# 	if(entry.endswith(i)):
	# 		# scan the folder for directory "Text"
	# 		dest=path+'\\Videos'
	# 		# if exists, move
	# 		os.makedirs(dest, exist_ok=True)
	# 		# else Create folder and move
	# 		# dest=path+'\\Text'
	# 		shutil.move(entry, dest)

	# for i in ARCHIVES_LIST:
	# 	# iterate through the lists to 
	# 	if(entry.endswith(i)):
	# 		# scan the folder for directory "Text"
	# 		dest=path+'\\Archives'
	# 		# if exists, move
	# 		os.makedirs(dest, exist_ok=True)
	# 		# else Create folder and move
	# 		# dest=path+'\\Text'
	# 		shutil.move(entry, dest)

	# for i in AUDIO_LIST:
	# 	# iterate through the lists to 
	# 	if(entry.endswith(i)):
	# 		# scan the folder for directory "Text"
	# 		dest=path+'\\Audios'
	# 		# if exists, move
	# 		os.makedirs(dest, exist_ok=True)
	# 		# else Create folder and move
	# 		# dest=path+'\\Text'
	# 		shutil.move(entry, dest)


# if certain files available move them 
# create folder if non-existant





