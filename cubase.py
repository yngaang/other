import sympy as sp

# Задаем исходную функцию
def target_function(x):
    return x**2


a = -10
b = 10
delta = 0.001
new_x = 2*a
old_x = a
# Создаем символьную переменную
x_sym = sp.symbols('x')

# Вычисляем производную функции
derivative = sp.diff(target_function(x_sym), x_sym)
print("Производная: ", derivative)

while abs(old_x - new_x) > delta:
    old_x = new_x
    f_a = target_function(a) #значения функции
    f_b = target_function(b)
    fd_a = derivative.subs(x_sym, a) #значения производной
    fd_b = derivative.subs(x_sym, b)

    print("f(a) =", f_a, " f(b) =", f_b, " f'(a) =", fd_a,  " f'(b) =", fd_b)

    z = fd_a + fd_b + 3*(f_a - f_b)/(b - a)

    print("z=", z)

    w = (z**2 - fd_a*fd_b)**(1/2) 

    print("w=", w)

    gamma = (z + w - fd_a) / (fd_b - fd_a + 2*w)

    print("gamma =", gamma)

    if gamma <= 1 and gamma >= 0 : 
        new_x = a + gamma*(b - a)
    if gamma < 0:
        new_x = a
    if gamma > 1:
        new_x = b

    if derivative.subs(x_sym, new_x) > 0 :
        b = new_x
    else:
        a = new_x
            
    print("new_x =", new_x, "\n")

