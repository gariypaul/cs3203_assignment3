def calculate_sum(numbers):
    """Calculates the sum of the array """
    sum = 0
    for number in numbers:
        sum=sum+number
    return sum

def calc_product(numbers):
    """Calculates the sum of the array """ 
    prod=0
    for number in numbers:
        if prod ==0:
            prod += number
        else:
            prod *= number
    return prodg

def reverse_list(numbers):
    """Returns the reverse of the list"""
    reversed = numbers[::-1]
    return reversed


def main():
   numbersstr = input("Enter your numbers seperated by a comma:")
   numbers = numbersstr.split(',')
   intlist = [int(num) for num in numbers]

   print("The product of the numbers is ",calc_product(intlist))
   print("The sum of the numbers is ", calculate_sum(intlist))

if __name__ == '__main__':
    main()