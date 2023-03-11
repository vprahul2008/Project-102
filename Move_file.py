import os
import shutil

from_dir="C:/Users/M/Downloads"
to_dir="C:/Users/M/Desktop/download_files"

list_of_files=os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)

    if extension=='':
            continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif','.pdf',".pdf"]:
            path1=from_dir+'/'+file_name
            path2=to_dir+'/'+'Images'
            path3=to_dir+'/'+'Images'+'/'+file_name

            if os.path.exists(path2):
                print("Moving")
                shutil.move(path1,path3)

            else:
                os.makedirs(path2)
                print("Moving")
                shutil.move(path1,path3)