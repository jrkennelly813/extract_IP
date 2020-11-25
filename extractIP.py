# Author: Justin Kennelly
# Date: 11-25-2020
# Purpose: Parse Source and Destination IP Addresses from a wireshark text file

#region FUNCTIONS
def CheckLine(currLine):
    key = ['No.', 'Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info'] # IP Addresses we are parsing occur after this line
    flag = False
    if currLine == key:
        flag = True # If the current line matches the key, signal the program the key was found
        return flag
    else:
        return flag

def parse_File(file):
    IPList = []
    
    with open(file, 'r') as InFile:
        print("File wireShark.txt was opened.")      
        for lines in InFile:
            line = lines.strip().split()
            flag = CheckLine(line)
            if flag == True: # If the flag is found, parse the following line for the IP addresses
                ip = str(next(InFile)).strip().split()
                IPList.append((ip[2], ip[3])) # Store the addresses
            else:
                continue
    InFile.close()
    print("File wireShark.txt was closed.")
    return IPList

def writeOutFile(iplist, outFile):
    with open(outFile, 'w') as outFile:
        print("File IPAddress.txt was opened.")
        outFile.write("Source IP                Destination IP" + "\n\n")
        for ip in iplist:
            outFile.write("{}               {} \n\n".format(ip[0], ip[1])) # Write the IP Addresses to the output file
    outFile.close()
    print("File IPAdresses.txt was closed.")
#endregion

def main():
    inFile = "wireShark.txt"
    outFile = "IPAddresses.txt"
    iplist = parse_File(inFile)
    writeOutFile(iplist, outFile)

if __name__ == "__main__":
    main()



        
    