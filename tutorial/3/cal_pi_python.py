# calc_pi.py
a = [i for i in range(1000)]

def recip_square(i):
    return 1. / i ** 2


def approx_pi(n=10000000):
    val = 0.
    for k in range(1, n + 1):
        val += recip_square(k)
    return (6 * val) ** .5


if __name__ == '__main__':
    approx_pi()
