import disnake

import settings
from classes.QueueInfo import QueueInfo
# These are the buttons and their responses when being clicked
# This initiates the button as a persistent view, so they stay active after shut off


class PersistentView(disnake.ui.View):
    _instance = None

#    def __new__(cls, *args, **kwargs):
#        if cls._instance is None:
#            cls._instance = super().__new__(cls, *args, **kwargs)
#        return cls._instance

    def __init__(self, client, *args, **kwargs):
        self.queueEnabled: bool = True
        self.client: disnake.Client = client
        self.log: settings.logging = settings.log
        self.queue_info: QueueInfo = settings.QUEUE
        super().__init__(*args, **kwargs)

# This is the Join/Leave button and its functions
# I think this button is doing too much -Covert
    @disnake.ui.button(
        label=settings.BUTTONLABEL1,
        style=disnake.ButtonStyle.green,
        custom_id="persistent_example:green",
    )
    async def green(self, _button: disnake.ui.Button, inter: disnake.MessageInteraction):
        log_channel: disnake.TextChannel = self.client.get_channel(settings.LOGGINGCHANNEL)
        if self.queueEnabled is False:
            await inter.response.send_message("Queue is currently closed, try again later", ephemeral=True)
            self.log.info(f"<@{inter.user.mention}> tried joining when it was empty")
            await log_channel.send(
                f"{inter.user.mention} tried joining when it was empty",
                allowed_mentions=disnake.AllowedMentions(users=False)
            )
            return
        user: disnake.User = inter.user
        if user in self.queue_info.queue and user in self.queue_info.priority:
            self.queue_info.queue.remove(user)
            self.queue_info.priority.remove(user)
            await inter.response.send_message("You successfully Left the queue!", ephemeral=True)
            self.log.info(f"{user.mention} left queue")
            await log_channel.send(
                f"{user.mention} left queue",
                allowed_mentions=disnake.AllowedMentions(users=False)
            )
            return
        elif user in self.queue_info.queue:
            self.queue_info.queue.remove(user)
            await inter.response.send_message("You successfully Left the queue!", ephemeral=True)
            self.log.info(f"{user.name} left queue")
            await log_channel.send(
                f"{user.mention} left queue",
                allowed_mentions=disnake.AllowedMentions(users=False))
            return
        guild = self.client.get_guild(settings.MAINSERVER)
        role_user = guild.get_member(user.id)
        if role_user is not None and (disnake.utils.get(guild.roles, id=settings.PRIORITY)) in role_user.roles:
            self.queue_info.priority.append(user)
            print(f"{user.mention} joined priority queue")
        self.queue_info.queue.append(user)
        print(len(self.queue_info.queue))
        self.log.info(f"{user.mention} joined queue")
        print(f"{user.mention} joined queue")
        await log_channel.send(
            f"{user.mention} joined queue",
            allowed_mentions=disnake.AllowedMentions(users=False))
        await inter.response.send_message("You successfully joined the queue", ephemeral=True)

# This is the red button that sends the preset messages in settings
# who's meant to be using the preset messages buttons? --Covert
    @disnake.ui.button(
        label=settings.BUTTONLABEL2, 
        style=disnake.ButtonStyle.blurple, 
        custom_id="persistent_example:blurple"
    )
    async def blurple(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        logChannel = self.client.get_channel(settings.LOGGINGCHANNEL)
        self.log = settings.log
        user = interaction.user
        if settings.PRESETMESSAGE1 == 'None':
            await interaction.response.send_message("There is no message to send", ephemeral=True)
            return
        else:
            await interaction.response.send_message(settings.PRESETMESSAGE1, ephemeral=True)
            self.log.info(f"<@{user.mention}> got the information from button 1")
            await logChannel.send(
                f"{user.mention} got the information from button 1", 
                allowed_mentions = disnake.AllowedMentions(users=False)
            )
            return

    @disnake.ui.button(
        label=settings.BUTTONLABEL3, 
        style=disnake.ButtonStyle.red, 
        custom_id="persistent_example:red"
    )
    async def red(self, button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        logChannel = self.client.get_channel(settings.LOGGINGCHANNEL)
        self.log = settings.log
        user = interaction.user
        if settings.PRESETMESSAGE2 == 'None':
            await interaction.response.send_message("There is no message to send", ephemeral=True)
            return
        else:
            await interaction.response.send_message(settings.PRESETMESSAGE2, ephemeral=True)
            self.log.info(f"<@{user.mention}> got the information from button 2")
            await logChannel.send(
                f"{user.mention} got the information from button 2", 
                allowed_mentions = disnake.AllowedMentions(users=False)
            )
            return

    @disnake.ui.button(
        label=settings.BUTTONLABEL4,
        style=disnake.ButtonStyle.grey,
        custom_id="persistent_example:grey"
    )
    async def grey(self, _button: disnake.ui.Button, interaction: disnake.MessageInteraction):
        log_channel = self.client.get_channel(settings.LOGGINGCHANNEL)
        user = interaction.user
        for i in range(0,len(self.queue_info.queue)):
            if self.queue_info.queue[i]==user:
                print(len(self.queue_info.queue))
                await interaction.response.send_message(f"You are in position #{i+1}", ephemeral=True)
                await log_channel.send(f"{user.mention} got the information from button 3", allowed_mentions = disnake.AllowedMentions(users=False))
                return