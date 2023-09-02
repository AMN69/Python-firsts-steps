#one.py

def func():
    print("func() in one.py")

print("Top level in one.py")

if __name__ == "__main__": # when you from the terminal call python one.py the internal __name__ var for that module is define as "__main__"
    print("one.py is being run directly")
else:
    print("one.py has been imported")