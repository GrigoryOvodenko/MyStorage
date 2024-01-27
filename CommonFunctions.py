import os

import datetime


class CommonCls:
    def __int__(self,namefile,namefilelog):
        self.namefile = namefile
        self.namefilelog=namefilelog
    def create_file(self):
        if os.path.isfile(self.namefile) == False:
            open(self.namefile, "w")
    def writelog(self,task):
        with open(self.namefilelog, "a") as file_log:
            file_log.write(f"{task} {str(datetime.datetime.now())}")
            file_log.write("\n")
# при транзакции снимаем копию чтоб ресторнуть если что
    def define_transaction(self):
        pass

# get with key value and check exist key + value or not

    def get_my(self,keysearch):

        with open(self.namefile, "r") as file_:
            data = file_.readlines()
        file_.close()
        for i in range(0,len(data),1):
            key = data[i][4::].split(";")[0]

            val =data[i].split("value:")[1].replace("\n","")
            print(data[i],keysearch)
            if key == keysearch:

                return False,i,val
        return True,-1,-1


    def deletedata(self,ind):
        with open(self.namefile, "r") as file_:
            data = file_.readlines()

        new_result = [data[i] for i in range(len(data)) if i != ind]


        os.remove(f"{os.getcwd()}//{self.namefile}") # remove old we have backup copy
        print("DELETE SUCCESS")

        self.writelog( f"DELETE SUCCESS-TIME {str(datetime.datetime.now())}")
        with open(self.namefile, "a") as file_obj:
            file_obj.writelines(new_result)
        file_obj.close()
        print("UPDATE SUCCESS")
    #добавить новое


    def insdata(self,key,value):
        with open(self.namefile, "a") as file_log:
            file_log.write("key:" + str(key) + ";value:" + str(value))
            file_log.write("\n")
        file_log.close()
        self.writelog( f"INSERT SUCCESS-TIME {str(datetime.datetime.now())}")