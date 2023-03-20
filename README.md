# NumberToArabicWords
## Python implementation of the algorthim that convert a number to Arabic words with Algerian currency.
## تطبيق Python للجورثيم الذي يقوم بتحويل عدد إلى كلمات عربية بعملة جزائرية.


# Example: 
```bash
import number_to_arabic

number = '10000.13'
print(    number_to_arabic.number_to_word(number)  )
'10000.13' => عشرة آلاف دينار جزائري و ثلاثة عشر سنتيم


text = ''
with open("myfile.txt", "w", encoding='utf-8') as file1:
    text = number_to_arabic.number_to_word(number)
    file1.write(text)
```
PS: altough, I hard coded the Algerian currency, it can easly modified for another currency.


Author: NAIR Ahmed Amine
Email: AhmedAmine.Nair@gmail.com
Date: 06/05/2019
Original Algorithm creator: https://adelkhayata.wordpress.com/2010/10/04/number-to-word-arabic-version-3/
C++ implimentation: https://github.com/01walid/ArabicNumberToWord
Java implimentation: https://github.com/bluemix/NumberToArabicWords
