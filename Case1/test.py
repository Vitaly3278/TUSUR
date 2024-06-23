print (range(3))
a = {'x': 1, 'y': 2}

a['z'] = 3

print(a)


def foo():
    try:

        return 1

    finally:

        return 2


print(foo())