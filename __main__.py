import logging
import os

import dotenv
from disnake.ext import commands


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    dotenv.load_dotenv()

    if (token := os.getenv("TOKEN")) is None:
        logging.error("No 'TOKEN' environment variable was found.")
        exit(1)

    sealbot = commands.InteractionBot(
        reload=False,
        test_guilds=None,
        activity=None,
    )

    sealbot.run(token)


if __name__ == "__main__":
    main()
