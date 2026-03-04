import os
import sys

# Добавляем путь к корневой папке проекта
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Добавляем путь к папке tg_bot_exfa (на всякий случай)
tg_bot_exfa_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'tg_bot_exfa'))
if tg_bot_exfa_path not in sys.path:
    sys.path.insert(0, tg_bot_exfa_path)

from tg_bot_exfa.bot import main

if __name__ == "__main__":
    main()
