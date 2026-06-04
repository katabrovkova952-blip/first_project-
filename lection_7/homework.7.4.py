def common_elements():
	set_1 = set()
	set_2 = set()
	for i in range(0, 100):
		if i % 3 == 0:
			set_1.add(i)
		if i % 5 == 0:
			set_2.add(i)
	result = set_1.intersection(set_2)
	return result
print(common_elements())
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
