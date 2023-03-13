
# Usage: number_to_word('15234.78')
# Description:
# A function that converts decimal to it's correspending textual representation
# Example 1: '10000.00'  => عشرة ألاف دينار جزائري
# Example 2: '15234.78' =>
# خمسة عشر ألفاً  و مئتا و أربع و ثلاثون ديناراً جزائرياً و ثمان و سبعون سنتيما
#
# Author: NAIR Ahmed Amine
# Email: AhmedAmine.Nair@gmail.com
# Date: 06/05/2019
# Original Algorithm creator:
# https://adelkhayata.wordpress.com/2010/10/04/number-to-word-arabic-version-3/
# C++ implimentation: https://github.com/01walid/ArabicNumberToWord
# Java implimentation: https://github.com/bluemix/NumberToArabicWords

from decimal import Decimal

tab_ones = [
    "", "واحد", "اثنان", "ثلاثة", "أربعة",
    "خمسة", "ستة", "سبعة", "ثمانية", "تسعة",
    "عشرة", "أحد عشر", "اثنا عشر", "ثلاثة عشر", "أربعة عشر",
    "خمسة عشر", "ستة عشر", "سبعة عشر", "ثمانية عشر", "تسعة عشر"
    ]

tab_feminine_ones = [
    "", "إحدى", "اثنتان", "ثلاث", "أربع",
    "خمس", "ست", "سبع", "ثمان", "تسع",
    "عشر", "إحدى عشرة", "اثنتا عشرة", "ثلاث عشرة", "أربع عشرة",
    "خمس عشرة", "ست عشرة", "سبع عشرة", "ثماني عشرة", "تسع عشرة"]

tab_tens = [
    "عشرون", "ثلاثون", "أربعون", "خمسون",
    "ستون", "سبعون", "ثمانون", "تسعون"]

tab_hundreds = [
    "", "مائة", "مئتان", "ثلاثمائة", "أربعمائة",
    "خمسمائة", "ستمائة", "سبعمائة", "ثمانمائة", "تسعمائة"]

tab_appended_twos = [
    "مئتا", "ألفا", "مليونا", "مليارا",
    "تريليونا", "كوادريليونا", "كوينتليونا", "سكستيليونا"]

tab_twos = [
    "مئتان", "ألفان", "مليونان", "ملياران",
    "تريليونان", "كوادريليونان", "كوينتليونان", "سكستيليونان"]

tab_twos_special_cases = [
    2_000,
    2_000_000,
    2_000_000_000,
    2_000_000_000_000,
    2_000_000_000_000_000,
    2_000_000_000_000_000_000]

tab_group = [
    "مائة", "ألف", "مليون", "مليار",
    "تريليون", "كوادريليون", "كوينتليون", "سكستيليون"]

tab_appended_group = [
    "", "ألفاً", "مليوناً", "ملياراً",
    "تريليوناً", "كوادريليوناً", "كوينتليوناً", "سكستيليوناً"]

tab_plural_groups = [
    "", "آلاف", "ملايين", "مليارات",
    "تريليونات", "كوادريليونات", "كوينتليونات", "سكستيليونات"]


