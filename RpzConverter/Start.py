from ipaddress import IPv4Address
import codecs
text_file = open("output.txt", "w")
def is_ipaddress(address):
    try:
         IPv4Address(address)
         return True
    except:
        return False

file = codecs.open("domains.txt","r", "utf-8")
for line in file.readlines():
    line = line.rstrip()
    if not is_ipaddress(line):
        text_file .write(line+"\n")
