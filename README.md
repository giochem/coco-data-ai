# coco-data-ai
A script install coco data

## Installation requirement
```
pip install -r requirement.txt
```

## Preprocessing data and Automatic setup data

```
Usage: python main.py [OPTIONS]

Options:
  -i      Dowload zip file and Init preprocessing
  -d      Put data to dataset folder by split name
  --help  Show this message and exit.
```

Example commands
```
# Preprocessing data
$ python main.py -i

# Preprocessing data and Automatic setup all data
$ python main.py -i -d

# Automatic setup val data (must run -i first)
$ python main -d val
```
