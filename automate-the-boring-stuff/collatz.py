def collatz(number):    

    if number % 2 == 0:
        print(number // 2)
        return number // 2
        
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

try:
    n = int(input('number: '))
except ValueError:
          print("Please enter a valid INTEGER.")

n = int(input('number: '))

while n != 1:
    n = collatz(int(n))

    