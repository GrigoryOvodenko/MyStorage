
from functools import lru_cache
import requests
def define_transaction():
    pass

# get with key value and check exist key + value or not
@lru_cache(maxsize=32)
def get_my(namefile,keysearch):

    with open(namefile, "r") as file_:
        data = file_.readlines()

    for i in range(0,len(data),1):
        key = data[i][4::].split(";")[0]

        val =data[i].split("value:")[1].replace("\n","")

        if key == keysearch:

            return False,i
    return True,-1
