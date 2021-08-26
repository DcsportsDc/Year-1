
def hello(name):
    print("Hey {}".format(name))



integer = 5
string = ''
array_or_list = []
unique_numbers = set([1,1,1,1,2,2,2,2,3])
dictionary = {
    "a": "a",
    "b": "b",
    "c": "c",
}
boolean = True
decimal = 0.345345
none = None # null
func = hello
range_0_to_10 = list(range(10 + 1))
format_example = "{}, {}".format(integer, boolean)
question = input("Tell me something: ")
print("You told me: {}".format(question))
list_comprehension = [i for i in range(10)]
f = lambda x: x*2

def f2(a,b,c):
    print(a, b, c)
f2(*[1,2,3])

if boolean:
    print("True")
elif not boolean:
    pass
else:
    print("No")

for i in range(10):
    print(i)

for name in ["Pjotr", "Jeff", "Lars"]:
    print(name)

x = 5
while x > 0:
    print(x)
    x -= 1

for a, b in dictionary.items():
    print(a, "=", b)

try:
    y = 0
    x = 1
    z = x / y
    raise Exception("The code should never reach this!")
except ZeroDivisionError:
    print("Why?")

