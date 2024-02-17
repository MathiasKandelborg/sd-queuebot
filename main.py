import disnake
from disnake.ext import commands
import sys
import os

import settings
from classes.PersistentView import PersistentView


# This is the rest of the logic for the persistent view and bot initiation
class PersistentViewBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.log: settings.logging = settings.log
        super().__init__(command_prefix=settings.PREFIX, *args, **kwargs)
#        self.persistent_views_added = False
 #       self.PersistentView: PersistentView = PersistentView(timeout=None, client=self)

    async def on_ready(self) -> None:
        self.log.info(f"User: {self.user.name} (ID: {self.user.id})")
        self.log.info(f"{self.user.name} has started")
        print(f'{self.user.name} is ready for use!')
        print('-------------------------')
 #       if not self.persistent_views_added:
 #           self.add_view(self.PersistentView)
 #           self.persistent_views_added = True


if __name__ == '__main__':
    bot = PersistentViewBot(intents=disnake.Intents.all(), asyncio_debug=True,)
    bot.load_extensions("cogs")
    bot.run(settings.BOTTOKEN)
