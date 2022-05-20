def prime_num(start, end):
    for num in range(start, end):
        if num  > 1:
            for i in range(2, num):
                if num% i == 0:
                    print(f'{num} ------->is not a prime')
                    break
            else:
                print(f'{num} ----------->is prime')
prime_num(1,500)