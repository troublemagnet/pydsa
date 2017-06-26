from pydsa import count_inversions
def test_count_inversions():
	a = [1, 3, 20, 12, 6, 15, 4, 5, 7]
	assert count_inversions(a) == 15