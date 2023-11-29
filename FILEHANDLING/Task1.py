import os
import shutil
source_path=input("Enter a source path: ")
destination_path=input("Enter a destination path: ")

folder_contents = os.listdir(source_path)

for i in range(len(folder_contents)):
    
    temp=os.listdir(folder_path=source_path+"\\"+folder_contents[i])
    
    for j in range(len(temp)):
        data=source_path+"\\"+folder_contents[i]+"\\"+temp[j]
        
        if os.path.exists(destination_path):
            shutil.copy(data,destination_path)
            
        else:
            os.mkdir(destination_path)
            shutil.copy(data,destination_path)

