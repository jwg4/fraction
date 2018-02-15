class Fraction:
    def __init__(self, numerator=0, denominator=1):
        self.numerator = numerator
        self.denominator = denominator

    def _gcd(self, num1, num2):
        if num2 == 0:
            return num1
        return self._gcd(num2, num1 % num2)

    @staticmethod
    def reciprocal(fraction):
        return Fraction(fraction.denominator, fraction.numerator)
        
    def __add__(self, other_fraction):
        a_n, a_d, b_n, b_d = self.numerator, self.denominator, other_fraction.numerator, other_fraction.denominator
        denom_lcm = (a_d * b_d) / self._gcd(a_d, b_d)
        new_numerator = ((denom_lcm / a_d) * a_n) + ((denom_lcm / b_d) * b_n)
        reduced_frac_gcd = self._gcd(new_numerator, denom_lcm)
        return Fraction(new_numerator / reduced_frac_gcd, denom_lcm / reduced_frac_gcd)

    def __sub__(self, other_fraction):
        a_n, a_d, b_n, b_d = self.numerator, self.denominator, other_fraction.numerator, other_fraction.denominator
        denom_lcm = (a_d * b_d) / self._gcd(a_d, b_d)
        new_numerator = ((denom_lcm / a_d) * a_n) - ((denom_lcm / b_d) * b_n)
        reduced_frac_gcd = self._gcd(new_numerator, denom_lcm)
        return Fraction(new_numerator / reduced_frac_gcd, denom_lcm / reduced_frac_gcd)

    def __mul__(self, other_fraction):
        a_n, a_d, b_n, b_d = self.numerator, self.denominator, other_fraction.numerator, other_fraction.denominator
        denom_lcm = a_d * b_d
        new_numerator = a_n * b_n
        reduced_frac_gcd = self._gcd(new_numerator, denom_lcm)
        return Fraction(new_numerator / reduced_frac_gcd, denom_lcm / reduced_frac_gcd)

    def __div__(self, other_fraction):
        return self.__mul__(Fraction.reciprocal(other_fraction))
