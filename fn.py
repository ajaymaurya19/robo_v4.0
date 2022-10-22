from datetime import datetime

def file_name():
    now = datetime.now()
    dtString = now.strftime('%d_%b_%Y_%H:%M:%S')
    return dtString