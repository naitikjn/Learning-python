# Sets in python
s = set()
print(type(s))
l = [1,2,3,4,5]
s_from_list = set(l)
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(2)
s1 = s.intersection([1,2,3])
#print(s , s1)
print(len(s))
print(max(s1))
print(min(s))
s1 = {1,2}
print(s.isdisjoint(s1))