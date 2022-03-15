import os
import glob


"""
Help on function glob in module glob:

glob(pathname, *, recursive=False)
    Return a list of paths matching a pathname pattern.
    
    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.
    
    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
"""

# os.mkdir("Folder")

# !touch text1.txt
# !touch text2.csv
# !touch text3.json
# !touch text4.py
# !touch text5.txt
# !mv text* Folder

print(glob.glob("Folder"))
print(glob.glob(os.path.join("Folder", "*.txt")))

# python3 glob_test.py

"""
['Folder']
['Folder/text5.txt', 'Folder/text1.txt']
"""
