# PyTap
A python module that allows you to get data from hyperPad .tap files.

## Functions
- `launch(tap)` - Initializes a .tap file, do this before anything else.  
- `get_game_details()` - Returns a JSON version of gameDetails.plist, it contains stuff such as the game name, and aspect ratios.  
- `get_level_details()` - Returns a JSON version of levelDetails.plist, has some dumb stuff you probably wont use.  
- `get_scenes()` - Returns a JSON with arrays for every scene and overlay in the project, this is one scene `{'name': 'Scene 1', 'position': (514.4542846679688, 480.0265808105469), 'zoom': 0.48193585872650146, 'preload': 0}`  
- `get_objects()` - Returns a JSON with every scene, inside the scenes are every object on that scene, and their data.  
- `get_behaviours()` - Returns a JSON of every object, and their behaviours.  
- `get_layers()` - Returns a JSON of every Layer in the project, each layer has its scene and if its a ui layer.  
- `get_project()` - Gets everything and compiles it into 1 JSON.  
- `extract_assets(to, format, compress)` - Extracts all assets with the `format` to `to` (format `format` like `".png"`), `compress` will resize all the images to their dimensions divided by `compress`, good if you wanna port a hyperpad game to hardware with little VRAM.    
- `get_asset_path(path, format, get_hd)` - Usually if you get a objects asset path, it will just be a path to the folder that has the asset in it, you can put that in here to get the actual path to the asset. (hyperPad stores a hd and non hd version of images, the non hd is half the normal size, so if you wanna get the HD make sure get_hd is `True`.)  
- `get_image_dimensions(path, format, get_hd)` - Gets the dimensions of an image, same inputs as `get_asset_path()`  
- `get_asset_size(path, format, get_hd)` - Gets the size of an asset in Bytes.  

## Required Libraries
This is everything thats imported in the .py, youre a big boy im sure youll figure it out.  
```
import zipfile
import plistlib
import json
import io
import os
import sqlite3
import base64
import tempfile
from plistlib import UID
from PIL import Image
```

## how to use the pytap audio extractor

youll need ffmpeg installed on your computer

```
python PyTapAudioExtract.py "C:\Path\To\YourFile.tap"
```
