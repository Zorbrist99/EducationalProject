import logging

logging.basicConfig(
    level=logging.INFO,  # показываем все сообщения от INFO и выше
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",  # формат вывода
    datefmt="%H:%M:%S"  # время в человеко-читаемом виде
)

logger = logging.getLogger(__name__)
