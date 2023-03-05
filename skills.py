import os
import webbrowser
from datetime import datetime
import datetime
import openai
import pyautogui
import pyjokes
import requests
from googletrans import Translator

import voice




def browser():
    webbrowser.open('https://www.youtube.com', new=2)



def question(a):
    print("Спрашиваю у chatGPT")
    openai.api_key = "your API key"
    model_engine = "text-davinci-003"
    prompt = a

    max_tokens = 1024

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    voice.speaker(completion.choices[0].text)
    


def date():
    now = datetime.datetime.now()

    months = {
        1: "января",
        2: "февраля",
        3: "марта",
        4: "апреля",
        5: "мая",
        6: "июня",
        7: "июля",
        8: "августа",
        9: "сентября",
        10: "октября",
        11: "ноября",
        12: "декабря",
    }

    date_str = now.strftime("%d {month} %Y года").format(month=months[now.month])

    voice.speaker(date_str)


def joke():
    text = pyjokes.get_joke()
    translator = Translator()
    try:
        t = translator.translate(text, dest="ru")
        voice.speaker(t.text)
    except Exception as e:
        print(f"Ошибка перевода: {e}")


def screenshot():
    try:
        img = pyautogui.screenshot()
        img.save(
            "C:\\Users\\user\\Desktop\\Jarvis\\screenshots\\ss.png"
        )
        voice.speaker('Готово')
    except:
        print("Проверьте правильность написания пути")


def vrema():
    Time = datetime.datetime.now().strftime("%H:%M")
    voice.speaker("сейчас")
    voice.speaker(Time)


def offpc():
    os.system("shutdown -i")


def restart():
    os.system("shutdown /r /t 1")


def sleep():
    os.system("shutdown /h")


def weather():
    api_key = "your API key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "Astana"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        r = ("в " + "Астане" + " температура " +
             str(int(current_temperature - 273.15)))
        voice.speaker(r)


def offBot():
    exit()


def passive():
    pass
