def f(text):
    words = text.split()
    lengths = [ len(i) for i in words ]
    longest = max(lengths)

    for i in words :
        if len(i) == longest :
            longest = i
            return longest

print(f("Python is a good programming language"))
