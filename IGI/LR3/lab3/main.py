# Lab 2: Functions Router
# Version 1.0
# Developer: Abmetko Pavel
# Date: 03.30.2024

import os
from Task1.task1 import main_1
from Task2.task2 import main_2
from Task3.task3 import main_3
from Task4.task4 import main_4
from Task5.task5 import main_5


# Task number input check.
def input_task(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= 5:
                return value
            else:
                print("The number must be either 1, 2, 3, 4 or 5")
        except ValueError:
            print("Enter the task number.")


# Main func.
def main():
    while True:
        task_number = input_task("Enter the task number: ")

        # Task number choice.
        if task_number == 1:
            main_1()
        elif task_number == 2:
            main_2()
        elif task_number == 3:
            main_3()
        elif task_number == 4:
            main_4()
        elif task_number == 5:
            main_5()

        choice = input("\nWould like to choose a new task to run? (yes / no)? ").lower()
        if choice != "yes":
            break


if __name__ == "__main__":
    main()
