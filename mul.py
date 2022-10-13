import numpy as np
import os


def mul(files):
    for file in files:
        if not os.path.exists(file):
            print(f"Can't find file '{file}'")
            return

    f = open(files[0], 'r')
    data_1 = np.loadtxt(f, skiprows=1)
    f.close()

    f = open(files[1], 'r')
    data_2 = np.loadtxt(f, skiprows=1)
    f.close()

    f = open(files[2], 'r')
    res = np.loadtxt(f)
    f.close()

    res_test = np.dot(data_1, data_2)
    print(res_test)
    print(np.array_equal(res, res_test))


if __name__ == '__main__':
    mul(['matrix1.txt', 'matrix2.txt', 'res.txt'])

