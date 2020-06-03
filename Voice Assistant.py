import os
import speech_recognition as sr
from win10toast import ToastNotifier

r = sr.Recognizer()

prefix = ['ok', 'hey', 'alright']
prefix2 = ['computer', 'laptop', 'pc']

def process(words_said):
    first_word = 0
    last_word = 0

    if 'search' in words_said:
        for x in words_said:
            if x == 'search':
                h = False
                for i in range(len(words_said)):
                    if x == words_said[i]:
                        first_word = first_word + 2
                        last_word = first_word + 3
                        h = True
                if h == False:
                    first_word = first_word + 1
                    last_word = first_word + 2
                os.startfile('www.google.com/search?q=' + ' '.join(words_said[first_word:last_word]))
            first_word = first_word + 1
    elif 'open' in words_said:
        for x in words_said:
            if x == 'open':
                first_word = first_word + 1
                last_word = first_word + 2
                try:
                    os.startfile(words_said[first_word] + '.exe')
                    break
                except:
                    files_found = 0
                    shortcut_folder = os.environ.get('USERPROFILE') + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs'
                    f = False
                    
                    for e in range(2):
                        if e > 0: shortcut_folder = os.environ.get('USERPROFILE') + r'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs'
                        else: shortcut_folder = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'

                        for root, dirs, files in os.walk(shortcut_folder):
                            if words_said[first_word] + '.lnk' in files:
                                os.startfile(root + '\\' + words_said[first_word] + '.lnk')
                                files_found = files_found + 1
                                f = True
                                break
                        if files_found < 1:
                            for root, dirs, files in os.walk(shortcut_folder):
                                last_word = last_word + 1
                                if ' '.join(words_said[first_word:last_word]) + '.lnk' in str(files).lower():
                                    os.startfile(root + '\\' + ' '.join(words_said[first_word:last_word]) + '.lnk')
                                    f = True
                                    break
                        if f: break
                break
            first_word = first_word + 1
    else:
        # print('That is not a command')
        print(words_said)

print('started')
with sr.Microphone() as source:
    while True:
        while True:
            try:
                audio = r.listen(source)
                result = r.recognize_google(audio).lower().split(" ")
                words = results
                break
            except:
                pass
        if 'ok' in words:
            if 'computer' in words:
                process(words)
            elif 'laptop' in words:
                process(words)
            elif 'pc' in words:
                process(words)
        elif 'hey' in words:
            if 'computer' in words:
                process(words)
            elif 'laptop' in words:
                process(words)
            elif 'pc' in words:
                process(words)
        elif 'alright' in words:
            if 'computer' in words:
                process(words)
            elif 'laptop' in words:
                process(words)
            elif 'pc' in words:
                process(words)