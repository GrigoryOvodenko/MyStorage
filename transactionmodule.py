
import os
class TransactionCls:
    def __init__(self):
        self.transactionfile = "transactions.txt"
        self.namefile = "storage.txt"
    def commit_transaction(self):
        try:
            with open(self.transactionfile, "a") as file_:
                file_.write("commit")
                file_.write("\n")
            return True
        except:
            return False
    def define_transaction(self):
        with open(self.transactionfile, "r") as file_:
            data = file_.readlines()
        print("define_transaction:",data)
        file_.close()
        #  если последний элемент commit то транзакция закрыта
        if  data == [] or data[-2] =="commit" :
            return False
        else:
            return True
    def rollbacktrans(self):
        with open(self.transactionfile, "r") as file:
            data = file.readlines()
        with open(self.namefile, "r") as filem:
            readdata = filem.readlines()
        #print("readdata:",readdata)
        myd={}
        for myelem in readdata:
            myd[myelem.split(";")[0].split(":")[1]]=myelem.split(";")[1].split(":")[1]
        #
        # open(self.namefile, "w")
        print(myd)
        for i in range(len(data) - 1, -1, -1):
            #print(data[i], i)
            if data[i] == "commit\n":
                continue
            if data[i] == "---Transcation start---\n":
                break
            else:
                olddata = data[i]
                task = olddata.split(";")[0].split(":")[1]
                key = olddata.split(";")[1].split(":")[1]
                val = olddata.split(";")[2].split(":")[1]
                #print(task,key,val)
        #
        #

                if task == "putdata":
                    del myd[key]
                if task == "deldata":
                    myd[key]=val

        #             for el in readdata:
        #                     print(el)
        #                     oldk=el.split(";")[0].split(":")[1]
        #                     oldv = el.split(";")[1].split(":")[1]
        #                     if oldk == key:
        #
        #                         continue
        #                     else:
        #
        #                         with open(self.namefile, "a") as file_obj:
        #                             file_obj.write(el)
        #
        #             for el in readdata:
        #                     oldk=el.split(";")[0].split(":")[1]
        #                     oldv = el.split(";")[1].split(":")[1]
        #                     print("res:",oldk,oldv)
        #                     with open(self.namefile, "a") as file_obj:
        #                         file_obj.write(el)
        #             with open(self.namefile, "a") as file_obj:
        #                 file_obj.write("key:" + str(key) + ";value:" + str(val))
        #                 file_obj.write("\n")
        print(myd)
        open(self.namefile,"w")
        with open(self.namefile,"a")  as file_obj:
            for k in myd.keys():
                file_obj.write("key:" + str(k) + ";value:" + str(myd[k]))
