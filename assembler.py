op = 67108864  # 2^26
rs = 2097152  # 2^21
rt = 65536  # 2^16
rd = 2048  # 2^11
shamt = 64  # 2^6

lines = []
print("Press enter without any text to end your input")
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

labels = {}
binary = []
for line in lines:
    words = line.split(" ")
    if words[0].endswith(":"):
        labels[words.pop(0)[:-1].lower()] = len(binary)
    dec = 0
    if words[0].lower() == "add":
        dec = op * 0 + rd * int(words[1][1:-1]) + rs * int(words[2][1:-1]) + rt * int(words[3][1:])
    elif words[0].lower() == "sub":
        dec = op * 1 + rd * int(words[1][1:-1]) + rs * int(words[2][1:-1]) + rt * int(words[3][1:])
    elif words[0].lower() == "mult":
        dec = op * 2 + rs * int(words[2][1:-1]) + rt * int(words[3][1:])
    elif words[0].lower() == "and":
        dec = op * 3 + rd * int(words[1][1:-1]) + rs * int(words[2][1:-1]) + rt * int(words[3][1:])
    elif words[0].lower() == "or":
        dec = op * 4 + rd * int(words[1][1:-1]) + rs * int(words[2][1:-1]) + rt * int(words[3][1:])
    elif words[0].lower() == "addi":
        dec = op * 5 + rd * int(words[1][1:-1]) + rs * int(words[2][1:-1]) + int(words[3])
    elif words[0].lower() == "sll":
        dec = op * 6 + rd * int(words[1][1:-1]) + rs * int(words[2][1:-1]) + shamt * int(words[3])
    elif words[0].lower() == "slt":
        dec = op * 7 + rd * int(words[1][1:-1]) + rs * int(words[2][1:-1]) + rt * int(words[3][1:])
    elif words[0].lower() == "mfhi":
        dec = op * 8 + rd * int(words[1][1:])
    elif words[0].lower() == "mflo":
        dec = op * 9 + rd * int(words[1][1:])
    elif words[0].lower() == "lw":
        word = words[2].split("(")
        dec = op * 10 + rd * int(words[1][1:-1]) + rs * int(word[1][1:-1]) + int(word[0])
    elif words[0].lower() == "sw":
        word = words[2].split("(")
        dec = op * 11 + rs * int(words[1][1:-1]) + rd * int(word[1][1:-1]) + int(word[0])
    elif words[0].lower() == "beq":
        dec = op * 12 + rs * int(words[1][1:-1]) + rt * int(words[2][1:-1]) + labels[words[3].lower()]
    elif words[0].lower() == "blez":
        dec = op * 12 + rs * int(words[1][1:-1]) + labels[words[3].lower()]
    elif words[0].lower() == "j":
        dec = op * 14 + labels[words[1].lower()]
    elif words[0].lower() == "adds":
        dec = op * 15 + rd * int(words[1][1:-1]) + rs * int(words[2][1:-1]) + rt * int(words[3][1:])
    binary.append(hex(dec))

for machinecode in binary:
    machinecode = machinecode[2:]
    if len(machinecode) < 8:
        machinecode = (8-len(machinecode))*'0'+machinecode
    print(machinecode)
