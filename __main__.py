import logging
import os
import dotenv
from core.bot import sealbot


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    dotenv.load_dotenv()

    if (token := os.getenv("TOKEN")) is None:
        logging.error(
            "No 'TOKEN' environment variable was found, please set it and try again."
        )
        exit(1)

    sealbot.run(token)


if __name__ == "__main__":
    main()
