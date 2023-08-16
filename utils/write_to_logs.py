from datetime import datetime


async def writing_logs(chat_id, text:str):
    current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S   ")

    file = open('logs/' + str(chat_id) + '_log.txt', 'a', encoding='UTF-8')
    file.write(current_time + text + '\n')
    file.close()

    del current_time