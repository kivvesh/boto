'''
1. Данные полученные благодаря api сервиса будут полученны в формате json,
данный файл нужно будет загрузить в переменную нашего приложения. Далее данные необходимо распарсить в соответствии с требованиями.
Существует вероятность, что запрос по api не будет работать корректно, для устронения данной ошибки необходимо
изучить документацию по данному api. Также перед запросом проверять доступность сервиса, например, get запрос
'''

from spellchecker import SpellChecker

class Correct_text:
    spell = SpellChecker(language='ru')
    uncorrect_words = ['ля']#некорректные слова, которые стоит исключить
    def __init__(self, text):
        self.text = text.split(' ')
    def test_text(self):
        for sym in self.spell.known(self.text):
            if sym in self.uncorrect_words:
                return False
        misspelled = self.spell.unknown(self.text)
        final=[]
        for word in misspelled:
            final.append(self.spell.correction(word))
        if None in final:
            return False
        return True

def test():#тестирование
    word1 = Correct_text('ля ля')
    word2 = Correct_text('sfsdfdsfds')
    word3 = Correct_text('все круто')
    word4 = Correct_text('1.я бы хотел заметить')
    word5 = Correct_text('отлично, что я это увидел')
    assert word1.test_text() == False
    assert word2.test_text() == False
    assert word3.test_text() == True
    assert word4.test_text() == True
    assert word5.test_text() == True
test()




