import random
def generate_number(n):
    rnd = [str(random.randint(1, 9))]
    for number in range(n - 1):
        rnd.append(str(random.randint(0, 9)))
    return rnd

def string_number(num): return ''.join(num[::])