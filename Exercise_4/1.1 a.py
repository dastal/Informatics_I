t = (1,"python",2,"tuple",3,"string")


def slice_tuple(tuple, a, b):
    print(tuple[a:b])


slice_tuple(t, 0, 3)
slice_tuple(t, 2, 5)
slice_tuple(t, -2, -1)
slice_tuple(t, 4, len(t))