# Iterate numbers 1 to 100
# if the number is divisible by 3, then print "Fizz"
# if the number is divisible by 5, then print "Buzz"
# if the number is divisible by 3 & 5, then print "FizzBuzz"
# Otherwise just print the number
#
# The challenge task is to limit the characters in the algorithm to accomplish the goal
# Employing the DRY (don't repeat yourself) principle along with a cascade of ternary operators limited the
# character count

for i in range(1, 101):
    f = "Fizz" if i % 3 == 0 else ""
    b = "Buzz" if i % 5 == 0 else ""
    print(f + b if f or b else i)
