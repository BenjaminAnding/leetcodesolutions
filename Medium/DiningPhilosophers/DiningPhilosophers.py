from threading import Semaphore
class DiningPhilosophers:
    def __init__(self, n=5):
        self.n = n
        self.forks = [Semaphore() for _ in range(n)]
    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        with self.forks[philosopher]:
            with self.forks[(philosopher+1)%self.n]:
                pickLeftFork()
                pickRightFork()
                eat()
                putLeftFork()
                putRightFork()
