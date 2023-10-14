class A:
    def __init__(self, name: str) -> None:
        print("class constructor run")
        self.name = name

    def foo(self):
        return f"my name is {self.name}"

    def add(self, a: int, b: int):
        return a + b


a = A("Xiao")
b = A("Li")

print(a.foo())
print(b.foo())
