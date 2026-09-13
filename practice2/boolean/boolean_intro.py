#1
print(True)
print(False)

#2
print(bool("Hello"))
print(bool(15))

#3
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#4
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

#5
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

#6
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#7
def my_function():
    return True


print(my_function())

#8
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#9
x = 200
print(isinstance(x, int))

