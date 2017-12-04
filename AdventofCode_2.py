checksum = 0
checksumdigit = 0
with open("table", "r") as file:
    line = file.readline()
    #print line
    while line:
        newlist = line.split()
        #print newlist
        i = 0
        largest = 0
        smallest = 10000
        nextline = False
        while i < len(newlist):
            newnumber = int(newlist[i])
            if int(newlist[i]) > largest:
                largest = int(newlist[i])
                print "new largest is", newlist[i]
            if int(newlist[i]) < smallest:
                smallest = int(newlist[i])
                print "new smallest is", newlist[i]

            i += 1
        checksumdigit = largest - smallest
        checksum += checksumdigit
        print "the checksum digit for this line is", str(checksumdigit)
        with open("checksums", "w") as filay:
            filay.write(str(checksumdigit) + "\n")
            filay.close()

        line = file.readline()
with open("checksums", "r") as fille:
    lines = fille.readline()
    while lines:
        checksum = checksum + int(lines)
        print "the checksum is now", checksum
        lines = fille.readline()
checksum -= checksumdigit
print checksum
#checksumdigit = largest - smallest
#print "the checksum digit for this line is", str (checksumdigit)
#checksum = 0
#with open("table", "r") as file:
    #line = file.readline()
   # print line
  #  while line:
      #  newlist = line.split()
   #     print newlist