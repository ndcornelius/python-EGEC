from encryption import GroupOperations as Group
from encryption.ModularMath import is_prime

user_input, a, b, p = 0, 0, 0, 0

t = False
while not t:

    print("Enter '1' to find properties of a specific curve.")
    print("Enter '2' to find properties of all curves with prime 5 <= p <= 101.")
    print("(Warning: option 2 may take several minutes.)")
    user_input = input("Please enter your choice: ")
    try:
        user_input = int(user_input)
        if user_input == 1 or user_input == 2:
            t = True
        else:
            print("Please enter '1' or '2'.")
    except ValueError:
        print("Please enter '1' or '2'.")

if user_input == 1:
    t = False
    while not t:
        p = input("Enter prime p > 5 for F[p]: ")
        try:
            p = int(p)
            if not is_prime(p):
                print("Please enter a prime number.")
            else:
                t = True
        except ValueError:
            print("Please enter an integer.")

    t = False
    while not t:
        a = input("Enter curve coefficient 'a': ")
        try:
            a = int(a)
            a = a % p
            t = True
        except ValueError:
            print("Please enter an integer.")

    t = False
    while not t:
        b = input("Enter curve coefficient 'b': ")
        try:
            b = int(b)
            b = b % p
            t = True
        except ValueError:
            print("Please enter an integer.")

    if (4 * (a**3) + 27 * (b**2)) % p != 0:
        print("----------------------------------------------------")
        print('{0:^30}|{1:^7}|{2:^12}'.format('Curve Parameters', 'Order', 'Generator'))
        print("----------------------------------------------------")
        order = Group.get_order(a, b, p)
        Group.set_curve(a, b, p)
        generator = Group.find_generator(a, b, p)
        if generator == (-1, -1):
            generator = "Not Cyclic"
        #  curve = "y^2 = x^3 + {0:d}x + {1:d}  mod {2:d}".format(a, b, p)
        curve = "a = {0:<3d}  b = {1:<3d}  p = {2:<3d}".format(a, b, p)
        print("{0:^30s}| {1:<5d} |{2!s:^12}".format(curve, order, generator))

else:

    print("----------------------------------------------------")
    print('{0:^30}|{1:^7}|{2:^12}'.format('Curve Parameters', 'Order', 'Generator'))
    print("----------------------------------------------------")
    for p in range(5, 102):
        if is_prime(p):
            for b in range(p):
                for a in range(p):
                    if (4 * (a**3) + 27 * (b**2)) % p != 0:
                        order = Group.get_order(a, b, p)
                        Group.set_curve(a, b, p)
                        generator = Group.find_generator(a, b, p)
                        if generator == (-1, -1):
                            generator = "Not Cyclic"
                        #  curve = "y^2 = x^3 + {0:d}x + {1:d}  mod {2:d}".format(a, b, p)
                        curve = "a = {0:<3d}  b = {1:<3d}  p = {2:<3d}".format(a, b, p)
                        print("{0:^30s}| {1:<5d} |{2!s:^12}".format(curve, order, generator))


