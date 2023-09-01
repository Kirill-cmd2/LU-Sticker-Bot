#remove pycache files from git control
#LU Stick: instead of deleting messages just change inline message
#write in working with photo and errors handler: with whom error occurred
# add inline cancel button
# function that will send image to admin, when admin sends id of photo
# update bot on server, install postgresql
# change the way of saving photo's id in creating
# replace emojis with unicode
# send user's log file to admin while requesting
# upload bot to github (every month on 1st)
# compare the Stick bot with other
# auto-deleting unnecessary messages
# moving back between handlers
# create webhook
# optimize working_with_photo - use IOBase instead of file saving
# change kirillic alphabet to latin one e.g. ф=f in correcr_name middleware
# find all emoji storage


from loader import DB, DP
import middlewares, filters, handlers


async def on_start(DP):
    try:
        DB.create_table()
    except Exception as err:
        print("An error:", err)


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
# 2.1.5 - removing creating_mention and writing_logs functions

__version__ = '2.1.4'
