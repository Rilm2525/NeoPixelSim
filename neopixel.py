class NeoPixel:
    def __init__(self, spacing:int, n:int) -> None:
        self.n = n
        self.__spacing = spacing
        self.__led = [(0, 0, 0)] * self.n
        self.write()
    
    def __getitem__(self, index):
        return self.__led[index]
    
    def __setitem__(self, index, value):
        self.__led[index] = value

    def fill(self, color):
        for i in range(self.n):
            self.__led[i] = color

    def write(self):
        compiled_led = [f"\033[38;2;{led[0]};{led[1]};{led[2]}m■\033[0m" for led in self.__led]
        simulated_str = "\r" + (" " * self.__spacing).join(compiled_led)
        print(simulated_str, end="")
