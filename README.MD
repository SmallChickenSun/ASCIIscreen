# Перевод видео в ASCII

## Инструкция

1. скачиваем проект

2. распаковываем проект

3. запускаем командруню строку и пишем **python frameslise.py video.mp3**, где video это путь к вашему видео

4. ждем пока программа закончит и пишем **python imgtoascii.py file.txt**, где *file.txt* файл куда вы хотите записать информацию о видео, это может занять некоторое время

5. далее запускаем любой текстовый редактор, я рекоменду [vscode](https://code.visualstudio.com/), открываем файл screen.txt и запускаем **python screendraw.py file.txt**, где *file.txt* файл откуда вы хотите считать информацию.

6. наслаждаемся

## Зависимости

Незабудьте установить [python](https://www.python.org/)

А также прописать

- pip install Pillow
- pip install imageio
