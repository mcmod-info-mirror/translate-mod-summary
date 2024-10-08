from pymongo import MongoClient

from utils.config.mongodb import MongodbConfig
from loguru import logger

_mongodb_config = MongodbConfig.load()

engine: MongoClient = None


def init_engine() -> MongoClient:
    """
    Raw Motor client handler, use it when beanie cannot work
    :return:
    """
    global engine
    engine = MongoClient(
        f"mongodb://{_mongodb_config.user}:{_mongodb_config.password}@{_mongodb_config.host}:{_mongodb_config.port}"
        if _mongodb_config.auth
        else f"mongodb://{_mongodb_config.host}:{_mongodb_config.port}"
    )
    return engine


engine: MongoClient = init_engine()
database = engine[_mongodb_config.database]

logger.info("MongoDB connection established.")
