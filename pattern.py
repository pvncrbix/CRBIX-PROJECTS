def pyramid_pattern(rows):
    for i in range(rows):
        print(" ", rows-i-1)
        for j in range(i+1):

            print(chr(65+j),end=" ")

        for k in range(i-1,-1,-1):


            print(chr(65+j), end=" ")
    print()
n=7
pyramid_pattern(n)