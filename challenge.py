a=1000
b=999
final=0
afinal=0
bfinal=0
while(a>99):

    a=a-1

    while(b>99):

        product = a * b
        if (list(str(product))==list(reversed(str(product)))):

            if(product>final):
                final = product
                afinal=a
                bfinal=b




        b=b-1

    b=999


print("we found it",final)
print("a is", afinal)
print("a is", bfinal)










