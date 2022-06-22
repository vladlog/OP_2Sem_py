
class TIntNumber:
    def __init__(self):
        self.__number = ""
        self.__base = 0

    def get_number(self):
        return self.__number

    def get_base(self):
        return self.__base

    def set_number(self,line):
        self.__number = line

    def set_base(self,num):
        self.__base = num

    def __iadd__(self, other):
        pass

    def __isub__(self, other):
        pass

    def ToDecimal(self):
        new_num = int(self.__number,self.__base)
        return new_num

    def __str__(self):
        return f"{self.__number} "

class TIntNumber2(TIntNumber):

    def ToBin(self,num):
        bin_num = ""
        if num < 0:
            bin_num = "-" + bin(num).split('b')[-1]
        else:
            bin_num = bin(num).split('b')[-1]
        return bin_num


    def __iadd__(self, other):
        new_num = super().ToDecimal()
        new_num += other
        self.set_number(self.ToBin(new_num))
        return self

    def __isub__(self, other):
        new_num = super().ToDecimal()
        new_num -= other
        self.set_number(self.ToBin(new_num))
        return self

class TIntNumber16(TIntNumber):

    def ToHex(self,num):
        bin_num = ""
        if num < 0:
            bin_num = "-" + hex(num).split('x')[-1]
        else:
            bin_num = hex(num).split('x')[-1]
        return bin_num

    def __iadd__(self, other):
        new_num = super().ToDecimal()
        new_num += other
        self.set_number(self.ToHex(new_num))
        return self

    def __isub__(self, other):
        new_num = super().ToDecimal()
        new_num -= other
        self.set_number(self.ToHex(new_num))
        return self
