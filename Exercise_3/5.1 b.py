def visual(palindrome, n):
    if len(palindrome) == 1 or len(palindrome) == 0:
        print(n * " " + palindrome)
    else:
        print(n * " " + palindrome[0] + (len(palindrome)-2) * " " + palindrome[-1])
        palindrome = visual(palindrome[1:len(palindrome)-1], n + 1)


visual("Hannah", 0)