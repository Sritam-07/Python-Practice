def greet(fx):
    def mfx():
        print(f"Good morining Sir!")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def func():
    print("Hello World")

func()
       