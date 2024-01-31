import sys
class Jar:
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError
        else:
            self._capacity = capacity
            self._size = 0
            
    def __str__(self):
        if self._size == 0:
            return "Empty"
        else:
            return str("🍪" * self._size)

    def deposit(self, n):
        if n < 0 or n > self._capacity or (n + self._size)>self._capacity:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if n > self._capacity or n > self.size :
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar(10)
    print(jar)
    print(str(jar.capacity))
    print(str(jar.size))
    jar.deposit(5)
    print(jar)
    jar.deposit(5)
    print(jar)
main()