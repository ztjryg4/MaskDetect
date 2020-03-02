import glob
import os
import shutil
import xml.etree.ElementTree as et
import data_log

def img_cmp():
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

def modify_text():
    xmldir = "label_nomask/"

    log = data_log.start("modifylog")
    
    for xmlpath in glob.glob(xmldir+"*xml"):
        tree = et.parse(xmlpath)
        root = tree.getroot()
        all_obj = root.findall('object')
        for curobj in all_obj:
            name = curobj.find("name")
            if name.text == "have_mask":
                name.text = "havemask"
                print(xmlpath)
            elif name.text == "no_mask":
                name.text = "nomask"
                print(xmlpath)
            else:
                data_log.add(xmlpath,log)
        tree.write(xmlpath)

def modify_tag():
    xmldir = "label_nomask/"

    log = data_log.start("modifylog")
    
    for xmlpath in glob.glob(xmldir+"*xml"):
        tree = et.parse(xmlpath)
        root = tree.getroot()
        all_obj = root.findall('object')
        for curobj in all_obj:
            name = curobj.find("Difficult")
            name.tag = 'difficult'
        tree.write(xmlpath)

def check():
    log = data_log.start("checklog")
    checklist = ["have_mask","no_mask"]
    for xmlpath in glob.glob(xmldir+"*xml"):
        for checkword in checklist:
            checkfile = open(xmlpath,"r")
            if checkword in checkfile.read():
                data_log.add(xmlpath,log)

def sample_statistics():
    xmldir = "label/"

    log = data_log.start("samplelog")
    havemask_face_cnt = 0
    nomask_face_cnt = 0

    havemask_img_cnt = 0
    nomask_img_cnt = 0
    mix_img_cnt = 0

    for xmlpath in glob.glob(xmldir+"*xml"):
        cur_havemask_cnt = 0
        cur_nomask_cnt = 0
        tree = et.parse(xmlpath)
        root = tree.getroot()
        all_obj = root.findall('object')
        for curobj in all_obj:
            name = curobj.find("name")
            if name.text == "havemask":
                havemask_face_cnt = havemask_face_cnt + 1
                cur_havemask_cnt = cur_havemask_cnt + 1
                print(xmlpath)
            elif name.text == "nomask":
                nomask_face_cnt = nomask_face_cnt + 1
                cur_nomask_cnt = cur_nomask_cnt + 1
                print(xmlpath)
            else:
                data_log.add(xmlpath,log)
        if cur_havemask_cnt == 0 and cur_nomask_cnt != 0:
            nomask_img_cnt = nomask_img_cnt + 1
        elif cur_havemask_cnt != 0 and cur_nomask_cnt == 0:
            havemask_img_cnt = havemask_img_cnt + 1
        elif cur_havemask_cnt != 0 and cur_nomask_cnt != 0:
            mix_img_cnt = mix_img_cnt + 1
        else:
            data_log.add(xmlpath,log)

    print("havemask_face: ", havemask_face_cnt)
    print("nomask_face: ", nomask_face_cnt)

    print("havemask_img: ", havemask_img_cnt)
    print("nomask_img: ", nomask_img_cnt)
    print("mix_img: ", mix_img_cnt)
    
sample_statistics()