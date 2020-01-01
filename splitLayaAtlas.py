import argparse
import os
import sys
import shutil
from PIL import Image
import json
path = os.path


def printError(*tx):
    print('--- err ---')
    print(tx)
    print('--- !!! ---')


def dispose1file(fn: str, only1=False):
    atlasName = fn + '.atlas'
    if only1 and not path.exists(atlasName):
        printError('file not exists', atlasName)
        return

    print('====')
    print(atlasName)

    if not path.exists(fn):
        os.makedirs(fn)

    content = None
    with open(atlasName, encoding='utf-8') as f:
        content = f.read()
    data = json.loads(content)

    imagetx: str = data['meta']['image']
    dirName = path.dirname(atlasName)
    image_ps = imagetx.split(',')
    big_images = []
    for ip in image_ps:
        im = Image.open(dirName+'/'+ip)
        big_images.append(im)

    frames = data['frames']
    tn = 0
    for k in frames.keys():
        tn += 1
        print(k)
        frame = frames[k]["frame"]
        idx = frame['idx']
        width = frame["w"]
        height = frame["h"]
        ltx = frame["x"]
        lty = frame["y"]
        rbx = ltx+width
        rby = lty+height
        result_image = None
        if k.endswith('.png'):
            result_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        else:
            result_image = Image.new("RGB", (width, height), (0, 0, 0, 0))
        im = big_images[idx]
        rect_on_big = im.crop((ltx, lty, rbx, rby))
        result_image.paste(rect_on_big, (0, 0, width, height))
        result_image.save(fn+'/'+k)
    print('----')
    print('image num:', tn)

    for im in big_images:
        del im


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-name")
    args = parser.parse_args()
    fn: str = args.name
    if fn:
        dispose1file(fn, True)
    else:
        fns = []
        for root, dirs, fs in os.walk('./'):
            for f in fs:
                if f.endswith('.atlas'):
                    i = f.rfind('.atlas')
                    fns.append(root+'/'+f[:i])
        for f in fns:
            dispose1file(f)


if __name__ == '__main__':
    main()
