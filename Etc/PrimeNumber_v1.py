# 주어진 수보다 작은 수를 순차적으로 탐색하면서 소수인지 아닌지 판별하기

def is_prime_number(x):
    for i in range(2,x):
        if x%i==0:
            return False
        else:
            return True
print(is_prime_number(4))
print(is_prime_number(7))
