
import dirsync
import os
import datetime
import numpy 

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

f1 = 'C:\\Users\\aspitarl\\Documents\\synctest\\Folder 1\\'
f2 = 'C:\\Users\\aspitarl\\Documents\\synctest\\Folder 2\\'

folders = [ name for name in os.listdir(f1) if os.path.isdir(os.path.join(f1, name)) ]

dates  = []
sizes = []
for folder in folders:
    dates.append( datetime.datetime.strptime(folder,'%Y-%m-%d'))
    size = get_size( os.path.join(f1,folder))

# cumsize = numpy.trapz(sizes)

# print(cumsize)


# folders = ['A','B']

# for folder in folders:
#     src = os.path.join(f1,folder)
#     dst = os.path.join(f2,folder)
#     dirsync.sync(src,dst,'sync', create = True)


