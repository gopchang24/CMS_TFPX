import re

f1 = open("./data/locating_hdi_MH111_210302.log",'r')
f2 = open("./data/locating_hdi_MH112_210302.log",'r')
f3 = open("./data/locating_hdi_MH113_210302.log",'r')
f4 = open("./data/locating_hdi_MH114_210302.log",'r')
f5 = open("./data/locating_hdi_MH115_210302.log",'r')

xx = []
yy = []
zz = []
angle = []
index = 0
while index<15 :
    line1 = f1.readline()
    splited = re.findall("[-+]?\d*\.\d+|\d+", line1)
    xx.append( float( splited[6] ) )
    yy.append( float( splited[7] ) )
    zz.append( float( splited[8] ) )
    angle.append( float( splited[9] ) )
    index += 1    

index = 0
while index<15 :
    line2 = f2.readline()
    splited = re.findall("[-+]?\d*\.\d+|\d+", line2)
    xx.append( float( splited[6] ) )
    yy.append( float( splited[7] ) )
    zz.append( float( splited[8] ) )
    angle.append( float( splited[9] ) )
    index += 1    

index = 0
while index<15 :
    line3 = f3.readline()
    splited = re.findall("[-+]?\d*\.\d+|\d+", line3)
    xx.append( float( splited[6] ) )
    yy.append( float( splited[7] ) )
    zz.append( float( splited[8] ) )
    angle.append( float( splited[9] ) )
    index += 1    

index = 0
while index<15 :
    line4 = f4.readline()
    splited = re.findall("[-+]?\d*\.\d+|\d+", line4)
    xx.append( float( splited[6] ) )
    yy.append( float( splited[7] ) )
    zz.append( float( splited[8] ) )
    angle.append( float( splited[9] ) )
    index += 1    

index = 0
while index<15 :
    line5 = f5.readline()
    splited = re.findall("[-+]?\d*\.\d+|\d+", line5)
    xx.append( float( splited[6] ) )
    yy.append( float( splited[7] ) )
    zz.append( float( splited[8] ) )
    angle.append( float( splited[9] ) )
    index += 1    




print( xx )
print( yy )
print( zz )
print( angle )



fw = open( "./data/data_sum.h", "w" )

fw.write("double xx[%d] = { " % (15*5))
for item in xx :
    fw.write( "%f, " % item )
fw.write("} ; \n " )

fw.write("double yy[%d] = { " % (15*5))
for item in yy :
    fw.write( "%f, " % item )
fw.write("} ; \n " )

fw.write("double zz[%d] = { " % (15*5))
for item in zz :
    fw.write( "%f, " % item )
fw.write("} ; \n " )

fw.write("double angle[%d] = { " % (15*5))
for item in angle :
    fw.write( "%f, " % item )
fw.write("} ; \n " )



fw.close()
