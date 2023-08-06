## OpenDataLab Python SDK 0.0.4

# Features:
1. download dataset from offical website: https://opendatalab.com/
2. preview dataset info online

# Usage: 
1. install
```
pip install opendatalab-python-sdk==0.0.4
```

2. download dataset into local path
```
script:
$ python -m opendatalab.download --help    
    Tool for download opendatalab public dataset.  

  Options:
    --name        TEXT    Name of the public dataset.
    --format      TEXT    Format, avaiable options: source, standard.
    --root        TEXT    Data root path, default: current working path.
    --thread      INTEGER Number of thread for download, default: 10.
    --limit_speed INTEGER Download limit speed: KB/s, 0 is unlimited, default: 0

example:
1). download dataset source compressed
    $ python -m opendatalab.download --name coco --format source --root /home/XXX/coco

2). download standard format compressed
    $ python -m opendatalab.download --name coco --format standard --root /home/XXX/coco --thread   8 --limit_speed 5000
```


# Support
More see: https://opendatalab.com/docs/3