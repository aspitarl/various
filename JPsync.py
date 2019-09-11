import os
import datetime
import numpy as np
import pandas as pd

JPpath = 'C:\\Users\\aspitarl\\Desktop\\JP Data\\Reports'
rawdatapath = 'C:\\Users\\aspitarl\\OneDrive\\MHD Common Drive\\Data\\Raw Data'

from shutil import copyfile

fns = [fn for fn in os.listdir(JPpath) if os.path.isfile(os.path.join(JPpath,fn))]

for fn in fns:
    fp = os.path.join(JPpath,fn)
    mtime = os.path.getmtime(fp)
    dt = datetime.datetime.fromtimestamp(mtime)
    folderstr = dt.strftime("%Y-%m-%d")
    outfolder = os.path.join(rawdatapath,folderstr + "\\Logfiles\\JP\\")
    if not os.path.exists(outfolder):
        os.makedirs(outfolder)
    outpath = os.path.join(outfolder,fn)
    copyfile(fp,outpath)

