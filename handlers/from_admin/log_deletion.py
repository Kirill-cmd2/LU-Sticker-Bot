from os import remove

from aiogram.dispatcher.filters import Command

from filters import IsAdminFilter
from loader import DP


@DP.message_handler(Command('deletelog'), IsAdminFilter())
async def delete_log_file(msg):
    """
    Function for deleting log file by command to bot
    Using os.remove()
    No need to manually connect to server and delete the file
    """
    file = 'logfile.log'

    try:
        remove(file)
    except FileNotFoundError:
        await msg.answer("Log file not found, so not deleted")
    else:
        await msg.answer("Successfuly deleted log file")
