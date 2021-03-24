import re

f = open("./data/dry_run_210303.txt",'r')

linenumb = 0 
while True :
    line = f.readline()
    if not line :
        break
    linenumb += 1
print("line numb is " , linenumb ) 
f.seek(0)

ax = []
ay = []
bx = []
by = []
cx = []
cy = []
dx = []
dy = []

index = 0

while True :
    line1 = f.readline()
    line2 = f.readline()
    line3 = f.readline()
    line4 = f.readline()
    if not line4 :
        break
    print( line1 )
    print( line2 )
    splited3 = re.findall("[-+]?\d*\.\d+|\d+", line3)
    print( splited3 )
    splited4 = re.findall("[-+]?\d*\.\d+|\d+", line4)
    print( splited4 )

    ax.append( float( splited3[6] ) )
    ay.append( float( splited3[7] ) )
    bx.append( float( splited3[9] ) )
    by.append( float( splited3[10] ) )

    cx.append( float( splited4[6] ) )
    cy.append( float( splited4[7] ) )
    dx.append( float( splited4[9] ) )
    dy.append( float( splited4[10] ) )
    index += 1    

print( "result" )
print( ax )
print( ay )
print( dx )
print( dy )

fw = open( "./data/pad_alignment.h", "w" )

fw.write("double ax[%d] = { " % index)
for item in ax :
    fw.write( "%f, " % item )
fw.write("} ; \n" )

fw.write("double ay[%d] = { " % index)
for item in ay :
    fw.write( "%f, " % item )
fw.write("} ; \n" )

fw.write("double bx[%d] = { " % index)
for item in bx :
    fw.write( "%f, " % item )
fw.write("} ; \n" )

fw.write("double by[%d] = { " % index)
for item in by :
    fw.write( "%f, " % item )
fw.write("} ; \n" )

fw.write("double cx[%d] = { " % index)
for item in cx :
    fw.write( "%f, " % item )
fw.write("} ; \n" )

fw.write("double cy[%d] = { " % index)
for item in cy :
    fw.write( "%f, " % item )
fw.write("} ; \n" )

fw.write("double dx[%d] = { " % index)
for item in dx :
    fw.write( "%f, " % item )
fw.write("} ; \n" )

fw.write("double dy[%d] = { " % index)
for item in dy :
    fw.write( "%f, " % item )
fw.write("} ; \n" )


fw.close()
