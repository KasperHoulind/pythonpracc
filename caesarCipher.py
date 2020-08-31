message = input("Write a message to encrypt it: ")

key = 3

#SYMBOLS=ascii(message)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !.'

translated=''

for s in message:
    if s in SYMBOLS:
        sIndex = SYMBOLS.find(s)
        translateIndex = sIndex + key

        #if the translate index exceeds the length of the symbols this should handel it. ie it loops around the SYMBOLS
        if translateIndex <= len(SYMBOLS):
            translateIndex = translateIndex-len(SYMBOLS)
        elif translateIndex < 0:
            translateIndex = translateIndex+len(SYMBOLS)

        translated = translated + SYMBOLS[translateIndex]
    else:
        translated = translated + s
print(translated)