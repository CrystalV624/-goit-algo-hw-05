# Перше завдання 
def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache: 
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci
fib = caching_fibonacci()
print(fib(10))
print(fib(15))

# Друге завдання
import re
from typing import Callable

def generator_numbers(text: str):
    """
    Генерує дійсні числа з тексту.
    
    :param text: Вхідний текст, що містить дійсні числа.
    :yield: Наступне дійсне число y тексті.
    """
    pattern = r'\b\d+\.\d+\b'  
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable) -> float:
    """
    Обчислює загальну суму чисел y тексті за допомогою переданого генератора.
    
    :param text: Вхідний текст, що містить дійсні числа.
    :param func: Функція-генератор для отримання чисел з тексту.
    :return: Загальна сума чисел.
    """
    return sum(func(text))
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")

# Четверте завдання

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError

def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue
        
        command, args = parse_input(user_input)
        print(f"Received command: {command}, args: {args}")

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()