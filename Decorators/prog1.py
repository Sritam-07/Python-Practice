def greet(fx):
    def mfx(*args):
        print(f"Good morining Sir!")
        fx(*args)
        print("Thanks for using this function")
    return mfx

# @greet
# def func():
#     print("Hello World")

@greet
def func2(a,b):
    print(a+b)
func2(2,19)
       