import wget
import zipfile
import os
import json
import shutil

def init_preprocessing(annotations_coco_url, val_coco_url, train_coco_url):
    wget.download(annotations_coco_url, out='annotations.zip')
    wget.download(val_coco_url, out='val.zip')
    wget.download(train_coco_url, out='train.zip')

    with zipfile.ZipFile("annotations.zip", "r") as zip_ref:
        zip_ref.extractall("preprocessing") 
    with zipfile.ZipFile("val.zip", "r") as zip_ref:
        zip_ref.extractall("preprocessing")
    with zipfile.ZipFile("train.zip", "r") as zip_ref:
        zip_ref.extractall("preprocessing")

    os.remove("annotations.zip")
    os.remove("val.zip")
    os.remove("train.zip")

def put_data(instance_annotation, root_folder_name, image_dir, split_data_name):
    # create root folder
    if not os.path.exists(root_folder_name):
        os.mkdir(root_folder_name)
    with open(instance_annotation, "r") as f:
        data = json.load(f)

        # create folder structure
        if not os.path.exists(f"./{root_folder_name}/{split_data_name}"):
            os.mkdir(f"./{root_folder_name}/{split_data_name}")
            for category in data["categories"]:
                os.mkdir(f"./{root_folder_name}/{split_data_name}/{category['name']}")
                os.mkdir(f"./{root_folder_name}/{split_data_name}/{category['name']}/labels")
                os.mkdir(f"./{root_folder_name}/{split_data_name}/{category['name']}/images")
    
        mapping_cat = {}
        for category in data["categories"]:
            mapping_cat[category["id"]] = category["name"]
            
        LEN_FILE_IMAGE = 12 # each image file have len(filename) == 12
        len_annotations = len(data["annotations"])
        for a_i,annotation in enumerate(data["annotations"]):
            last_filename = str(annotation["image_id"])
            rest_filename = (LEN_FILE_IMAGE - len(last_filename)) * "0"
            full_filename = rest_filename + last_filename

            category_name = mapping_cat[annotation["category_id"]]
            # create or write file txt
            with open(f"{root_folder_name}/{split_data_name}/{category_name}/labels/{full_filename}.txt", 'a') as f:
                cls, x_min, y_min, x_max, y_max = [mapping_cat[annotation["category_id"]]] + annotation["bbox"]
                f.write(f"{cls} {x_min} {y_min} {x_max} {y_max}\n")
            # copy original image file to image dataset dir
            shutil.copy(f"{image_dir}/{full_filename}.jpg", f"{root_folder_name}/{split_data_name}/{category_name}/images/{full_filename}.jpg")
            print(f"{split_data_name}: {100*(a_i / len_annotations)}", end='\r')