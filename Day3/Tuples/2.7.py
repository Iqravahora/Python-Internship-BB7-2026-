def make_frozenset(lst):
    return frozenset(lst)

result = make_frozenset([1,2,2,3])
print(result)
print(type(result))
