<h1 align="center">Batch File Renamer</h1>

[![CodeFactor](https://www.codefactor.io/repository/github/joshuacrotts/Batch-File-Renamer/badge)](https://www.codefactor.io/repository/github/joshuacrotts/Batch-File-Renamer) ![GitHub contributors](https://img.shields.io/github/contributors/JoshuaCrotts/Batch-File-Renamer) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/JoshuaCrotts/Batch-File-Renamer) ![GitHub repo size](https://img.shields.io/github/repo-size/JoshuaCrotts/Batch-File-Renamer)  ![](https://tokei.rs/b1/github/JoshuaCrotts/Batch-File-Renamer) ![](https://tokei.rs/b1/github/JoshuaCrotts/Batch-File-Renamer?category=files) [![GitHub issues open](https://img.shields.io/github/issues/JoshuaCrotts/Batch-File-Renamer)]() 
[![GitHub issues closed](https://img.shields.io/github/issues-closed-raw/JoshuaCrotts/Batch-File-Renamer)]()

Have you ever had a list of files in a directory that you wanted to rename all at once, but couldn't find the necessary bash or terminal commands to do so? Well, this Python script has you covered! Sure, it's a very narrow use-case, but it works! For instance, when I download and splice spritesheets, very often I find myself having to go through and rename every file to have a common, no padded-zero prefix (e.g. tile_009.png, tile_010.png... this just screws up my whole day!). 

## Usage ##

To use this, open your terminal/Python shell, and use the following format to execute the program:

<code>python main.py /path/to/dir/ old_file_prefix desired_file_prefix .file_extension padded_zero_count</code>

Example:

<code>python main.py C:\Users\Joshua\Downloads\test\ tile_0 frame_ .png 2</code>

The above command will rename all files with the prefix tile_0, and 2 successive padded zero integers (i.e. tile_010, tile_020, tile_033, etc.) to frame_*i*, where *i* is an integer between 0 and *n*, where *n* is the number of files in the directory.


## Dependencies

The only dependency for this project is Python 3.8.

## Reporting Bugs

See the Issues Tab.
