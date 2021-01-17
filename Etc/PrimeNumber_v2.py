# 순차적으로 판별하는 것은 시간 너무 오래 걸림
# 따라서 제급근까지만 판별하면 된다
import math

def is_prime_number(x):
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
        else:
            return True

print(is_prime_number(4))
print(is_prime_number(13))
