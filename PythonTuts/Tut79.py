# soldier Prettify the Folder

# path, dictionary file, format
# def soldier("C://", "arpan.txt", "jpg") 

import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as f:
        filelist = f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file, file.upper())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i +=1

soldier(r"C:\Users\Dell\Documents\Python, Flask & Django\PythonTuts\testing", r"C:\Users\Dell\Documents\Python, Flask & Django\PythonTuts\ext.txt", ".jpg" )
