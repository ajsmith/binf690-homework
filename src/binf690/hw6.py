"""Homework 6

Alexander Smith
BINF690
George Mason University
Fall 2020

"""

from binf690.regression import LinearRegression


class Homework6A:

    def __init__(self, X=None, Y=None):
        self.X = X or [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.Y = Y or [1, 1.5, 2, 3, 4, 5, 8, 10, 13]
        self.reg = LinearRegression(self.X, self.Y)

    def print_solution(self):
        print('X:', ' '.join(f'{x:2.1f}' for x in self.X))
        print('Y:', ' '.join(f'{y:2.1f}' for y in self.Y))
        print('Linear Regression:')
        print(self.reg)

    def plot(self):
        self.reg.plot(filename='asmitl-hw6a.png')


def hw6a():
    hw = Homework6A()
    hw.print_solution()


def hw6a_plot():
    hw = Homework6A()
    hw.plot()


def hw6b():
    not_yet


if __name__ == '__main__':
    hw6a_plot()
#    hw6b()
