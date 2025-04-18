#!/usr/bin/env python3

import os
from PIL import Image
from multiprocessing import Pool

def convert(args):
    print("Convert {} in  {}".format(args[0], args[1]))
    img = Image.open(args[0])
    img.rotate(-90).resize((128, 128)).convert("RGB").save(args[1], 'jpeg')
    img.close()

if __name__ == "__main__":

    #Estas direcciones son para probar, cambiar por direcciones a usar
    dir_path = os.path.dirname(os.path.realpath(__file__))
    old_path = os.path.join(dir_path, '../images/')
    new_path = os.path.join(dir_path, '../opt/icons/')


    if not os.path.exists(os.path.dirname(new_path)):
        os.makedirs(os.path.dirname(new_path))

    tasks = []

    for image in os.listdir(old_path):
        if '.' not in image[0]:
            tasks.append([os.path.join(old_path, image), os.path.join(new_path, image.split('.')[0])])

    p = Pool(len(tasks))
    p.map(convert, tasks)