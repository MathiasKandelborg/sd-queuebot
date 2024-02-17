import disnake
from disnake.ext import commands

import settings
from classes.PersistentView import PersistentView
from classes.QueueInfo import QueueInfo


class LogListener(commands.Cog):
    def __init__(self, bot):
        self.bot: disnake.Client = bot
        self.log: settings.logging = settings.log
        self.queue_info: QueueInfo = QueueInfo()
        self.persistent_views_added = False

    async def cog_load(self) -> None:
        if not self.persistent_views_added:
            self.bot.add_view(PersistentView(timeout=None, client=self.bot))
            self.persistent_views_added = True
        self.log.info("loaded")

    # This tells the bot what to do when it finds the message
    async def on_raid(self, message: disnake.Message):
        priority_pulled = 0
        log_channel=self.bot.get_channel(settings.LOGGINGCHANNEL)
        s = message.content + "\n"     
        for i in range(0, 3):
            if self.queue_info.request == True:
                priority_pulled += 1
                str(i + 1)
                self.queue_info.request == False
            if priority_pulled < settings.PRIORITYCOUNT and len(self.queue_info.priority) > 0:
                priority_pulled += 1
                print("it made it this far")
                user = self.queue_info.priority.pop(0)
                self.queue_info.queue.remove(user)
                await user.send(message.content)
                s += str(i + 1) + f". <@{user.id}>" + "\n"
                print(f"<@{user.id}> Pulled From Priority")
                self.log.info(f"<@{user.id}> Pulled From Priority")
            elif len(self.queue_info.queue) > 0:
                user = self.queue_info.queue.pop(0)
                if user in self.queue_info.priority:
                    self.queue_info.priority.remove(user)
                await user.send(message.content)
                s += str(i + 1) + f". <@{user.id}>" + "\n"
                print(f"<@{user.id}> Pulled From Normal")
                self.log.info(f"<@{user.id}> Pulled From Priority")
        await log_channel.send(s, allowed_mentions=disnake.AllowedMentions(users=False))


    @commands.command(name='menu', description="This will add the buttons")
    async def menu(self, inter):
        await inter.channel.send(settings.QUEUENAME, view=PersistentView(timeout=None, client=self.bot))
        print("Button Created")

    @commands.command(name="viewservers", description="see which servers have the bot")
    async def viewservers(self, inter):
        s = ""
        i = 0
        await inter.channel.send("Sending server list")
        
        for guild in self.bot.guilds:
            if i > 9:
                await inter.channel.send(s)
                i = 0
                s = ""
            s += guild.name + " ID: " + str(guild.id) + " joined at:" + guild.me.joined_at.strftime("%b %d, %Y, %X") + "\n"
            i+=1
        if i > 0:
            await inter.channel.send(s)

    @commands.command(name="removeserver", description="leaves a bad server")
    async def removeserver(self, inter):
        guild = self.bot.get_guild(settings.BADSERVER)
        print("Removing guild " + guild.name)
        await guild.leave()
        await inter.channel.send("left guild")

    @commands.Cog.listener()
    async def on_message(self, message: disnake.Message):
        log_channel= self.bot.get_channel(settings.RAIDLOGCHANNEL)
        if message.channel == log_channel:
            if settings.RAIDTRIGGER in message.content and message.author.id != self.bot.user.id:
                print(len(self.queue_info.queue))
                if "ij0ltu" in message.content:
                    print("iJ0LTU found in " + message.content)
                    self.log.info("iJ0LTU found in " + message.content)
                    await log_channel.send("iJ0LTU found in " + message.content)
                else:
                    await self.on_raid(message)
                    print("Found message " + message.content)
                    self.log.info("Found message " + message.content)
                    await log_channel.send("Found message " + message.content)
            elif settings.REQUESTTRIGGER in message.content and message.author.id != self.bot.user.id:
                print(len(self.queue_info.queue))
                if "Admin Provided Raid" in message.content:
                     print("Admin Provided Raid Discovered")
                     await log_channel.send("Admin Provided Raid Discovered")
                else:
                    self.queue_info.request == True
                    print("Player Provided Raid Discovered")
                    await log_channel.send("Player Provided Raid Discovered")
            else:
                return


def setup(bot: commands.Bot):
    bot.add_cog(LogListener(bot))