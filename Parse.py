from dataclasses import replace
print('''SAMARTH CHAWLA'S PARSING PROJECT''')

with open("website.log",'r') as f:
    lines=f.readlines()
    with open("output.txt","w+") as of:
        of.write("IP\t\tDate Time\t\t\tRequest\t\tProtocol\tStatus Code\tPacket Size\n")
        for i in lines:
            i=i.replace('[','')
            i=i.replace(']','')
            i=i.replace('"','')
            line =i.split()
            of.write(f"{line[0]}\t{line[3]+line[4]}\t{line[5]}\t\t{line[7]}\t{line[8]}\t\t{line[9]}\n")
    of.close()
    f.close()














