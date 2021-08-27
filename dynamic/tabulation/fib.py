""" Generating fibonacci numbers """


def fib_tab(n):
    """ Generate nth fibonacci number """
    table = [0 for i in range(n+1)]
    table[1] = 1
    for i in range(n):
        table[i + 1] += table[i]
        if i == n-1:
            continue
        table[i + 2] += table[i]

    return table[n]


if __name__ == "__main__":
    print(fib_tab(50))