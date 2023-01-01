from datetime import datetime

def file_name():
    now = datetime.now()
    dtString = now.strftime('%d_%b_%Y_%H_%M_%S')
    return dtString

if __name__ == "__main__":
    print(file_name())