#xxx/xxx.jpg 18.19,6.32,424.13,421.83,20 323.86,2.65,640.0,421.94,20 
#xxx/xxx.jpg 48,240,195,371,11 8,12,352,498,14
# image_path x_min, y_min, x_max, y_max, class_id  x_min, y_min ,..., class_id 
import argparse
import cv2
import glob
import os

parser = argparse.ArgumentParser()
parser.add_argument('--dataset', type=str, default='', help='dataset_folder')
parser.add_argument('--output', type=str, default='output.txt', help='output_file')
parser.add_argument('--lpr_annotation', type=str, default='lpr_annotation.txt', help='lpr number annotation')
opt = parser.parse_args()

if __name__ == '__main__':
    f = open(opt.output,'w')
    jpg_list = glob.glob(opt.dataset + '**/*.jpg', recursive=True) + glob.glob(opt.dataset + '**/*.JPG', recursive=True)
    for jpg in jpg_list:
        try:
            open_file = open(os.path.splitext(jpg)[0] + '.lpr', 'r')
        except OSError:
            print('can not open file: ' + jpg + '.lpr')
        else:
            print('{}'.format(os.path.splitext(jpg)[0] + '.jpg'), end='',file=f)
            line = open_file.readline().replace('\n', '')
            while line:
                xy = line.split(' ')
                xy = [int(element) for element in xy]
                x_min = min(xy[0],xy[2],xy[4], xy[6])
                x_max = max(xy[0],xy[2],xy[4], xy[6])
                y_min = min(xy[1],xy[3],xy[5], xy[7])
                y_max = max(xy[1],xy[3],xy[5], xy[7])
                line = open_file.readline()
                class_id = int(line)
                #draft
                line = open_file.readline()
                line = open_file.readline()
                real_number = line
                print(' {},{},{},{},{}'.format(str(x_min), str(y_min), str(x_max), str(y_max), class_id),end='',file=f)
                line = open_file.readline()
                line = open_file.readline().replace('\n', '')
            print('',file=f)
    print("-------\nprocessing the png")
    png_list = glob.glob(opt.dataset+'/**/*.png', recursive=True) + glob.glob('**/*.JPG', recursive=True)
    for png in png_list:
        img = cv2.imread(png)
        print('file proceed: ' + png)
        cv2.imwrite(os.path.splitext(png)[0] + '.jpg', img)
        try:
            open_file = open(os.path.splitext(png)[0] + '.lpr', 'r')
        except OSError:
            print('can not open file: ' + png + '.lpr')
        else:
            print('{}'.format(os.path.splitext(png)[0] + '.jpg'), end='',file=f)
            line = open_file.readline().replace('\n', '')
            while line:
                xy = line.split(' ')
                xy = [int(element) for element in xy]
                x_min = min(xy[0],xy[2],xy[4], xy[6])
                x_max = max(xy[0],xy[2],xy[4], xy[6])
                y_min = min(xy[1],xy[3],xy[5], xy[7])
                y_max = max(xy[1],xy[3],xy[5], xy[7])
                #draft                
                line = open_file.readline()
                line = open_file.readline()
                line = open_file.readline()
                print(' {},{},{},{},{}'.format(str(x_min), str(y_min), str(x_max), str(y_max), '0'),end='',file=f)
                line = open_file.readline()
                line = open_file.readline().replace('\n', '')
            print('',file=f)

