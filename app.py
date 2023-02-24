import json
import queue

import sounddevice as sd
import vosk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


import voice
from skills import *
import words

q = queue.Queue()

model = vosk.Model('model_small')

device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')[
                     'default_samplerate'])  # получаем частоту микрофона


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def recognize(data, v, clf):
    '''
    Анализ распознанной речи
    '''

    # проверяем есть ли имя бота в data, если нет, то return
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return

    # удаляем имя бота из текста
    data.replace(list(trg)[0], '')

    # сравниваем с вариантами, получая наиболее подходящий ответ
    text_vector = v.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    # получение имени функции из ответа из data_set
    func_name = answer.split()[0]

    # озвучка ответа из модели data_set
    voice.speaker(answer.replace(func_name, ''))
    # оптимизация работы с openAI API
    if func_name == "question":
        question_ = data.replace(list(trg)[0], '')
        question(question_)
    else:
        # запуск функции из skills
        exec(func_name + '()')


def main():
    import json
import queue

import sounddevice as sd
import vosk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


import voice
from skills import *
import words

q = queue.Queue()

model = vosk.Model('model_small')

device = sd.default.device
samplerate = int(sd.query_devices(device[0], 'input')[
                     'default_samplerate'])  # получаем частоту микрофона


def callback(indata, frames, time, status):
    q.put(bytes(indata))


def recognize(data, v, clf):
    '''
    Анализ распознанной речи
    '''

    # проверяем есть ли имя бота в data, если нет, то return
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return

    # удаляем имя бота из текста
    data.replace(list(trg)[0], '')

    # сравниваем с вариантами, получая наиболее подходящий ответ
    text_vector = v.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    # получение имени функции из ответа из data_set
    func_name = answer.split()[0]

    # озвучка ответа из модели data_set
    voice.speaker(answer.replace(func_name, ''))
    if func_name == "question":
        question_ = data.replace(list(trg)[0], '')
        question(question_)
    else:
        # запуск функции из skills
        exec(func_name + '()')


def main():
    # приветсвенное сообщение
    fornow = datetime.datetime.now().strftime("%H")
    if 6 < int(fornow) <= 11:
        voice.speaker("Доброе утро хозяин")
    elif 11 < int(fornow) <= 17:
        voice.speaker("Добрый день хозяин")
    elif 17 < int(fornow) <= 22:
        voice.speaker("Добрый вечер хозяин")
    elif 22 < int(fornow) <= 6:
        voice.speaker("Доброй ночи хозяин")
    '''
    Обучаем матрицу ИИ
    и постоянно слушаем микрофон
    '''

    # Обучение матрицы на data_set модели
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set

    # постоянная прослушка микрофона
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)


if __name__ == '__main__':
    main()

    '''
    Обучаем матрицу ИИ
    и постоянно слушаем микрофон
    '''

    # Обучение матрицы на data_set модели
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))

    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set

    # постоянная прослушка микрофона
    with sd.RawInputStream(samplerate=samplerate, blocksize=16000, device=device[0], dtype='int16',
                           channels=1, callback=callback):

        rec = vosk.KaldiRecognizer(model, samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                recognize(data, vectorizer, clf)


if __name__ == '__main__':
    main()

