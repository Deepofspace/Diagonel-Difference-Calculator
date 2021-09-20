from random import randint


# Rastgele bir kare n x n matrisi oluşturmak


def olusuturMatrix(matrix, n):
    for satir in range(0, n):
        matrix.append([])
        for sutun in range(0, n):
            value = randint(0, 99)
            matrix[satir].append(value)


# Bir kare matrisi 2B  olarak görüntüleme


def gosterMatrix(matrix):
    n = len(matrix)
    for satir in range(0, n):
        res = "| "
        for sutun in range(0, n):
            if matrix[satir][sutun] < 10:
                res = res + str(matrix[satir][sutun]) + "| "
            else:
                res = res + str(matrix[satir][sutun]) + "| "
        print(res)


matrix = []


n = int(input("Kare matrisinizin n boyutunu girin. : "))
olusuturMatrix(matrix, n)
gosterMatrix(matrix)


def difference(matrix, n):

    # diagonellierin toplamı
    dia1 = 0
    dia2 = 0

    for i in range(0, n):
        dia1 = dia1 + matrix[i][i]
        dia2 = dia2 + matrix[i][n - i - 1]

    # toplamların mutlak farkı
    return abs(dia1 - dia2)


def toplamKose(mtx):

    x = len(mtx)
    y = len(mtx[0])

    # print("left top corner :", matrix[0][0])
    # print("right top corner :", matrix[0][y-1])
    # print("left bottom corner :", matrix[x-1][0])
    # print("right bottom corner :", matrix[x-1][y-1])

    koselerinToplami = (mtx[0][0]+mtx[0][y-1] +
                        mtx[x-1][0]+mtx[x-1][y-1])
    print("Koselerdeki sayıların toplamı : ", koselerinToplami)


print(f"Diagonel Farkı : {difference(matrix, n)}")
toplamKose(matrix)
