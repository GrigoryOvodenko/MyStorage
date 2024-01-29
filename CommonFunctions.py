import os

import datetime


class CommonCls:
    def __init__(self):
        self.namefile = "storage.txt"
        self.namefilelog = "logjournal.txt"
        self.transactionfile = "transactions.txt"
        self.namefileopentransstate = "opentransact.txt"
        self.bigstorage = "BigStorage.txt"

    # запись открыта ли транзакция
    def recordopentransact(self, flag):
        with open(self.namefileopentransstate, "w") as f:
            f.write(flag)

    # создание в случае необходимости файлов
    def create_files(self):
        if os.path.isfile(self.namefile) == False:
            open(self.namefile, "w")
        if os.path.isfile(self.namefilelog) == False:
            open(self.namefilelog, "w")
        # если файла нет, то создаем его
        if os.path.isfile(self.namefileopentransstate) == False:
            with open(self.namefileopentransstate, "w") as f:
                f.write("False")

        open(self.transactionfile, "w")

    # запись логов
    def writelog(self, task):
        with open(self.namefilelog, "a") as file_log:
            file_log.write(f"{task}")
            file_log.write("\n")

    # получить по ключу значение и проверить существует ли ключ+значение или нет
    def get_my(self, keysearch):
        with open(self.bigstorage, "r") as file_:
            data = file_.readlines()
        file_.close()
        for i in range(0, len(data), 1):
            key = data[i][4::].split(";")[0]

            val = data[i].split("value:")[1].replace("\n", "")

            if key == keysearch:
                return False, i, val
        return True, -1, -1

    # начинаем транзакцию
    def start_trans(self):
        with open(self.transactionfile, "a") as file_obj:
            file_obj.write("---Transcation start---")
            file_obj.write("\n")

    # перенос в итоговое хранилище транзакций и данных
    def transfertranscations(self):
        with open(self.transactionfile, "r") as file1:
            data = file1.readlines()
        with open("listTransaction.txt", "a") as f:
            for el in data:
                f.write(el)
        with open(self.namefile, "r") as fileresend:
            data_old_resend = fileresend.readlines()

        with open("BigStorage.txt", "w") as filereceive:
            filereceive.writelines(data_old_resend)

    # запись задачи
    def write_task(self, nametasktrans):
        with open(self.transactionfile, "a") as file_obj:
            file_obj.writelines(nametasktrans)
            file_obj.write("\n")

    # удаление данных
    def deletedata(self, ind, key, value):
        with open(self.namefile, "r") as file_:
            data = file_.readlines()

        new_result = [data[i] for i in range(len(data)) if i != ind]

        os.remove(f"{os.getcwd()}//{self.namefile}")  # remove old we have backup copy

        with open(self.namefile, "a") as file_obj:
            file_obj.writelines(new_result)
        file_obj.close()
        self.start_trans()
        self.write_task(f"task:deldata;key:{key};value:{value}")

        self.writelog(
            f"delete success key:{key} value:{value}-time {str(datetime.datetime.now())}"
        )

    # поиск ключей по значению
    def findkeysbyvalue(self, value):
        with open(self.bigstorage, "r") as file_:
            data = file_.readlines()
        file_.close()
        lst = []
        for i in range(0, len(data), 1):
            key = data[i][4::].split(";")[0]

            val = data[i].split("value:")[1].replace("\n", "")
            if val == value:
                lst.append(key)
        return lst

    # добавить новое
    def insdata(self, key, value):
        with open(self.namefile, "a") as file_log:
            file_log.write("key:" + str(key) + ";value:" + str(value))
            file_log.write("\n")
        file_log.close()

        self.write_task(f"task:putdata;key:{key};value:{value}")
        self.writelog(
            f"insert success key:{str(key)} value:{str(value)}-time {str(datetime.datetime.now())}"
        )
