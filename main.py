import sys
import os

def main():
  arg_count = len(sys.argv)
  argv = list(sys.argv)

  # Format should be "python main.py path/to/dir/ old_prefix desired_prefix .extsn padded_zero_count"
  if arg_count != 6:
    print("Error, you need to have six command arguments: main.py /path/to/dir old_prefix desired_prefix .extsn padded_zero_count!")
    return
  
  # Grab the directory to search through.
  path = argv[1]

  # The path itself should not be a file.
  if os.path.isfile(path):
    print("Error, your path {} needs to be a directory; not a file.".format(path), file=sys.stderr)
    return

  # Grab the arguments. 
  common_prefix = argv[2]
  desired_prefix = argv[3]
  common_suffix = argv[4] # File extension.
  zero_count = int(argv[5]) # Padded zeroes are for files such as tile009 tile010... etc.

  # Now walk the path to see how many files are in the directory.
  path, dirs, files = next(os.walk(path))
  file_count = len(files)

  # Iterate through the files and change them one by one.
  for i in range (file_count):
    # Modify the path name with the number of padded zeroes.
    i_str = str(i)
    file_name = path + common_prefix + i_str.zfill(zero_count) + common_suffix
    if os.path.exists(file_name):
      modified_name = path + desired_prefix + str(i) + common_suffix
      os.rename(file_name, modified_name)
    else:
      print("Error, your file name {} does not exist.".format(file_name), file=sys.stderr)
      return

  print("Renaming successful!")

main()  
