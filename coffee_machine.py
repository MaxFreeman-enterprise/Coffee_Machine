class CoffeeMachine:
    # machine_states
    _MAIN_MENU = "main menu"
    _COFFEE_CHOICE = "coffee choice"
    _FILL_WATER = "fill water"
    _FILL_MILK = "fill milk"
    _FILL_COFFEE_BEANS = "fill coffee beans"
    _FILL_CUPS = "fill cups"

    def __init__(self):

        self._water = 400
        self._milk = 540
        self._coffee_beans = 120
        self._cups = 9
        self._money = 550
        self._current_state = CoffeeMachine._MAIN_MENU

        self._display_main_menu()

    def _print_current_stock(self):
        print("\nThe coffee machine has:")
        print(f"{self._water} of water")
        print(f"{self._milk} of milk")
        print(f"{self._coffee_beans} of coffee beans")
        print(f"{self._cups} of disposable cups")
        print(f"{self._money} of money\n")

    def _update_stock_after_buy(self, type_of_coffee):

        temp_water = -1
        temp_milk = -1
        temp_coffee_beans = -1
        temp_cups = -1
        temp_money = -1

        if type_of_coffee == 1:
            temp_water = self._water - 250
            temp_milk = self._milk
            temp_coffee_beans = self._coffee_beans - 16
            temp_cups = self._cups - 1
            temp_money = self._money + 4
        elif type_of_coffee == 2:
            temp_water = self._water - 350
            temp_milk = self._milk - 75
            temp_coffee_beans = self._coffee_beans - 20
            temp_cups = self._cups - 1
            temp_money = self._money + 7
        elif type_of_coffee == 3:
            temp_water = self._water - 200
            temp_milk = self._milk - 100
            temp_coffee_beans = self._coffee_beans - 12
            temp_cups = self._cups - 1
            temp_money = self._money + 6

        if any([temp_water < 0, temp_milk < 0, temp_coffee_beans < 0, temp_cups < 0, temp_money < 0]):
            resources_names = ["water", "milk", "coffee beans", "disposable cups", "money"]
            fail_index = [temp_water < 0, temp_milk < 0, temp_coffee_beans < 0, temp_cups < 0, temp_money < 0].index(
                True)
            print("Sorry, not enough " + resources_names[fail_index] + "!\n")
        else:
            print("I have enough resources, making you a coffee!\n")
            self._water = temp_water
            self._milk = temp_milk
            self._coffee_beans = temp_coffee_beans
            self._cups = temp_cups
            self._money = temp_money

    def _update_stock_after_take(self):
        print(f"\nI gave you ${self._money}\n")
        self._money = 0

    def process_input(self, user_input):
        if self._current_state == CoffeeMachine._MAIN_MENU:
            self._process_main_menu(user_input)

        elif self._current_state == CoffeeMachine._COFFEE_CHOICE:
            self._process_coffee_choice(user_input)

        elif self._current_state == CoffeeMachine._FILL_WATER:
            self._process_fill_water(user_input)

        elif self._current_state == CoffeeMachine._FILL_MILK:
            self._process_fill_milk(user_input)

        elif self._current_state == CoffeeMachine._FILL_COFFEE_BEANS:
            self._process_fill_coffee_beans(user_input)

        elif self._current_state == CoffeeMachine._FILL_CUPS:
            self._process_fill_cups(user_input)

    def _process_main_menu(self, user_input):
        if user_input == "buy":
            self._current_state = CoffeeMachine._COFFEE_CHOICE
            self._display_coffee_choice()

        elif user_input == "fill":
            self._current_state = CoffeeMachine._FILL_WATER
            self._display_fill_water()

        elif user_input == "take":
            self._update_stock_after_take()
            self._current_state = CoffeeMachine._MAIN_MENU
            self._display_main_menu()

        elif user_input == "remaining":
            self._print_current_stock()
            self._current_state = CoffeeMachine._MAIN_MENU
            self._display_main_menu()

        elif user_input == "exit":
            exit()

    def _process_coffee_choice(self, user_input):

        if user_input.isnumeric():
            # user input: 1 - espresso, 2 - latte, 3 - cappuccino
            self._update_stock_after_buy(int(user_input))
            self._current_state = CoffeeMachine._MAIN_MENU
            self._display_main_menu()

        elif user_input == "back":
            self._current_state = CoffeeMachine._MAIN_MENU
            self._display_main_menu()

    def _process_fill_water(self, user_input):
        self._update_stock_water(int(user_input))
        self._current_state = CoffeeMachine._FILL_MILK
        self._display_fill_milk()

    def _process_fill_milk(self, user_input):
        self._update_stock_milk(int(user_input))
        self._current_state = CoffeeMachine._FILL_COFFEE_BEANS
        self._display_fill_coffee_beans()

    def _process_fill_coffee_beans(self, user_input):
        self._update_stock_coffee_beans(int(user_input))
        self._current_state = CoffeeMachine._FILL_CUPS
        self._display_fill_cups()

    def _process_fill_cups(self, user_input):
        self._update_stock_cups(int(user_input))
        print()
        self._current_state = CoffeeMachine._MAIN_MENU
        self._display_main_menu()

    def _display_main_menu(self):
        print("Write action (buy, fill, take, remaining, exit):\n")

    def _display_coffee_choice(self):
        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

    def _display_fill_water(self):
        print("\nWrite how many ml of water do you want to add:\n")

    def _display_fill_milk(self):
        print("Write how many ml of milk do you want to add:\n")

    def _display_fill_coffee_beans(self):
        print("Write how many grams of coffee beans do you want to add:\n")

    def _display_fill_cups(self):
        print("Write how many disposable cups of coffee do you want to add:\n")

    def _update_stock_water(self, water_filled):
        self._water += water_filled

    def _update_stock_milk(self, milk_filled):
        self._milk += milk_filled

    def _update_stock_coffee_beans(self, coffee_beans_filled):
        self._coffee_beans += coffee_beans_filled

    def _update_stock_cups(self, cups_filled):
        self._cups += cups_filled


my_coffee_machine = CoffeeMachine()

while True:
    my_coffee_machine.process_input(input())
