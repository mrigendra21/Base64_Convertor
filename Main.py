# This function returns the Base64 encoded value for the supplied binary string.
def returnCode(data):
    if data == "000000":
        return 'A'
    if data == "000001":
        return 'B'
    if data == "000010":
        return 'C'
    if data == "000011":
        return 'D'
    if data == "000100":
        return 'E'
    if data == "000101":
        return 'F'
    if data == "000110":
        return 'G'
    if data == "000111":
        return 'H'

    if data == "001000":
        return 'I'
    if data == "001001":
        return 'J'
    if data == "001010":
        return 'K'
    if data == "001011":
        return 'L'
    if data == "001100":
        return 'M'
    if data == "001101":
        return 'N'
    if data == "001110":
        return 'O'
    if data == "001111":
        return 'P'

    if data == "010000":
        return 'Q'
    if data == "010001":
        return 'R'
    if data == "010010":
        return 'S'
    if data == "010011":
        return 'T'
    if data == "010100":
        return 'U'
    if data == "010101":
        return 'V'
    if data == "010110":
        return 'W'
    if data == "010111":
        return 'X'

    if data == "011000":
        return 'Y'
    if data == "011001":
        return 'Z'
    if data == "011010":
        return 'a'
    if data == "011011":
        return 'b'
    if data == "011100":
        return 'c'
    if data == "011101":
        return 'd'
    if data == "011110":
        return 'e'
    if data == "011111":
        return 'f'

    if data == "100000":
        return 'g'
    if data == "100001":
        return 'h'
    if data == "100010":
        return 'i'
    if data == "100011":
        return 'j'
    if data == "100100":
        return 'k'
    if data == "100101":
        return 'l'
    if data == "100110":
        return 'm'
    if data == "100111":
        return 'n'

    if data == "101000":
        return 'o'
    if data == "101001":
        return 'p'
    if data == "101010":
        return 'q'
    if data == "101011":
        return 'r'
    if data == "101100":
        return 's'
    if data == "101101":
        return 't'
    if data == "101110":
        return 'u'
    if data == "101111":
        return 'v'

    if data == "110000":
        return 'w'
    if data == "110001":
        return 'x'
    if data == "110010":
        return 'y'
    if data == "110011":
        return 'z'
    if data == "110100":
        return '0'
    if data == "110101":
        return '1'
    if data == "110110":
        return '2'
    if data == "110111":
        return '3'

    if data == "111000":
        return '4'
    if data == "111001":
        return '5'
    if data == "111010":
        return '6'
    if data == "111011":
        return '7'
    if data == "111100":
        return '8'
    if data == "111101":
        return '9'
    if data == "111110":
        return '+'
    if data == "111111":
        return '/'

# This function accept the binary string and pad it with "0" if required to make it a 6 bit long binary string. 
# Once the binary string is padded appropriately, then it calls the returnCode function to get the encoded value for the string.

def base64(data):
    if len(data) == 1:
        return returnCode("00000"+data)
    elif len(data) == 2:
        return returnCode("0000"+data)
    elif len(data) == 3:
        return returnCode("000"+data)
    elif len(data) == 4:
        return returnCode("00"+data)
    elif len(data) == 5:
        return returnCode("0"+data)
    else:
        return returnCode(data)


# Open a running config file, read the data and close it.
file = open("Running_Config.txt",'r')
t = file.read()
file.close()

# Converting a character into binary. Since the returned binary string depends on the decimal value of the character, hence the size of the binary could be less than 8.
# So we need to ensure that each character is being represented by 8 bit binary, hence padding is necessary.
absolutebin = ""
for i in t:
    mybin = format(ord(i), 'b')
    stlen = len(mybin)
    if stlen == 7:
        temp = "0"+ mybin
    if stlen == 6:
        temp = "00"+mybin
    if stlen == 5:
        temp = "000"+mybin
    if stlen == 4:
        temp = "0000"+mybin
    if stlen == 3:
        temp = "00000"+mybin
    if stlen == 2:
        temp = "000000"+mybin
    if stlen == 1:
        temp = "0000000"+mybin
    absolutebin = absolutebin + temp

# absolutebin is a complete binary string for the entire config. Now we need to write a code to covert this binary into base64 encoded.

encoded = ""
for b in range(0, len(absolutebin), 6):
    temp_Data = absolutebin[b:b + 6]
    basesix4 = base64(temp_Data)
    encoded = encoded + basesix4
print(encoded)

