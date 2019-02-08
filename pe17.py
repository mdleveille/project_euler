"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

number_letters = {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
number_str = ""
for integer in range(1,101):
    # print(integer)
    number = str(integer)


    if integer <= 20:
        number_str += number_letters[integer]


    elif len(number) == 2:
        # print(number)
        try:
            number_str += number_letters[integer]
        except KeyError:
            tens_lookup = int(number[0] + "0")
            ones_lookup = int(number[1])
            number_str += number_letters[tens_lookup] + number_letters[ones_lookup]


    # elif integer == 100:
    #     number_str += "onehundred"


    # elif len(number) == 3:
    #     hundreds_lookup = int(number[0])
    #     tens_lookup = int(number[1] + "0")
    #     ones_lookup = int(number[2])
    #     print(hundreds_lookup, tens_lookup, ones_lookup)
    #     try:
    #         string = number_letters[hundreds_lookup] + "hundred and " + number_letters[tens_lookup] +" "+ number_letters[ones_lookup]
    #     except KeyError:
    #         string = number_letters[hundreds_lookup] + "hundred and " + number_letters[ones_lookup]
    #     print(string)

    # elif len(number) == 4:
    #     number_str += "onethousand"


count = len(number_str)
print(count)
count += len("twohundredand"*99) + len(number_str)
count += len("threehundredand"*99) + len(number_str)
count += len("fourhundredand"*99) + len(number_str)
count += len("fivehundredand"*99) + len(number_str)
count += len("sixhundredand"*99) + len(number_str)
count += len("sevenhundredand"*99) + len(number_str)
count += len("eighthundredand"*99) + len(number_str)
count += len("ninehundredand"*99) + len(number_str)
count += len("onethousand")

print(count)

