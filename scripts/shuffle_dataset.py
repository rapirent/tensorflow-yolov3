import argparse
import random
from datetime import datetime
import os

parser = argparse.ArgumentParser()
parser.add_argument('--target', type=str, default='', help='target file')
parser.add_argument('--output', type=str, default='shuffle.txt', help='output_file')
opt = parser.parse_args()

if __name__ == '__main__':
    with open(opt.target, 'r') as t:
        lines = t.readlines()
        random.seed(datetime.now())
        random.shuffle(lines)
        f = open(opt.output, 'w')
        for line in lines:
            print(line, end='', file=f)
        
