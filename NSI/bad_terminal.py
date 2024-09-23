from PIL import Image
import time
import os
import math

def convert_to_emojies(list):

    data = ""
    count = 0
    for y in list:
        
        for x in y:
            if x == 255:
                data += "⚫"
            else:
                data += "🔴"
        count += 1
        if count != len(list):
            data += "\n"

    return data

def get_avg_fps(PIL_Image_object):
    """ Returns the average framerate of a PIL Image object """
    PIL_Image_object.seek(0)
    frames = duration = 0
    while True:
        try:
            frames += 1
            duration += PIL_Image_object.info['duration']
            PIL_Image_object.seek(PIL_Image_object.tell() + 1)
        except EOFError:
            return frames / duration * 1000
    return None

with Image.open('bad.gif') as im:

    print("Number of frames: "+str(im.n_frames))

    fps = get_avg_fps(im)

    print("Average Fps:",fps)
    print("Terminal Size:",os.get_terminal_size())

    line = math.floor(os.get_terminal_size().lines)
    column = math.floor(os.get_terminal_size().columns/2)

    for i in range(im.n_frames):
        im.seek(im.n_frames // im.n_frames * i)

        a = im.resize((column,line))
        a = a.convert('1')
        pixels = list(a.getdata())
        width, height = a.size
        pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
        print(chr(27) + "[2J")
        print(convert_to_emojies(pixels))
        time.sleep(1/fps)
