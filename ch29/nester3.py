X = 1


def nester():
    X = 2
    print(X)

    class C:
        X = 3
        print(X)

        def method1(self):
            print(X)
            print(self.X)

        def method2(self):
            X = 4
            print(X)
            self.X = 5
            print(X)
            print(self.X)

    I = C()
    I.method1()
    I.method2()

print(X)
nester()
print('x'*40)

