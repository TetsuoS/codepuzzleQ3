morse_code = {"iI": "A", "Iiii": "B", "IiIi": "C", "i": "E", "iiIi": "F", "IIi": "G", "iiii": "H", "ii": "I", "iIII": "J", "IiI": "K", "iIii":"L", "II": "M", "Ii": "N", "III": "O", "iIIi": "P", "IIiI": "Q", "iIi": "R", "iii": "S", "I": "T", "iiI": "U", "iiiI": "V", "iII": "W", "IiiI": "X", "IiII": "Y", "IIii": "Z"}


def decode_morse(self):

        ans1 = self.split(" ")
        
        ans2 = filter(pre_filter, ans1)

        ans3 = map(pre_map, ans2)

        return str(ans3)

def pre_filter(x):
    return x != ""


def pre_map(x):
    return morse_code[x]