# จงเขียนฟังชั่นแปลง เลขอารบิกเป็นเลขโรมัน และ เลขโรมันเป็นอารบิกโดยที่

# M=1000    CM=900    D=500    CD=400,

# C=100    XC=90    L=50    XL=40,

# X=10    IX=9    V=5    IV=4    I=1

# เช่น 197 = 100 + 90 +7 = 100 + 90 + 5 + 1 + 1 = C XC V I I

# (https://roman-numerals.info/)



class translator:
    roman = {'M':1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L':50, 'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
    def deciToRoman(self, num):
        result =''
        for roman_number in self.roman:
            while num >= self.roman[roman_number]:
                result += roman_number
                num -= self.roman[roman_number]
        return result

    def romanToDeci(self, s):
        i = 0
        result = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in self.roman:
                result += self.roman[s[i:i+2]]
                i += 2
            else:
                result += self.roman[s[i]]
                i += 1
        return result

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))