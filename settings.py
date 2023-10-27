import pathlib
import os
import discord
from dotenv import load_dotenv
import logging
from logging.config import dictConfig

load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

BASE_DIR = pathlib.Path(__file__).parent

CMDS_DIR = BASE_DIR / "cmds"
COGS_DIR = BASE_DIR / "cogs"
SlASH_CMDS_DIR = BASE_DIR / "slash_cmds"

GUILD_ID = discord.Object(id=int(os.getenv("GUILD")))

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        'verbose': {
            "format": "%(levelname)-10s - %(asctime)s - %(module)-15s: %(message)s"
        },
        "simple": {
            "format": "%(levelname)-10s - %(name)-15s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple"
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/infos.log",
            "mode": "w",
            "formatter": "verbose"
        }
    },
    "loggers": {
        "bot": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False
        }
    }
}

dictConfig(LOGGING_CONFIG)
