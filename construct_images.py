"""Build mnist images for classification """

from PIL import Image

import numpy
import csv
import os


def main():
    create_dirs()
    build_images_from_csv()

def create_dirs():
    path = 'data/downloads/'
    if not os.path.exists(path):
        os.makedirs(path)
    for x in range(10):
        new_path = path + str(x)
        if not os.path.exists(new_path):
            os.makedirs(new_path)

def build_images_from_csv():
    path = 'data/downloads/'
    with open('data/mnist/sample.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in reader:
            row = row[0].split(',')
            arr = []
            for x in range(1, 784, 28):
                line = []
                for y in range(28):
                    line.append(int(row[x+y]))
                arr.append(line)
            array = numpy.array(arr, dtype=numpy.uint8)
            img = Image.fromarray(array)
            img_path = path + row[0][0]
            img_path_name = img_path + '/' + str(len(os.listdir(img_path))) + '.png'
            img.save(img_path_name)

if __name__ == "__main__":
    main()
