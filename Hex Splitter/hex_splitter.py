# HEX SPLITTER
# Split 16bit Hexadecimal numbers into 8 sets of 2bit Hexadecimal Numbers

def inputNSplit(filename):
    with open(filename) as f:
        chunks = []
        for x in f:
            x = x[2:]
            n = 2
            chunks.append([("0x" + x[i:i+n]) for i in range(0, len(x)-1, n)])
            # print(chunks)
        f.close()
        return chunks

def toCArray(hexList):
    count = 0
    f = open("output.txt","w")
    f.write(f"uint8_t {arrayName}[{arrayLength}][8] = " + "{\n")
    f.close()
    for hexArray in hexList:
        # print(str(hexArray))
        hexArray = str(hexArray).replace("[", "{")
        hexArray = hexArray.replace("]", "}")
        hexArray = hexArray.replace("'", "")
        with open("output.txt","a") as f:
            f.write("  " + hexArray + f", //{count:02}\n")
            f.close()
        count += 1

    f = open("output.txt","a")
    f.write("};\n")
    f.close()
            

hex = inputNSplit("input.txt")
arrayName = input("Enter Array Name: ")
arrayLength = len(open("input.txt").readlines())
toCArray(hex) 