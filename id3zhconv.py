from zhconv import convert
import eyed3
import os


simplifiedOption = None
while simplifiedOption != 1 and simplifiedOption != 2:
    input_value = input("请选择 1：转换到繁体  2：转换到简体 \nPlease Enter 1 or 2: ")
    try:
        simplifiedOption = int(input_value)
    except ValueError:
        print("{input} is not a number, please enter number 1 or 2 only".format(input=input_value))

files = os.listdir()
files = [fi for fi in files if fi.endswith(".mp3")]

if simplifiedOption==1:
    convertTo = 'zh-hant'
else:
    convertTo = 'zh-hans'

for mp3file in files:
    audiofile = eyed3.load(mp3file)
    tagToConvert = ['artist', 'album','album_artist',"title"]
    
    for tag in tagToConvert:
        if getattr(audiofile.tag, tag) is not None:
            setattr(audiofile.tag, tag, convert(getattr(audiofile.tag, tag), convertTo))
    audiofile.tag.save()


for fi in files:
    os.rename(fi, convert(fi, convertTo))
