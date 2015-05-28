from omg import *
import random
import omg.colormap

wad = WAD("D:/Doom/IWADS/DOOM.WAD")

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
    
brown_ramp = []
brown_ramp.extend(range(48,80))
brown_ramp.extend(range(1,3))
brown_cramp = Color_ramp(brown_ramp)
    
green_ramp = []
green_ramp.extend(range(112,128))
green_ramp.extend(12)
green_ramp.extend(0)
green_cramp = Color_ramp(green_ramp)
    
lbrown_ramp = []
lbrown_ramp.extend(range(128,144))
lbrown_ramp.append(151)
lbrown_ramp.append(range(77,80))
lbrown_ramp.append(range(1,3))
lbrown_cramp = Color_ramp(lbrown_ramp)
    
    
write_ramp(colormap,grey_cramp)
write_ramp(colormap,brown_cramp)
write_ramp(colormap,pink_cramp)
write_ramp(colormap,green_cramp)
write_ramp(colormap,lbrown_cramp)

output_wad = WAD()
output_wad.data["COLORMAP"] = colormap.to_lump()
output_wad.to_file("C:\users\jmickle\documents\colmap.wad")