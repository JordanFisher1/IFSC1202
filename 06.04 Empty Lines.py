inputfilename = "06.04 EmptyLinesInput.txt"
outputfilename = "06.04 EmptyLinesOutput.txt"
fout = open(outputfilename, "w")
readcount = 0
writecount = 0
with open (inputfilename, "r") as f:
    for line in f:
        readcount += 1
        if line.strip():
            writecount += 1
            fout.write(line)
fout.close()
print(readcount, "records read")
print(writecount, "records written")
