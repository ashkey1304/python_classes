# Write a Python program to create a chain of function decorators (bold, italic, underline etc.).
def bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b"
    return wrapped

def italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def underline(fn):
    def warpped():
        return "<u>" + fn() + "</u>"
    return warpped

def hello():
    return "Hello World"
print(hello())
