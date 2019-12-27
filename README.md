# 16-bit-Single-Cycle-Processor

Designed a single cycle MIPS-alike processor with 32-bit word and 16-bit data sizes using [Logisim][1] for COMP303 - Computer Architecture course taught in [Koç University][2]

## Instruction set

| Instruction       | Operation                   | Description                                                                           |
| ----------------- | --------------------------- | ------------------------------------------------------------------------------------- |
| add rd, rs, rt    | rd = rs + rt                | rd = destination, rs, rt = source                                                     |
| sub rd, rs, rt    | rd = rs – rt                | rd = destination, rs, rt = source                                                     |
| mult rs, rt       | hi;lo = rs*rt               | hi, lo: two 16-bit registers in multiplier unit to store 32-bit multiplication result |
| and rd, rs, rt    | rd = rs & rt                | rd = destination, rs, rt = source                                                     |
| or rd, rs, rt     | rd = rs \| rt               | rd = destination, rs, rt = source                                                     |
| addi rd, rs, I    | rd = rs + I                 | rd = destination, rs = source, I = 16-bit immediate value                             |
| sll rd, rs, shamt | rd = rs << shamt            | rd = destination, rs = source, shamt = shift amount                                   |
| slt rd, rs, rt    | rd = (rs < rt)              | rd = 1 if rs < rt, otherwise rd = 0                                                   |
| mfhi rd           | rd = hi                     | Load hi from multiplier unit into register rd                                         |
| mflo rd           | rd = lo                     | Load lo from multiplier unit into register rd                                         |
| lw rd, i(rs)      | rd = rs[i]                  | rd = destination, rs = base address, i = offset                                       |
| sw rs, i(rd)      | rd[i] = rs                  | rd = base address, rs = source, i = offset                                            |
| beq rs, rt, label | if (rs == rt) jump to label | rs, rt = registers to compare, label = label to jump to                               |
| blez rs, label    | if (rs <= 0) jump to label  | rs = register to compare, label = label to jump to                                    |
| j label           | Jump to label               | label = label to jump to                                                              |
| adds rd, rs, I    | rd = rs + I                 | rd = address, rs = source, I = 16-bit immediate value                                 |

## Assembler

Coded an assembler in python that is capable of handling labels and comments.

### Usage

```
python Assembler.py input [output]
```

### Example

```
addi $1, $0, 0         # address of array a in RAM
addi $2, $0, 0         # loop variable i
addi $3, $0, 5         # loop contant 5
loop: beq $2, $3, exit # if i == 6 goto exit
add $4, $1, $2         # address of a[i]
lw $5, 0($4)           # a[i]
adds $4, $5, 10        # a[i] = a[i] + 10
addi $2, $2, 1         # i = i + 1
j loop
exit: addi $9, $0, 1  # Does not serve any purpose
```

[1]: http://www.cburch.com/logisim
[2]: https://www.ku.edu.tr
