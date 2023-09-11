text = input()
# считает прелдложения
count_sentence = 0
last = 0
now = 0
for i in text:
    if ord(i) > 1039 and ord (i) < 1072:
        now = 1
    if now == 1 and last == 1:
        now = 0
        last = 0
        count_sentence += 1
    if i in '.?!':
        last = 1
if last == 1:
    count_sentence += 1

# считает слоги
count_vowels = 0
for x in text.lower():
    if x in 'аоуыэуёюяие':
        count_vowels += 1

# как считать количество слов
count_words = text.count(" ") + 1

# индекс Флеша
I_F = 206.835 - 1.3 * (count_words/count_sentence) - 60.1 * (count_vowels/count_words)
print(I_F)
if I_F >= 90 and I_F <= 100:
    print('Очень высокий - 5 классов')
if I_F >= 80 and I_F < 90:
    print('Высокий - 6 классов')
if I_F >= 70 and I_F < 80:
    print('Выше среднего - 7 классов')
if I_F >= 60 and I_F < 70:
    print('Средний - 8-9 классов')
if I_F >= 50 and I_F < 60:
    print('Ниже среднего - 10-11 классов')
if I_F >= 30 and I_F < 50:
    print('Низкий - вуз')
if I_F >= 0 and I_F < 30:
    print('Очень низкий - выпускник вуза')