print("before import")
import math

def main():
    function_a()
    function_b()

print("before function_a")
def function_a():
    print("Function A")

print("before function_b")
def function_b():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    print("Calling main module")
    main()
print("after __name__ guard")