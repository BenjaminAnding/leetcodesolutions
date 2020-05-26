from threading import Semaphore
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooSem = Semaphore()
        self.barSem = Semaphore()
        self.barSem.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.fooSem.acquire()
            try:
            # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
            finally:
                self.barSem.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.barSem.acquire()
            try:
            # printBar() outputs "bar". Do not change or remove this line.
                printBar()
            finally:
                self.fooSem.release()
