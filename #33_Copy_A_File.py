#copyfile() = copies contents of a file
#copy() = copyfile() + permission mode + destiation can be a directiory
#copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

shutil.copyfile("test.txt", "copy.txt") #src,dst