from GroupOperations import find_generator, get_order, set_curve, ec_add
from ModularMath import modular_inverse

set_curve(1, 0, 11)
x = (9, 1)
a = ec_add(x, x)
print(a)
for i in range(11):
    print(ec_add(a, x))
    a = ec_add(a, x)