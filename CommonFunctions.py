import os

import datetime


class CommonCls:
    def __init__(self,namefile,namefilelog,transactionfile,namefileopentransstate):
        self.namefile = namefile
        self.namefilelog=namefilelog
        self.transactionfile=transactionfile
        self.namefileopentransstate=namefileopentransstate
    def create_files(self):
        if os.path.isfile(self.namefile) == False:
            open(self.namefile, "w")
        if os.path.isfile(self.namefilelog) == False:
            open(self.namefilelog, "w")

        if os.path.isfile(self.namefileopentransstate) == False:
            with open(self.namefileopentransstate, "w") as f:
                f.write("False")
        open(self.transactionfile, "w")
    def writelog(self,task):
        with open(self.namefilelog, "a") as file_log:
            file_log.write(f"{task}")
            file_log.write("\n")




# get with key value and check exist key + value or not

    def get_my(self,keysearch):

        with open(self.namefile, "r") as file_:
            data = file_.readlines()
        file_.close()
        for i in range(0,len(data),1):
            key = data[i][4::].split(";")[0]

            val =data[i].split("value:")[1].replace("\n","")

            if key == keysearch:

                return False,i,val
        return True,-1,-1

    def write_task(self,nametasktrans):
        with open(self.transactionfile, "a") as file_obj:
            file_obj.writelines(nametasktrans)
            file_obj.write("\n")
    def deletedata(self,ind,key,value):
        with open(self.namefile, "r") as file_:
            data = file_.readlines()

        new_result = [data[i] for i in range(len(data)) if i != ind]


        os.remove(f"{os.getcwd()}//{self.namefile}") # remove old we have backup copy



        with open(self.namefile, "a") as file_obj:
            file_obj.writelines(new_result)
        file_obj.close()


        self.write_task("task:deldata")

        self.writelog( f"delete success key:{key} value:{value}-time {str(datetime.datetime.now())}")

    def findkeysbyvalue(self,value):
        with open(self.namefile, "r") as file_:
            data = file_.readlines()
        file_.close()
        lst = []
        for i in range(0, len(data), 1):
            key = data[i][4::].split(";")[0]

            val = data[i].split("value:")[1].replace("\n", "")
            if val == value:
                lst.append(key)
        return lst

    #добавить новое
    def insdata(self,key,value):
        with open(self.namefile, "a") as file_log:
            file_log.write("key:" + str(key) + ";value:" + str(value))
            file_log.write("\n")
        file_log.close()
        self.write_task("task:putdata")
        self.writelog( f"insert success key:{str(key)} value:{str(value)}-time {str(datetime.datetime.now())}")