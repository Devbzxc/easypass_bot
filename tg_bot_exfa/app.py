import sys
import os

# Добавляем путь к текущей папке, чтобы видеть config.py
sys.path.insert(0, os.path.dirname(__file__))

# Правильный импорт (из той же папки)
from config import load_config, BotConfig

# Здесь должен быть остальной код файла
# Например:
# config = load_config()
# и так далее...
