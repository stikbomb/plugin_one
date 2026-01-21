from loguru import logger
from shiva.common.base import BaseDaemon
import asyncio


class PluginOneWorker(BaseDaemon):
    name = "plugin_one_worker"

    async def prepare(self):
        pass

    async def start(self):
        logger.info("Hello from plugin one worker!")
        self.running = True
        while self.running:
            # logger.info('Waiter sleep...')
            await asyncio.sleep(5)
        logger.warning(f"Stopped: {self.name}")

    async def stop(self):
        self.running = False
