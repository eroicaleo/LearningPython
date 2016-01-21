X = 11


def g1():
    print(X)


def g2():
    global X
    X = 22


def h1():
    X = 33

    def nested():
        print(X)

    nested()


def h2():
    X = 33

    def nested():
        nonlocal X
        X = 44

    nested()
    print(X)

if __name__ == '__main__':
    g1()
    g2()
    g1()

    h1()
    h2()

