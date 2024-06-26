<p align="center">
  <img src="https://img.shields.io/badge/python-3.7%2B-blue">
  <img src="https://img.shields.io/github/license/programer3001/Jarvis">
</p>

# Jarvis

Jarvis is a voice assistant program that can perform various tasks by voice commands. This project was inspired by the Iron Man movie, where Tony Stark uses his AI assistant named Jarvis.

## Features

btw he understands only Russian

Jarvis can perform various tasks such as:

- Tell the weather
- Tell the date and time
- Launch the browser
- Turn off/restart the computer
- Ask chatGPT
- Take a screenshot
- Tell a joke
- And many more (you can check them in words.py)!

## Installation

To use Jarvis, you need to follow these steps:

1. Clone this repository:
<pre>
    git clone https://github.com/KaliyevArsen/Jarvis.git
    cd Jarvis
</pre>

2. Install the required Python packages by running pip install -r requirements.txt in the project directory.
<pre>
   pip install -r requirements.txt
</pre>

3. download a <a href="https://alphacephei.com/vosk/models">language model</a> for vosk and put in the same file and rename it in "model_small"

4. API's

- get <a href="https://openai.com/product">openAI</a> and <a href="https://openweathermap.org/api">openweathermap</a> API
- put it in "skills.py" file (23, 105 lines)
- also if not from Astana write your city in 107 and 114:21

5. requirement files 

- create a screenshots file and write the path to it(skills.py, 78)

## Usage

To use Jarvis, simply say "Hey Jarvis" followed by your command. For example, if you want to know the weather, say "Jarvis the weather".

To view a list of available commands, say "Jarvis, what can you do?"
  
### If you are not Russian-speaking

in "words.py" file translate the keys into your language 

## Contact

If you have any questions or suggestions about this project, feel free to contact us at kaliyev.arsen@gmail.com.

