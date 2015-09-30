class Bars:

    def __init__(self, bar):
        self.bar = bar

    def next(self):
        original_list = list(self.bar)
        new_list = list(original_list)
        for i in range(len(original_list)):
            new_list[i] = ' '

        for i in range(len(original_list)):
            c0 = original_list[i-1]
            c1 = original_list[i]
            c2 = original_list[(i+1)%len(original_list)]


            table = [{ " ":" ", "i":"T", "T":"i", "I":"I" },
                     { " ":"i", "i":"I", "T":" ", "I":"T" }]


            count = 0
            if is_black(c0):
                 count=count+1
            if is_black(c2):
                 count=count+1

            new_list[i] = table[count%2][c1]
 

        self.bar = "".join(new_list)

        return str(self.bar)


    def __str__(self):
        return str(self.bar)


    def __setitem__(self, key, value):
        original_list = list(self.bar)
        original_list[key] = value
        self.bar = "".join(original_list)

        return str(self)


    def __len__(self):
        return len(self.bar)

    def is_black(self, c):
        return c == 'i' or c == 'I' 