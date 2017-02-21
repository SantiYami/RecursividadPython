def inv(l):
    if len(l)==1:
        return l[:1]
    else:
        return inv(l[-1:])+inv(l[:-1])

l=['a', 'b', 'c', 'd', 'e']
print inv(l)
