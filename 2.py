r'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.'''

fn = [1]
max_fn = 2
while max_fn < 100:
	fn.append(max_fn)
	max_fn = fn[-1] + fn[-2]

assert fn == [1,2,3,5,8,13,21,34,55,89], "Initial sequence is incorrect."

fn = [1]
max_fn = 2
while max_fn < 4000000:
	fn.append(max_fn)
	max_fn = fn[-1] + fn[-2]

assert fn[-1] < 4000000, "Values exceed four million."

even_fn = [x for x in fn if x % 2 == 0]
print sum(even_fn)
