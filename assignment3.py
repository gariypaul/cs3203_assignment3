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
    return prod
