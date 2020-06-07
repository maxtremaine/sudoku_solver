class Puzzle:
    """ Sudoku puzzle. """

    ROWS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    COLS = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    BOXES = ["b2", "e2", "h2", "b5", "e5", "h5", "b8", "e8", "h8"]

    def __init__(self, start):
        self.a1 = start[16]
        self.b1 = start[17]
        self.c1 = start[18]
        self.d1 = start[20]
        self.e1 = start[21]
        self.f1 = start[22]
        self.g1 = start[24]
        self.h1 = start[25]
        self.i1 = start[26]
        self.a2 = start[30]
        self.b2 = start[31]
        self.c2 = start[32]
        self.d2 = start[34]
        self.e2 = start[35]
        self.f2 = start[36]
        self.g2 = start[38]
        self.h2 = start[39]
        self.i2 = start[40]
        self.a3 = start[44]
        self.b3 = start[45]
        self.c3 = start[46]
        self.d3 = start[48]
        self.e3 = start[49]
        self.f3 = start[50]
        self.g3 = start[52]
        self.h3 = start[53]
        self.i3 = start[54]
        self.a4 = start[72]
        self.b4 = start[73]
        self.c4 = start[74]
        self.d4 = start[76]
        self.e4 = start[77]
        self.f4 = start[78]
        self.g4 = start[80]
        self.h4 = start[81]
        self.i4 = start[82]
        self.a5 = start[86]
        self.b5 = start[87]
        self.c5 = start[88]
        self.d5 = start[90]
        self.e5 = start[91]
        self.f5 = start[92]
        self.g5 = start[94]
        self.h5 = start[95]
        self.i5 = start[96]
        self.a6 = start[100]
        self.b6 = start[101]
        self.c6 = start[102]
        self.d6 = start[104]
        self.e6 = start[105]
        self.f6 = start[106]
        self.g6 = start[108]
        self.h6 = start[109]
        self.i6 = start[110]
        self.a7 = start[128]
        self.b7 = start[129]
        self.c7 = start[130]
        self.d7 = start[132]
        self.e7 = start[133]
        self.f7 = start[134]
        self.g7 = start[136]
        self.h7 = start[137]
        self.i7 = start[138]
        self.a8 = start[142]
        self.b8 = start[143]
        self.c8 = start[144]
        self.d8 = start[146]
        self.e8 = start[147]
        self.f8 = start[148]
        self.g8 = start[150]
        self.h8 = start[151]
        self.i8 = start[152]
        self.a9 = start[156]
        self.b9 = start[157]
        self.c9 = start[158]
        self.d9 = start[160]
        self.e9 = start[161]
        self.f9 = start[162]
        self.g9 = start[164]
        self.h9 = start[165]
        self.i9 = start[166]

    @classmethod
    def generate(cls, start):
        """ Turns a .sudoku file into a Puzzle object. """
        if len(start) != 167:
            raise Exception ("The .sudoku file is not formatted properly.")

        return cls(start)

    def get_row(self, n):
        rows = {
            1: [self.a1, self.b1, self.c1, self.d1, self.e1, self.f1, self.g1, self.h1, self.i1],
            2: [self.a2, self.b2, self.c2, self.d2, self.e2, self.f2, self.g2, self.h2, self.i2],
            3: [self.a3, self.b3, self.c3, self.d3, self.e3, self.f3, self.g3, self.h3, self.i3],
            4: [self.a4, self.b4, self.c4, self.d4, self.e4, self.f4, self.g4, self.h4, self.i4],
            5: [self.a5, self.b5, self.c5, self.d5, self.e5, self.f5, self.g5, self.h5, self.i5],
            6: [self.a6, self.b6, self.c6, self.d6, self.e6, self.f6, self.g6, self.h6, self.i6],
            7: [self.a7, self.b7, self.c7, self.d7, self.e7, self.f7, self.g7, self.h7, self.i7],
            8: [self.a8, self.b8, self.c8, self.d8, self.e8, self.f8, self.g8, self.h8, self.i8],
            9: [self.a9, self.b9, self.c9, self.d9, self.e9, self.f9, self.g9, self.h9, self.i9]
        }
        return rows[n]

    def get_col(self, a):
        cols = {
            "a": [self.a1, self.a2, self.a3, self.a4, self.a5, self.a6, self.a7, self.a8, self.a9],
            "b": [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9],
            "c": [self.c1, self.c2, self.c3, self.c4, self.c5, self.c6, self.c7, self.c8, self.c9],
            "d": [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9],
            "e": [self.e1, self.e2, self.e3, self.e4, self.e5, self.e6, self.e7, self.e8, self.e9],
            "f": [self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8, self.f9],
            "g": [self.g1, self.g2, self.g3, self.g4, self.g5, self.g6, self.g7, self.g8, self.g9],
            "h": [self.h1, self.h2, self.h3, self.h4, self.h5, self.h6, self.h7, self.h8, self.h9],
            "i": [self.i1, self.i2, self.i3, self.i4, self.i5, self.i6, self.i7, self.i8, self.i9]
        }
        return cols[a]
        
    def get_box(self, c):
        boxes = {
            "b2": [self.a1, self.b1, self.c1, self.a2, self.b2, self.c2, self.a3, self.b3, self.c3],
            "e2": [self.d1, self.e1, self.f1, self.d2, self.e2, self.f2, self.d3, self.e3, self.f3],
            "h2": [self.g1, self.h1, self.i1, self.g2, self.h2, self.i2, self.g3, self.h3, self.i3],
            "b5": [self.a4, self.b4, self.c4, self.a5, self.b5, self.c5, self.a6, self.b6, self.c6],
            "e5": [self.d4, self.e4, self.f4, self.d5, self.e5, self.f5, self.d6, self.e6, self.f6],
            "h5": [self.g4, self.h4, self.i4, self.g5, self.h5, self.i5, self.g6, self.h6, self.i6],
            "b8": [self.a7, self.b7, self.c7, self.a8, self.b8, self.c8, self.a9, self.b9, self.c9],
            "e8": [self.d7, self.e7, self.f7, self.d8, self.e8, self.f8, self.d9, self.e9, self.f9],
            "h8": [self.g7, self.h7, self.i7, self.g8, self.h8, self.i8, self.g9, self.h9, self.i9]
        }
        return boxes[c]

    def check_puzzle(self):
        for row in self.ROWS:
            if check_group(self.get_row(row)) == False:
                return False
        
        for col in self.COLS:
            if check_group(self.get_col(col)) == False:
                return False

        for box in self.BOXES:
            if check_group(self.get_box(box)) == False:
                return False

        return True


def check_group(group):
    """ Return False if there are any doubles in a list. """

    if len(group) != 9:
        raise Exception("The group size renders it invalid.")

    check_scope = set()

    for num in group:
        num = str(num)

        if num != "_":
            if num in check_scope:
                return False
            else:
                check_scope.add(num)
    
    return True