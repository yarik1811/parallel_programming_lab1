import random


def generate(a: int, b: int, file: str):
	"""
	Запись матриц указанного размера [a; b] в файл (file)
	:param a: Количество строк
	:param b: Количество столбцов
	:param file: Имя файла
	:return: none
	"""

	with open(file, 'w') as f:
		f.write(f'{a} {b}\n')
		for i in range(a):
			for j in range(b):
				f.write(f'{random.randint(-10, 10)} ')
			f.write('\n')


if __name__ == '__main__':
	generate(1000, 1000, 'matrix1.txt')
	generate(1000, 1000, 'matrix2.txt')
