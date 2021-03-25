import re

f = open("./data/pick_and_place_for_dry_run_210303.txt",'r')

linenumb = 0 
while True :
    line = f.readline()
    if not line :
        break
    linenumb += 1
print("line numb is " , linenumb ) 
f.seek(0)

x = []
y = []
a = []


index = 0

while True :
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    line5 = f.readline()
    if not line5 :
        break
    print( line3 )
    print( line4 )
    splited3 = re.findall("[-+]?\d*\.\d+|\d+", line3)
    print( splited3 )
    splited4 = re.findall("[-+]?\d*\.\d+|\d+", line4)
    print( splited4 )

    x.append( float( splited3[6] ) )
    y.append( float( splited3[7] ) )
    a.append( float( splited4[10] ) )

    index += 1    

print( "result" )
print( x )
print( y )
print( a )

fw = open( "./data/sensor_disp.h", "w" )

fw.write("double x[%d] = { " % index)
for item in x :
    fw.write( "%f, " % item )
fw.write("} ; \n" )

fw.write("double y[%d] = { " % index)
for item in y :
    fw.write( "%f, " % item )
fw.write("} ; \n" )

fw.write("double a[%d] = { " % index)
for item in a :
    fw.write( "%f, " % item )
fw.write("} ; \n" )


fw.close()
