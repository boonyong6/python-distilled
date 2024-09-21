nums = [1, 2, 3, 4, 5]

# Map
squares_lc = [x * x for x in nums]
squares_gen = (x * x for x in nums)
squares_fn = map(lambda x: x * x, nums)

# Filter
nums_gt_lc = [x for x in nums if x > 2]
nums_gt_gen = (x for x in nums if x > 2)
nums_gt_fn = filter(lambda x: x > 2, nums)

# Reduce
from functools import reduce

total_fn = reduce(lambda x, y: x + y, nums)
total_agg = sum(nums)
