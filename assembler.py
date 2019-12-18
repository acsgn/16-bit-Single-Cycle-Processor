import sys

op = 67108864  # 2^26
rs = 2097152  # 2^21
rt = 65536  # 2^16
rd = 2048  # 2^11
shamt = 64  # 2^6

args = sys.argv.copy()
args.pop(0)
if len(args) < 1 or len(args) > 2:
    print("Usage: input [output]")
    exit()

inp = args.pop(0)
out = "a.txt" if len(args) is 0 else args.pop(0)

try:
    file = open(inp, "r")
    lines = file.readlines()
    file.close()
except IOError:
    print("File not found:", inp)
    exit()

labels = {}
codes = []
comment = 0
for i in range(len(lines)):
    line = lines[i].strip()
    if line == '' or line.startswith('#'):
        continue
    words = line.split(" ")
    if not (1 < len(words) < 6):
        print("Syntax error at line", i+1)
        exit()
    if words[0].endswith(":"):
        labels[words.pop(0)[:-1]] = len(codes)
    codes.append(words)

binary = []
for line in codes:
    if line[0].lower() == "add":
        dec = op * 0 + rd * int(line[1][1:-1]) + rs * int(line[2][1:-1]) + rt * int(line[3][1:])
    elif line[0].lower() == "sub":
        dec = op * 1 + rd * int(line[1][1:-1]) + rs * int(line[2][1:-1]) + rt * int(line[3][1:])
    elif line[0].lower() == "mult":
        dec = op * 2 + rs * int(line[2][1:-1]) + rt * int(line[3][1:])
    elif line[0].lower() == "and":
        dec = op * 3 + rd * int(line[1][1:-1]) + rs * int(line[2][1:-1]) + rt * int(line[3][1:])
    elif line[0].lower() == "or":
        dec = op * 4 + rd * int(line[1][1:-1]) + rs * int(line[2][1:-1]) + rt * int(line[3][1:])
    elif line[0].lower() == "addi":
        dec = op * 5 + rd * int(line[1][1:-1]) + rs * int(line[2][1:-1]) + int(line[3])
    elif line[0].lower() == "sll":
        dec = op * 6 + rd * int(line[1][1:-1]) + rs * int(line[2][1:-1]) + shamt * int(line[3])
    elif line[0].lower() == "slt":
        dec = op * 7 + rd * int(line[1][1:-1]) + rs * int(line[2][1:-1]) + rt * int(line[3][1:])
    elif line[0].lower() == "mfhi":
        dec = op * 8 + rd * int(line[1][1:])
    elif line[0].lower() == "mflo":
        dec = op * 9 + rd * int(line[1][1:])
    elif line[0].lower() == "lw":
        word = line[2].split("(")
        dec = op * 10 + rd * int(line[1][1:-1]) + rs * int(word[1][1:-1]) + int(word[0])
    elif line[0].lower() == "sw":
        word = line[2].split("(")
        dec = op * 11 + rs * int(line[1][1:-1]) + rd * int(word[1][1:-1]) + int(word[0])
    elif line[0].lower() == "beq":
        dec = op * 12 + rs * int(line[1][1:-1]) + rt * int(line[2][1:-1]) + labels[line[3].lower()] - len(binary)
    elif line[0].lower() == "blez":
        dec = op * 12 + rs * int(line[1][1:-1]) + labels[line[3].lower()] - len(binary)
    elif line[0].lower() == "j":
        dec = op * 14 + labels[line[1].lower()]
    elif line[0].lower() == "adds":
        dec = op * 15 + rd * int(line[1][1:-1]) + rs * int(line[2][1:-1]) + rt * int(line[3][1:])
    else:
        print("Unknown operation on line", len(binary))
        exit()
    binary.append(hex(dec))

output = open(out, "w", encoding="utf-8")
output.write("v2.0 raw\n")
for machinecode in binary:
    machinecode = machinecode[2:]
    if len(machinecode) < 8:
        machinecode = (8 - len(machinecode)) * '0' + machinecode
    output.write(machinecode+"\n")
