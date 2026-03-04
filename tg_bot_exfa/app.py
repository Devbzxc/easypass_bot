import sys
import os

# Добавляем путь к текущей папке, чтобы видеть config.py
sys.path.insert(0, os.path.dirname(__file__))

# Импортируем config из той же папки (без tg_bot_exfa.)
from config import load_config, BotConfig

# Здесь остальной код файла (который был ниже)
# Например:
# config = load_config()
# и так далее...
