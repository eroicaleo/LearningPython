X = 1


def nester():
    print(X)

    class C:
        print(X)

        def method1(self):
            print(X)

        def method2(self):
            X = 3
            print(X)

    I = C()
    I.method1()
    I.method2()

print(X)
nester()
print('x'*40)

