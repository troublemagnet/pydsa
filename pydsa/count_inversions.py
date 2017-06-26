	# Counting inversions in an array
	# Complexity : O(nlog(n))


def _merge(L, R):
    m, i, j, cnt = [], 0, 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            m.append(L[i])
            i += 1
        else:
            m.append(R[j])
            j += 1
            cnt = cnt + len(L) - i
    if i == len(L):
        m.extend(R[j:])
    else:
        m.extend(L[i:])
    return m, cnt


def merge_sort(a):
    l = len(a)
    if l > 1:
        L = a[0:l // 2]
        R = a[l // 2:]
        L, left = merge_sort(L)
        R, right = merge_sort(R)
        merged, ans = _merge(L, R)
        return merged, left + right + ans
    return a, 0


def count_inversions(a):
	"""
	Counts the number of inversions in an array. 
	Divide and conquer algorithm is used for same.
	>>> from pydsa import count_inversions
	>>> a = [1,20,6,4,5]
	>>> count_inversions(a)
	5
	"""
	ans = merge_sort(a)
	return ans[1]

