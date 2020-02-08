import glob
import os
import shutil

imgDir = "img/"
xmlDir = "label/"
imgDirNew = "img_new/"
xmlDirNew = "label_new/"

curID = 0

# print(os.path.exists("label/_2020011619353286084.xml"))

for imgPath in glob.glob(imgDir+"*jpg"):
    onlyName = imgPath.replace("img/","").replace(".jpg","")
    xmlPath = xmlDir +onlyName+".xml"
    if(os.path.exists(xmlPath)):
        newName = "mask_"+str(curID)
        print(imgPath,imgDirNew+newName+".jpg")
        shutil.copyfile(imgPath,imgDirNew+newName+".jpg") 
        shutil.copyfile(xmlPath,xmlDirNew+newName+".xml") 
        curID = curID + 1
    # print(imgPath)