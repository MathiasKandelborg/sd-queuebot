from dataclasses import dataclass, field
from disnake import User

import disnake


@dataclass
class QueueInfo:
    queue: list[User] = field(default_factory=list)
    priority: list[User] = field(default_factory=list)
    priorityUsers: list[User] = field(default_factory=list)
    queueEnabled: bool = True
    request: bool = False
    button_locations: list[disnake.TextChannel.id] = field(default_factory=list)