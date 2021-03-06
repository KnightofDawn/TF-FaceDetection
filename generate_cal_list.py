import glob
import random

size_list = (12, 24, 48)

for size in size_list:
    lines = []
    for i in range(45):

        dir_path = 'data_prepare/cal_positive_' + str(i+1) + '_' + str(size) + '/*.jpg'

        filenames = glob.glob(dir_path)

        filelist = map(lambda x:x+' '+str(i)+'\n', filenames)
        lines = lines+filelist

    random.shuffle(lines)
    savename = 'cal_' + str(size) + '_list.txt'
    with open(savename,'w') as f:
        f.writelines(lines)