import os
import logging
import sys
from dotenv import load_dotenv
import pathlib

from classes.QueueInfo import QueueInfo

load_dotenv()

QUEUE=QueueInfo()

# Discord Developer Portal bot token
BOTTOKEN = os.getenv('BOTTOKEN')
# The prefix you want the bot to recognize as a command
PREFIX = os.getenv('PREFIX')
#This sets the name for your queue
QUEUENAME=os.getenv('QUEUENAME')
# The role that is put into priority queue
PRIORITY = int(os.getenv('PRIORITY'))
# The channel your bot is watching for the specific message
RAIDLOGCHANNEL = int(os.getenv('RAIDLOGCHANNEL'))
# The message you want the bot to watch for
RAIDTRIGGER = os.getenv('RAIDTRIGGER')
# The message you want the bot to watch for if you want a different thing to happen
REQUESTTRIGGER = os.getenv('REQUESTTRIGGER')
# The amount of people you want to be pulled from priority queue
# this is to prevent free members from being completely
# locked out in the event that more than 3 priority users join the queue
PRIORITYCOUNT = int(os.getenv('PRIORITYCOUNT'))
# The channel you want the bot to send logs to
LOGGINGCHANNEL = int(os.getenv('LOGGINGCHANNEL'))
# The server where priority role is given
MAINSERVER = int(os.getenv('MAINSERVER'))

BADSERVER = int(os.getenv('BADSERVER'))
# this is the messages that gets sent to the user when they click the blurple button
# Set the ones you don't want to use to None without quotations
PRESETMESSAGE1 = os.getenv('PRESETMESSAGE1')
# This is the message that gets sent to people when they click the red button
# Set the ones you don't want to use to None without quotations
PRESETMESSAGE2 = os.getenv('PRESETMESSAGE2')
# This is the message that gets sent to people when they click the grey button
# Set the ones you don't want to use to None without quotations
PRESETMESSAGE3 = os.getenv('PRESETMESSAGE3')
# This is the name for the green button
BUTTONLABEL1 = os.getenv('BUTTONLABEL1')
# This is the name for the blurple button
BUTTONLABEL2 = os.getenv('BUTTONLABEL2')
# This is the name for the red button
BUTTONLABEL3 = os.getenv('BUTTONLABEL3')
# This is the name for the grey button
BUTTONLABEL4 = os.getenv('BUTTONLABEL4')

BASE_DIR = pathlib.Path(__file__).parent

COGS_DIR = BASE_DIR / "cogs"


rootLogger = logging.getLogger()

c_handler = logging.StreamHandler(sys.stdout)
f_handler = logging.FileHandler(pathlib.Path(BASE_DIR / "debug.log"))
c_handler.setLevel(level=20)
f_handler.setLevel(level=20)
log_format = logging.Formatter(
    "[%(asctime)s - %(name)s - %(levelname)s] : [%(filename)s:%(lineno)s - %(funcName)s()] : %(message)s"
)
c_handler.setFormatter(log_format)
f_handler.setFormatter(log_format)

rootLogger.addHandler(c_handler)
rootLogger.addHandler(f_handler)

log = logging.getLogger("Bot logger")
log.setLevel(logging.INFO)

# log.debug("A DEBUG message")
# log.info("An INFO message")
# log.warning("A WARNING message")
# log.error("An ERROR message")
# log.critical("A CRITICAL message")
