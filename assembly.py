from PIL import Image, ImageDraw ,ImageFont
from operator import itemgetter
from random import randint,choice
import string,os
sentence="Manaki antha ledu le"

# 18pts trebuchet - 16,21

def sizer(fnt):
    sz=[]
    for each in string.ascii_letters:
        # hld=d.textsize(each, font=fnt)[0]
        sz.append(fnt.getsize(each))
    dims=[]
    # print(font.getsize("m"))
    dims.append(max(sz,key=itemgetter(0))[0]) #Width
    dims.append(max(sz,key=itemgetter(1))[1]) #Height
    # print(dims)
    return dims

def alfa(leter,font_size,font):
    # print(leter)
    wdth=font_size[0]
    hgt=font_size[1]
    if leter!=" ":
        clr=(randint(70,226), randint(70,226),randint(70,200))
        img = Image.new('RGB', (wdth+5,hgt+2), color = clr)
        d = ImageDraw.Draw(img)
        d.text((2,0), leter,font=font, fill=(0,0,0))
        return img.rotate(randint(-15,15),resample=Image.BICUBIC,fillcolor=clr)
    else:
        img = 0
        return img

def main(total):
    i=0
    j=10
    hgtmx=0
    a4im = Image.new('RGB', (595, 700), (255, 255, 255))
    for each in total:
        font=ImageFont.truetype(choice(['trebucbd.ttf','comicbd.ttf','comic.ttf','VeraMoBI.ttf','Times_New_Roman.ttf','FreeSans.ttf','Verdana_Italic.ttf']), randint(22,32))
        font_size = sizer(font)
        wdth=font_size[0]+5
        hgt=font_size[1]+2
        word = alfa(each,font_size,font)
        if word:
            if (wdth+i)>577:
                i=0
                j=j+hgtmx+9
            # for letter in word[1:]:
            # word=word.rotate(25,expand=1)
            a4im.paste(word,[wdth+i,j+randint(-2,3)])
            i=i+wdth
        else:
            i=i+wdth
        if hgt>hgtmx:
            hgtmx=hgt
    a4im.save("./static/letter.jpeg")

# main(sentence)