def number_to_word(number):
    
    # make sure there is a decimal part in the string
    if '.' not in number:
        number += '.00'

    # convert String to a type Decimal
    n = Decimal(number)

    # special case of Zero
    if n == 0:
        result = "صفر"
        return result

    # extract  to decimal and integer parts of n
    number_integer_part = int(n)
    number_decimal_part = int((n-int(n))*100)

    # 1- format the integer part of the number
    ret_val = ""
    group = 0
    temp_number = n
    number_to_process = None
    group_description = ""
    while(True):
        if temp_number <= 0:
            break
        # Seperate number into groups
        number_to_process = int(temp_number % 1000)
        temp_number = int(temp_number/1000)
        # Convert group into its text
        group_description = process_arabic_group(
            number_to_process, group, temp_number, n)
        if group_description != "":
            if group > 0:
                if ret_val != "":
                    ret_val = " و" + " " + ret_val
                if number_to_process != 2:
                    if number_to_process % 100 != 1:
                        if number_to_process >= 3 and number_to_process <= 10:
                            ret_val = tab_plural_groups[group]+" "+ret_val
                        else:
                            if ret_val != "":
                                ret_val = tab_appended_group[group]+" "+ret_val
                            else:
                                ret_val = tab_group[group]+" "+ret_val
                    else:
                        ret_val = tab_group[group]+" "+ret_val
            ret_val = group_description + " " + ret_val
        group += 1

    # 2- append currency
    algerian_1_currency_name = u"دينار جزائري"
    algerian_2_currency_name = u"ديناران جزائريان"
    algerian_310_currency_name = u"دنانير جزائرية"
    algerian_1199_currency_name = u"ديناراً جزائرياً"
    formatted_number = ret_val
    if number_integer_part != 0:
        remaining100 = int(
            Decimal(number_integer_part) % 100)
        if remaining100 == 0 or remaining100 == 1:
            formatted_number += algerian_1_currency_name
        if remaining100 == 2:
            if Decimal(number_integer_part) == 2:
                formatted_number += algerian_2_currency_name
            else:
                formatted_number += algerian_1_currency_name
        if remaining100 >= 3 and remaining100 <= 10:
            formatted_number += algerian_310_currency_name
        if remaining100 >= 11 and remaining100 <= 99:
            formatted_number += algerian_1199_currency_name

    # 3- add decimal part to the formatted_number
    algerian_1_currency_part_name = u"سنتيم"
    algerian_2_currency_part_name = u"سنتيمان"
    algerian_310_currency_part_name = u"سنتيم"
    algerian_1199_currency_part_name = u"سنتيما"
    if number_decimal_part != 0:
        decimal_string = process_arabic_group(number_decimal_part, -1, 0, n)
        formatted_number += u" و " + decimal_string + u" "
        if remaining100 == 0 or remaining100 == 1:
            formatted_number += algerian_1_currency_part_name
        if remaining100 == 2:
            formatted_number += algerian_2_currency_part_name
        if remaining100 >= 3 and remaining100 <= 10:
            formatted_number += algerian_310_currency_part_name
        if remaining100 >= 11 and remaining100 <= 99:
            formatted_number += algerian_1199_currency_part_name
    return formatted_number


def process_arabic_group(
        group_number, group_level,
        remaining_number, number):

    tens = group_number % 100
    hundreds = group_number // 100
    ret_val = ""
    if hundreds > 0:
        if tens == 0 or hundreds == 2:
            # addition case
            ret_val = tab_appended_twos[0] 
        else:
            # normal case
            ret_val = tab_hundreds[hundreds]

    if tens > 0:
        if tens < 20:
            if tens == 2 and hundreds == 0 and group_level > 0:
                if int(number) in tab_twos_special_cases:
                    # addition case
                    ret_val = tab_appended_twos[group_level]
                else:
                    # normal case
                    ret_val = tab_twos[group_level]        
            else:
                if ret_val != "":
                    ret_val += " و "
                if tens == 1 and group_level > 0 and hundreds == 0:
                    ret_val += ""
                else:
                    if ((tens == 1 or tens == 2) and
                            (group_level == 0 or group_level == -1) and
                            hundreds == 0 and remaining_number == 0):
                        ret_val += ""  # special case for 1 and 2 numbers
                    else:
                        ret_val += tab_ones[tens]
        else:
            ones = tens % 10
            tens = tens // 10 - 2
            if ones > 0:
                if ret_val != "":
                    ret_val += " و "
                ret_val += tab_feminine_ones[ones]
            if ret_val != "":
                ret_val += " و "
            ret_val += tab_tens[tens]
    return ret_val



if __name__ == "__main__":

