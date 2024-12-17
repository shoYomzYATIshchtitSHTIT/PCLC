from time import sleep, time
from contextlib import contextmanager

class cm_timer_1:
    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time()
        print(f"Time: {end_time - self.start_time:.1f}")

@contextmanager
def cm_timer_2():
    st = time()
    yield None
    en = time()
    print(f'Time: {en - st}')

def main6():
    with cm_timer_1():
        sleep(2.5)

    with cm_timer_2():
        sleep(2.5)


if __name__ == '__main__':
    main6()