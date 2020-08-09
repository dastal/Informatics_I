t = (1,"python",2.5,[9,8,7],{1:"One", 2:"Two", 3:"Three"}, (1,))

def element_type(tuple, a):
    print(type(tuple[a]))

element_type(t, 0)
element_type(t, 1)
element_type(t, 2)
element_type(t, 3)
element_type(t, 4)
element_type(t, 5)