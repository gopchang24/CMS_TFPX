import re

f = open("./data/locating_hdi_MH115_210302.log",'r')

linenumb = 0 
while True :
    line = f.readline()
    if not line :
        break
    linenumb += 1
print("line numb is " , linenumb ) 
f.seek(0)

xx = []
yy = []
zz = []
angle = []
index = 0

while True :
    line = f.readline()
    if not line :
        break

    print( line )
    splited = re.findall("[-+]?\d*\.\d+|\d+", line)
    print( splited )

    xx.append( float( splited[6] ) )
    yy.append( float( splited[7] ) )
    zz.append( float( splited[8] ) )
    angle.append( float( splited[9] ) )
    index += 1    


print( xx )
print( yy )
print( zz )
print( angle )



fw = open( "./data/data_MH0115.h", "w" )

fw.write("double xx[%d] = { " % index)
for item in xx :
    fw.write( "%f, " % item )
fw.write("} ; \n " )

fw.write("double yy[%d] = { " % index)
for item in yy :
    fw.write( "%f, " % item )
fw.write("} ; \n " )

fw.write("double zz[%d] = { " % index)
for item in zz :
    fw.write( "%f, " % item )
fw.write("} ; \n " )

fw.write("double angle[%d] = { " % index)
for item in angle :
    fw.write( "%f, " % item )
fw.write("} ; \n " )



fw.close()
