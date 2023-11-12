# TODO  Напишите функцию count_letters
def count_letters (text):
    lower_text = text.lower() #Приводим все к нижнему регистру
    src_text = ''.join(lower_text.split())  #Удаляем все пробелы
    modified_text = src_text.replace('\n','') #Удаляем все переносы строк

    marks = "!()-—[]{};?@#$%:,.^&8*…"
    dict_ = {}
    count = 0

    for i in modified_text:
        if i not in marks:
            dict_[i] = dict_.get(i,count)+1

    return dict_
# TODO Напишите функцию calculate_frequency
def calculate_frequency (dict_):
    total = sum(dict_.values()) #Вычисляется сумма

    for i in dict_:
        dict_[i] = round(dict_[i]/total,2)
        if dict_[i] == 0.0: #добавил для того, что в ответе отображалось 0.00 вместо 0.0
            dict_[i] = "0.00"

    return dict_

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
for i,j in calculate_frequency(count_letters(main_str)).items():
    print(f"{i}: {j}")