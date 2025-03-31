from sympy import symbols, Eq, solve

x, y, z = symbols('x y z')
eq1 = Eq(2*x + y - z, 5)
eq2 = Eq(3*x - 2*y + z, -3)
eq3 = Eq(x + y + z, 4)

sol = solve((eq1, eq2, eq3), (x, y, z))

print(sol[x], sol[y], sol[z])
