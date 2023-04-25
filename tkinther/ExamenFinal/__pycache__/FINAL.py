
class Convertidor:
    def __init__(self):
        self.romanos_a_arabigos = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50}
        self.arabigos_a_romanos = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L'}

    def arabigo_a_romano(self, num):
        if num < 1 or num > 50:
            raise ValueError("El número debe estar entre 1 y 50.")
        romano = ''
        for arabigo, letra_romana in sorted(self.arabigos_a_romanos.items(), key=lambda x: -x[0]):
            while num >= arabigo:
                romano += letra_romana
                num -= arabigo
        return romano

    def romano_a_arabigo(self, num):
        num = num.upper()
        if num not in self.romanos_a_arabigos:
            raise ValueError("Ingrese un número romano válido")
        arabigo = self.romanos_a_arabigos[num]
        if num.startswith('X') and arabigo > 10:
            raise ValueError("Ingrese un número romano válido")
        for letra_romana, valor in self.romanos_a_arabigos.items():
            if letra_romana in num:
                arabigo += valor * (num.count(letra_romana) - (letra_romana == 'X' and num[-1] != 'X'))
        return arabigo