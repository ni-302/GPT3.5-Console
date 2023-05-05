@echo off
7z a GPT3.5-Console.zip main.py gpt.py config.py
pyinstaller main.py --hidden-import gpt --hidden-import config --hidden-import sys --hidden-import openai  --hidden-import configparser --onefile --name=GPT3.5-Console
move /Y dist\GPT3.5-Console.exe .
rd /S /Q build\ dist\
del /S /Q GPT3.5-Console.spec
pause