<error descr="starred assignment target must be in a list or tuple">*hi</error> = [1, 2]
*a, = range(5)
for a, *b in [(1, 2, 3), (4, 5, 6, 7)]:
    print(b)
a, b, c = seq[0], seq[1:-1], seq[-1]
a, *b, c = seq
[a, *b, c] = seq
