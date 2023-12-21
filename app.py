# send messages to users (save msg ids, admin_id who sent the msg)
# what bytesio seek function do in python

#remove pycache files from git control
# auto-deleting unnecessary messages
# instead of deleting messages just change inline message

# study postgresql, gino, sqlalchemy
# add postgresql to bot
# update bot on server, install postgresql

# create webhook
# compare the Stick bot with other
# improve errors handling and notifying
# advance analytics of bot user interactions
# moving back between handlers
# change kirillic alphabet to latin one e.g. ф=f in correcr_name middleware
# find all emoji storage

# upload bot to github (every month on 1st)

from loader import DP
import middlewares, filters, handlers


# async def on_start(DP):
    # DB.create_table_users()


async def shutdown(DP):
    await DP.storage.close()
    await DP.storage.wait_closed()


if __name__ == "__main__":
    from aiogram.utils.executor import start_polling
    start_polling(dispatcher = DP,
                # on_startup = on_start,
                on_shutdown = shutdown,
                skip_updates = True)


# 1.0.0 - Polling on Heroku server
# 2.0.0 - Polling on Amazon server
# 2.1.0 - Add database
# 2.1.1 - Bugs fixed and some little additions
# 2.1.2 - Replacing echo to logs in echo.py handler
# 2.1.3 - Changing setting of states 20/05/2023
# 2.1.4 - cancel accepting same inline quiries

__version__ = '2.1.6'
