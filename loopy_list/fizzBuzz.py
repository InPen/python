def fizzbuzz(n):
    for index in range(n):
        if index %5 == 0 and index %3 == 0:
            print('fizzbuzz')
        elif index %5 == 0:
            print('buzz')
        elif index %3 == 0:
            print('fizz')
        else:
            print(index)
fizzbuzz(305)
