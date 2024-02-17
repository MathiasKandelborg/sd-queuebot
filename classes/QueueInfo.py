from dataclasses import dataclass, field

import disnake


@dataclass
class QueueInfo:
    queue: list[disnake.user] = field(default_factory=list)
    priority: list[disnake.user] = field(default_factory=list)
    priorityUsers: list[disnake.user] = field(default_factory=list)
    queueEnabled: bool = True
    request: bool = False
    button_locations: list[disnake.TextChannel.id] = field(default_factory=list)