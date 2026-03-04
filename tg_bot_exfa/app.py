import sys
import os

# Добавляем корневую папку проекта в пути поиска
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Теперь импорт должен работать
from tg_bot_exfa.config import load_config, BotConfig

# Здесь остальной код файла (который был ниже)
# Например:
# config = load_config()
# и так далее...
