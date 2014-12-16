from encryption import GroupOperations as group

#EC.set_curve( 5, 2, 23)

#G = [(17,3), (0,5), (8,5), (15, 5), (18,6), (6,8), (7,9), (1,10), (11,10), (20,11), (20, 12), (1,13), (11,13),  (7,14), (6,15), (18,17), (0,18), (8,18), (15,18), (17,20)]
from encryption.ModularMath import is_prime

print("----------------------------------------------------")
print('{0:^30}|{1:^7}|{2:^12}'.format('Curve Parameters', 'Order', 'Generator'))
print("----------------------------------------------------")
for p in range(5, 102):
    if is_prime(p):
        for b in range(p):
            for a in range(p):
                if (4 * (a**3) + 27 * (b**2)) % p != 0:
                    order = group.get_order(a, b, p)
                    group.set_curve(a, b, p)
                    generator = group.find_generator(a, b, p)
                    if generator == (-1, -1):
                        generator = "Not Cyclic"
                    #curve = "y^2 = x^3 + {0:d}x + {1:d}  mod {2:d}".format(a, b, p)
                    curve = "a = {0:<3d}  b = {1:<3d}  p = {2:<3d}".format(a, b, p)
                    print("{0:^30s}| {1:<5d} |{2!s:^12}".format(curve, order, generator))


