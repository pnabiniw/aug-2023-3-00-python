"""
Separate out valid and invalid dictionary?
1. {"first message": "hello world"}
2. dict("message"="hello")
3. {"": 123}
4. dict(value=4)
5. {1: "Hello", 2: "World"}
6. {1.2: "Hello", 2.1: "World"}
7. {[1, 2, 3]: "Hello"}
8. {([1, 2,], 1): "World"}
9. {(2, 1): "World"}

"""

s = {"": 123}
print(s[""])
