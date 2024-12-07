# 1
# import random
# from decimal import Decimal
# from datetime import datetime, timedelta
# class Descriptor:
#     def __init__(self):
#         self.value = Decimal(0)
#     def __get__(self, instance, owner):
#         return self.value
#     def __set__(self, instance, value):
#         if value <= 0:
#             print("Value Error")
#
# class Valuta:
#     def __init__(self, cureent):
#         self.current = Decimal(cureent)
#     def convert(self, amount):
#         if not isinstance(amount, (int,Decimal)):
#             raise ValueError("ValueError")
#         amount_decimal = Decimal(amount)
#         random_days = random.randint(1, 30)
#         conversion_date = datetime.now() + timedelta(days=random_days)
#         result = amount_decimal * self.current
#         return result, conversion_date.strftime("%Y-%m-%d")
# try:
#     converter = Valuta("12000")
#     amount = int(input("Enter Valuyte: "))
#     converted_amount, date = converter.convert(amount)
#     print(f"{amount} USD = {converted_amount} UZS (Sana: {date})")
# except ValueError as e:
#     print(e)

# import random
# from datetime import datetime,timedelta
# from decimal import Decimal
# class Descriptor:
#     def __init__(self):
#         self.value = Decimal(0)
#     def __get__(self, instance, owner):
#         return self.value
#     def __set__(self, instance, value):
#         if value <= 0:
#             print("Value Error")
# class Valuyta:
#     valute = Descriptor()
#     def __init__(self,ogartirish):
#         self.ozgartirish = Decimal(ogartirish)
#     def convert(self,miqdor):
#         if not isinstance(miqdor, (int,Decimal)):
#             raise ValueError("ValueError")
#         elif Decimal(miqdor) == 0:
#             print("ValueError")
#             breakpoint(miqdor)
#         miqdor_decimal = Decimal(Decimal(miqdor))
#         random_days = random.randint(1,30)
#         date_c = datetime.now() + timedelta(days=random_days)
#         result = miqdor_decimal * self.ozgartirish
#         return result, date_c.strftime("%Y-%m-%d")
# try:
#     converter = Valuyta("130")
#     amount = int(input("Enter Valuyta: "))
#     converted_amount, date = converter.convert(amount)
#     print(f"{amount} RUB = {converted_amount} UZS (Sana: {date})")
# except ValueError as e:
#     print(f"Error {e}")

# 2
import random
import decimal
import datetime
from decimal import Decimal


class Descriptor:
    def __init__(self):
        self.value = decimal.Decimal(0)

    def get(self, instance, owner):
        return self.value
    def set(self, instance, value):
        if value <= 0:
            raise ValueError("Mahsulot narxi manfiy yoki nol bo'lishi mumkin emas.")
        self.value = decimal.Decimal(value).quantize(decimal.Decimal('0.01'))
class MaxsulotNarxi:
    maxsulot = Descriptor()

    def __init__(self, narx):
        self.narx = narx
        self.chegirma_foizi = random.randint(1, 50)
        self.sana = datetime.datetime.now()
    @property
    def narxni_hisobla(self):
        chegirma = (self.chegirma_foizi / 100) * self.narx
        yangi_narx = self.narx - Decimal(f"{chegirma}")
        return yangi_narx.quantize(decimal.Decimal('0.01'))
    def str(self):
        return (f"Mahsulot narxi: {self.narx} UZS, "
                f"Chegirma: {self.chegirma_foizi}%, "
                f"Yangi narx: {self.narxni_hisobla} UZS "
                f"(Sana: {self.sana}).")
narx = MaxsulotNarxi(100000)
print(narx)