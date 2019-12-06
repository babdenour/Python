class CoffeeMachine:
    WATER_LEVEL = 100

    def _start_machine(self):
        if self.WATER_LEVEL > 20:
            return True
        else:
            print("add water !!!")
            return False
        #starts the machine

    def __boil_water(self):
        #boiling the water
        return "Boiling ..."

    def make_coffee(self):
        #yumm a good  coffee
        if self._start_machine():
            self.WATER_LEVEL -= 20
            print(self.__boil_water())
            print("Coffee is ready")

machine = CoffeeMachine()
print("make Coffe public ", machine.make_coffee())
print("start protected ", machine._start_machine())
print("boil private ", machine._CoffeeMachine__boil_water())
