def hanoi(n, orig, dest, aux):
    if n == 1:
        print("Mover disco 1 de {} a {}".format(orig, dest))
        return
    hanoi(n - 1, orig, aux, dest)
    print("Mover disco {} de {} a {}".format(n, orig, dest))
    hanoi(n - 1, aux, dest, orig)


n = 3
hanoi(n, 'A', 'C', 'B')