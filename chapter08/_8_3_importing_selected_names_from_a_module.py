from module import a, func
import module

# `a` is a reference to `module.a`. Reassigning `a` changes its reference to 
#   the new value. The `module.a` value remains unchanged.
a = 42
func()      # "func says that a is 37"
print(a)    # 42

# Reassigning `module.a` value.
module.a = 42
func()      # "func says that a is 42"
