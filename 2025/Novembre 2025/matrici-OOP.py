from random import randint


class MatriceCasuale:
    def __init__(self, row: int, col: int, minimum: int, maximum: int):
        self.row = row
        self.col = col
        self.minimum = minimum
        self.maximum = maximum
        self.matrix = self.creaMatrice()  # assegno il valore restituito dalla funzione al metodo .matrix

    def __getitem__(self, index):
        """
            Permette di restituire un valore di un oggetto quando viene chiamato l'indice con [].
        """
        return self.matrix[index]

    def creaMatrice(self):
        matrix = []
        for r in range(self.row):
            lista = []
            for c in range(self.col):
                lista.append(randint(self.minimum, self.maximum))
            matrix.append(lista)
        return matrix

    def __str__(self):
        stringa = ''
        for r in range(self.row):
            for c in range(self.col):
                if self[r][c] < 10:
                    stringa += '   ' + str(self[r][c])
                elif 10 <= self[r][c] < 100:
                    stringa += '  ' + str(self[r][c])
                else:
                    stringa += ' ' + str(self[r][c])
            stringa += '\n'
        return stringa


class MatriceSimmetrica(MatriceCasuale):
    def __init__(self, row: int, col: int, minimum: int, maximum: int, separator=0):
        self.separator = separator
        super().__init__(row, col, minimum, maximum)
        self.matrix = self.creaMatrice()

    def creaMatrice(self):
        matrix = [[0] * self.col for _ in range(self.row)]
        for r in range(self.row):
            for c in range(r, self.col):
                x = randint(self.minimum, self.maximum)
                matrix[r][c] = x
                matrix[c][r] = x
                if r == c:
                    matrix[r][c] = self.separator
        return matrix


class MatricePerimetrale(MatriceCasuale):
    def __init__(self, row: int, col: int, minimum: int, maximum: int, border: int = 0):
        self.border = border
        super().__init__(row, col, minimum, maximum)
        self.matrix = self.creaMatrice()

    def creaMatrice(self):
        matrix = []
        for r in range(self.row):
            lista = []
            for c in range(self.col):
                if r in (0, self.row - 1) or c in (0, self.col - 1):
                    lista.append(self.border)
                else:
                    lista.append(randint(self.minimum, self.maximum))
            matrix.append(lista)
        return matrix


class MatriceIsolare(MatriceCasuale):
    def __init__(self, row: int, col: int, minimum: int, maximum: int):
        super().__init__(row, col, minimum, maximum)
        self.matrix = self.creaMatrice()

    def creaMatrice(self):
        matrix = []
        for r in range(self.row):
            lista = []
            for c in range(self.col):
                lista.append(randint(self.minimum, self.maximum))
            matrix.append(lista)
        return matrix


LENR = 9
LENC = 9
minrange = 1
maxrange = 1000

print(f'Matrice casuale {LENR}x{LENC}: ')
casuale = MatriceCasuale(LENR, LENC, minrange, maxrange)
print(casuale)

asse = 1
print(f'Matrice simmetrica {LENR}x{LENC}: ')
simmetrica = MatriceSimmetrica(LENR, LENC, minrange, maxrange, asse)
print(simmetrica)

perimetro = 1
print(f'Matrice perimetrale {LENR}x{LENC}: ')
perimetrale = MatricePerimetrale(LENR, LENC, minrange, maxrange, perimetro)
print(perimetrale)

print(f'Matrice isolare {LENR}x{LENC}: ')
isolare = MatriceIsolare(LENR, LENC, minrange, maxrange)
print(isolare)
