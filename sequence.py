#Step 1: The user inputs the length of the sequence.
#Step 2: Make the sequence 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
#Step 3: The program prints the first n numbers in the sequence: 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …

n = int(input("Enter the length of the sequence: ")) # Do not change this line

x_int = 0
a_int = 0
b_int = 0
c_int = 0

for i in range(1, n+1):
    if i == 1:
        a_int = i
        print(a_int)
    elif i == 2:
        b_int = i
        print(b_int)
    elif i == 3:
        c_int = i
        print(c_int)
    else:
        x_int = a_int + b_int + c_int
        print(x_int)
        
        a_int = b_int
        b_int = c_int
        c_int = x_int