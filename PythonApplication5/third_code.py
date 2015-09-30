def decode_morse(self):

        morse_code = {"iI": "A", "Iiii": "B", "IiIi": "C", "i": "E", "iiIi": "F", "IIi": "G", "iiii": "H", "ii": "I", "iIII": "J", "IiI": "K", "iIii":"L", "II": "M", "Ii": "N", "III": "O", "iIIi": "P", "IIiI": "Q", "iIi": "R", "iii": "S", "I": "T", "iiI": "U", "iiiI": "V", "iII": "W", "IiiI": "X", "IiII": "Y", "IIii": "Z"}

        print(morse_code.get(self))

        return self