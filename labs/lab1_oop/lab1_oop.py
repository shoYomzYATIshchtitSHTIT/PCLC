import sys
import math

class EquationSolver:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        D = self.discriminant()
        if D < 0:
            return []
        elif D == 0:
            root = -self.b / (2 * self.a)
            return [root] if root >= 0 else []
        else:
            sqD = math.sqrt(D)
            root1 = (-self.b + sqD) / (2 * self.a)
            root2 = (-self.b - sqD) / (2 * self.a)
            return [root1, root2] if root1 >= 0 and root2 >= 0 else [root for root in [root1, root2] if root >= 0]

    def find_biquadratic_roots(self):
        quadratic_roots = self.solve()
        biquadratic_roots = []
        for root in quadratic_roots:
            if root > 0:
                biquadratic_roots.append(math.sqrt(root))
                biquadratic_roots.append(-math.sqrt(root))
            elif root == 0:
                biquadratic_roots.append(0)
        return biquadratic_roots

def get_coef(index, prompt):
    while True:
        try:
            coef = float(sys.argv[index])
            return coef
        except (IndexError, ValueError):
            try:
                coef = float(input(prompt))
                return coef
            except ValueError:
                print("Некорректный ввод, попробуйте снова.")

def main():
    a = get_coef(1, 'Введите коэффициент А: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')

    solver = EquationSolver(a, b, c)
    roots = solver.find_biquadratic_roots()

    if not roots:
        print("Действительных корней нет.")
    else:
        print(f"Найдены корни: {', '.join(map(str, roots))}")

if __name__ == "__main__":
    main()
