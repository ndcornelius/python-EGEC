import ECGroupOperations as EC

EC.set_curve( 5, 2, 23)

G = [(17,3), (0,5), (8,5), (15, 5), (18,6), (6,8), (7,9), (1,10), (11,10), (20,11), (20, 12), (1,13), (11,13),  (7,14), (6,15), (18,17), (0,18), (8,18), (15,18), (17,20)]

for x in G: 
    for y in G:

        if y[1] >= x[1] and y[0] >= x[0]:

            z = EC.ec_add(x[0], x[1], y[0], y[1])

            if z in G:
                t = " ----> TRUE"
            else:
                t = " ----> FALSE"

            #if x[0] is 'e' and x[1] is 'e':

            print ("(" + str(x[0]) + ", " + str(x[1]) + ")" + " + " + "(" + str(y[0]) + ", " + str(y[1]) + ") = (" + str(z[0]) + ", "+ str(z[1]) + ")" + t + "\n")
