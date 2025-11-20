from collections.abc import Callable
import re

def sum_profit(text:str,func:Callable[[str],float]):
    total=0

    for income in func(text):
        total += float(income)

    return total


def generator_numbers(text:str):
    numbers= re.findall(r"\d+\.\d+", text)

    for numb in numbers:
        yield float(numb)
 
if __name__=='__main__':
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")




