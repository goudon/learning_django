import sys

FIZZ_BUZZ_DICT = {3:"FIZZ",5:"BUZZ"}

class FizzBuzzClass():
    def __init__(self, num):
        self._num = num
    
    def output(self):
        i = 0
        while i <= self._num:
            output_str = ""
            for key_num in FIZZ_BUZZ_DICT:
                if i % key_num == 0 and i != 0:
                    output_str += FIZZ_BUZZ_DICT[key_num]
            print(f'{i} is {output_str}')
            i += 1


if __name__ == '__main__':
    count = int(sys.argv[1])
    if type(count) is int:
        print("passed")
        FizzBuzz = FizzBuzzClass(count)
        FizzBuzz.output()