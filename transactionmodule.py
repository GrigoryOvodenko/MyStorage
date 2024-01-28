

class TransactionCls:
    def __init__(self):
        self.transactionfile = "transactions.txt"
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