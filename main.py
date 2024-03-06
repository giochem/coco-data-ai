import argparse
from utils import init_preprocessing, put_data
# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("-i", "--Init", action='store_true', help = "Dowload data and extractall to preprocessing")
parser.add_argument("-d", "--Dataset", nargs='?', const='all', type=str, help = "Put data to each categories: images, labels"+
                    " |ex: python main.py -d train,val,all")

args = parser.parse_args()

# Link setup install 
# https://gist.github.com/mkocabas/a6177fc00315403d31572e17700d7fd9
ANNOTATIONS_COCO_URL = "http://images.cocodataset.org/annotations/annotations_trainval2017.zip"
VAL_COCO_URL = "http://images.cocodataset.org/zips/val2017.zip"
TRAIN_COCO_URL =  "http://images.cocodataset.org/zips/train2017.zip"

VAL_INSTANCE_ANNOTATION = './preprocessing/annotations/instances_val2017.json'
TRAIN_INSTANCE_ANNOTATION = './preprocessing/annotations/instances_train2017.json'

ROOT_FOLDER_NAME = "dataset"
VAL_IMAGE_DIR = "./preprocessing/val2017"
TRAIN_IMAGE_DIR = "./preprocessing/train2017"

if args.Init:
    init_preprocessing(ANNOTATIONS_COCO_URL, VAL_COCO_URL, TRAIN_COCO_URL)
if args.Dataset:
    split_dataset = args.Dataset.split(',')
    if 'all' in split_dataset:
        put_data(VAL_INSTANCE_ANNOTATION,ROOT_FOLDER_NAME,VAL_IMAGE_DIR, "val")
        put_data(TRAIN_INSTANCE_ANNOTATION, ROOT_FOLDER_NAME,TRAIN_IMAGE_DIR,"train")
    else:
        if 'val' in split_dataset:
            put_data(VAL_INSTANCE_ANNOTATION,ROOT_FOLDER_NAME,VAL_IMAGE_DIR, "val")
        if 'train' in split_dataset:
            put_data(TRAIN_INSTANCE_ANNOTATION, ROOT_FOLDER_NAME,TRAIN_IMAGE_DIR,"train")