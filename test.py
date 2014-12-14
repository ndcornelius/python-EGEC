import GroupOperations as EC

#EC.set_curve( 5, 2, 23)

#G = [(17,3), (0,5), (8,5), (15, 5), (18,6), (6,8), (7,9), (1,10), (11,10), (20,11), (20, 12), (1,13), (11,13),  (7,14), (6,15), (18,17), (0,18), (8,18), (15,18), (17,20)]
from ModularMath import isprime

print( '{0:^30} {1:^10} {2:>12}'.format('Curve', 'Group Order', 'Generator'))
for i in range(5, 101):
    if isprime(i):
        for j in range(0, i):
            for k in range(0, i):
                if (4 * (k**3) + 27 * (j**2)) % i != 0:
                    #try:
                    order = EC.num_points(k, j, i)
                    EC.set_curve(k, j, i)
                    generator = EC.find_generator(k, j, i)
                    print(  "y^2 = x^3 + {0:d}x + {1:d}  mod {2:d} {3:10d} {4:>12}".format(k, j, i, order, generator))
                    #except( Exception):
                     #   print( "Curve y^2 = x^3 +%dx + %d mod %d does not form a group" % (k, j, i))
              

