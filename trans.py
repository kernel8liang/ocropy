import glob
import sys
import os
import cv2


if __name__ == '__main__':
    origin_dir = sys.argv[1]
    fname_list = glob.glob(origin_dir + "/*.png")
    for i, f in enumerate(fname_list):
        im = cv2.imread(f)
        im = cv2.resize(im, (384, 64))
        cv2.imwrite(f, im)
        index = f.split("/")[-1].split(".")[0]
        path = f.split("/")[0:-1]
        path = "/".join(path)
        code_file = ("%s/%s.gt.txt") % (path, index)
        code_f = open(code_file)
        code = ""
        for line in code_f:
            code = line.strip()
        new_name = ("%s/%08d_%s_1.png") % (path, i, code)
        os.rename(f, new_name)

