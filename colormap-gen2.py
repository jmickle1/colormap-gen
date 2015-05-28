from omg import *
import random
import omg.colormap

wad = WAD("C:/Users/jmickle/dropbox/projects/games/2015/oitns/oitns_boom.wad")

playpal = wad.data["PLAYPAL"]

paldata = bytearray(playpal.data)

class Pal_color():
    def __init__(self):
        self.red=0
        self.green=0
        self.blue=0
    
    def from_byte_position(self,paldata,position):
        self.red = paldata[position]
        self.green = paldata[position+1]
        self.blue = paldata[position+2]
        
    def to_tuple(self):
        return (self.red,self.green,self.blue)
        
def to_palcolors(paldata):
    output = []
    for i in range(0,256):
        newcol = Pal_color()
        newcol.from_byte_position(paldata,i*3)
        output.append(newcol)
    return output

class Color_ramp():
    #note: color ramps are light to dark

    def __init__(self,*pal_indexes):
        if len(pal_indexes) == 1:
            self.ramp = pal_indexes[0]
        else:
            self.ramp = pal_indexes
        
    def size(self):
        return len(self.ramp)
    
    def resize(self,start_index,size):
        #start_index - first color to use
        #size - output size
        output = []
        
        s_ramp = self.ramp[start_index:]
        
        for i in range(0,size):
            output.append(s_ramp[(i*len(s_ramp))/size])
            
        return output

        
        
colormap = omg.colormap.Colormap()

        
def write_ramp(colormap,color_ramp):
    for c in color_ramp.ramp:
        ramp_draw = color_ramp.resize(color_ramp.ramp.index(c),32)
        for d in range(32):
            colormap.set_position(d,c,ramp_draw[d])
       
    

pink_ramp = []
pink_ramp.extend(range(16,48))
pink_ramp.append(239)
pink_ramp.extend(range(1,3))
pink_ramp.append(0)
pink_cramp = Color_ramp(pink_ramp)

grey_ramp = [4]
grey_ramp.extend(range(80,112))
grey_ramp.extend(range(5,9))
grey_cramp = Color_ramp(grey_ramp)

grey2_ramp = [3]
grey2_ramp.extend(range(105,112))
grey2_ramp.extend(range(5,9))
grey2_cramp = Color_ramp(grey2_ramp)
    
brown_ramp = []
brown_ramp.extend(range(48,80))
brown_ramp.extend(range(1,3))
brown_ramp.append(0)
brown_cramp = Color_ramp(brown_ramp)
    
green_ramp = []
green_ramp.extend(range(112,128))
green_ramp.append(12)
green_ramp.extend(range(7,9))
green_cramp = Color_ramp(green_ramp)
    
lbrown_ramp = []
lbrown_ramp.extend(range(128,144))
lbrown_ramp.extend(range(13,16))
lbrown_ramp.extend(range(77,80))
lbrown_ramp.extend(range(1,3))
lbrown_ramp.append(0)
lbrown_cramp = Color_ramp(lbrown_ramp)

mbrown_ramp = []
mbrown_ramp.extend(range(144,152))
mbrown_ramp.extend(range(78,80))
mbrown_ramp.extend(range(1,3))
mbrown_ramp.append(0)
mbrown_cramp = Color_ramp(mbrown_ramp)

lgreen_ramp = []
lgreen_ramp.extend(range(152,160))
lgreen_ramp.extend(range(9,13))
lgreen_ramp.extend(range(7,9))
lgreen_cramp = Color_ramp(lgreen_ramp)

yellow_ramp = []
yellow_ramp.extend(range(224,232))
yellow_ramp.append(249)
yellow_ramp.extend(range(161,168))
yellow_ramp.extend(range(250,255))
yellow_ramp.append(0)
yellow_cramp = Color_ramp(yellow_ramp)

yellow2_ramp = []
yellow2_ramp.extend(range(160,168))
yellow2_ramp.extend(range(250,255))
yellow2_ramp.append(0)
yellow2_cramp = Color_ramp(yellow2_ramp)

red_ramp = []
red_ramp.extend(range(168,192))
red_ramp.append(239)
red_ramp.extend(range(1,3))
red_ramp.append(0)
red_cramp = Color_ramp(red_ramp)
    
blue_ramp = []
blue_ramp.extend(range(192,208))
blue_ramp.extend(range(240,248))
blue_cramp = Color_ramp(blue_ramp)

orange_ramp = []
orange_ramp.extend(range(208,224))
orange_ramp.extend(range(232,236))
orange_ramp.extend(range(250,255))
orange_ramp.append(0)
orange_cramp = Color_ramp(orange_ramp)

brown2_ramp = []
brown2_ramp.extend(range(236,240))
brown2_ramp.extend(range(1,3))
brown2_ramp.append(0)
brown2_cramp = Color_ramp(brown2_ramp)

peach_ramp = []
peach_ramp.append(248)
peach_ramp.extend(range(215,224))
peach_ramp.extend(range(250,255))
peach_ramp.append(0)
peach_cramp = Color_ramp(peach_ramp)

yellow3_ramp = [249]
yellow3_ramp.append(249)
yellow3_ramp.extend(range(161,168))
yellow3_ramp.extend(range(250,255))
yellow3_ramp.append(0)
yellow3_cramp = Color_ramp(yellow3_ramp)


pink2_ramp = [255]
pink2_ramp.extend(range(26,48))
pink2_ramp.append(239)
pink2_ramp.extend(range(1,3))
pink2_ramp.append(0)
pink2_cramp = Color_ramp(pink2_ramp)

    
write_ramp(colormap,grey_cramp)
write_ramp(colormap,grey2_cramp)
write_ramp(colormap,brown_cramp)
write_ramp(colormap,pink_cramp)
write_ramp(colormap,pink2_cramp)
write_ramp(colormap,green_cramp)
write_ramp(colormap,lgreen_cramp)
write_ramp(colormap,lbrown_cramp)
write_ramp(colormap,mbrown_cramp)
write_ramp(colormap,yellow_cramp)
write_ramp(colormap,yellow2_cramp)
write_ramp(colormap,yellow3_cramp)
write_ramp(colormap,red_cramp)
write_ramp(colormap,blue_cramp)
write_ramp(colormap,brown2_cramp)
write_ramp(colormap,peach_cramp)
write_ramp(colormap,orange_cramp)

colormap.build_invuln()

output_wad = WAD()
output_wad.data["COLORMAP"] = colormap.to_lump()
output_wad.to_file("C:\users\jmickle\documents\oitnscolmap.wad")