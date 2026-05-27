import logging
from rectangle import Rectangle
logging.basicConfig(level=logging.INFO,
                    format= "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
                    handlers= [
                        logging.FileHandler("app.log", encoding="utf-8"),
                        logging.StreamHandler()
                    ]
                )

logger = logging.getLogger(__name__)


def main():
    """Execute the main program logic and log execution."""
    logger.info("The program started running")

if __name__ == "__main__":
    main()