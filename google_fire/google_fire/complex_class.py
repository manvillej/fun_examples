import time 
import fire
import sys

class timer(object):
    def __init__(self, total=10):
        self.total = total
        self.max_len = 0

    def countup(self):
        for i in range(self.total+1):
            time.sleep(.1)
            self.progress(i, status=f'{i}/{self.total}')
        print("\ncountup complete", end="")

    def countdown(self):
        for i in range(self.total+1):
            time.sleep(.1)
            self.progress(
                self.total-(i), 
                status=f'{self.total-(i)}/{self.total}',
                reverse=True)
        print("\ncountdown complete")

    def progress(self, count, status='', reverse=False):
        bar_len = 60
        filled_len = int(round(bar_len * count / float(self.total)))

        percents = round(100.0 * count / float(self.total), 1)

        if reverse:
            bar = '-' * (bar_len - filled_len) + '=' * filled_len
        else:
            bar = '=' * filled_len + '-' * (bar_len - filled_len)

        progress = f'[{bar}] {percents}% ...{status}'

        if(len(progress)<self.max_len):
            progress = progress + " "*(self.max_len-len(progress))
        else:
            self.max_len = len(progress)

        print(progress, end='\r')


def main():
    fire.Fire(timer)