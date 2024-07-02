def main():

    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
    num5 = int(input("Enter the fifth number: "))
    numbers = [num1,num2,num3,num4,num5]
    for i  in range(0,5):
        if numbers[i] >= numbers[0] and numbers[1] and numbers[2] and numbers[3] and numbers[4]:
            maxval = numbers[i]
        elif numbers[i] <= numbers[0] and numbers[1] and numbers[2] and numbers[3] and numbers[4]:
            minval = numbers[i]

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
