Задача:Необходимо спроектировать и реализовать веб-приложение с использованием языка Python.

Приложения представляет собой хранилище “ключ-значение” с сохранением загруженных данных при помощи файлов операционной системы. 

Поддерживает следующие операции:
сохранить значение по ключу;
получить значение по ключу;
удалить значение по ключу;
найти все ключи, у которых значения равны искомому;
открыть транзакцию (можно открыть вложенные одна в другую транзакции, как матрешка);
сделать роллбэк (откатывается последняя транзакция);
сделать коммит (коммитятся все вложенные транзакции).



Task: It is necessary to design and implement a web application using the Python language.

The application is a key-value store with saving loaded data using operating system files.

Supports the following operations:
save a value by key;
get a value by key;
delete a value by key;
find all keys whose values ​​are equal to the desired one;
open a transaction (you can open transactions nested one inside another, like a Russian doll);
make a rollback (the last transaction is rolled back);
make a commit (all nested transactions are committed).



1. Данное приложение состоит из нескольких файлов:
main.py (запуск приложения,API,связанные с открытие транзакции и чтением),transactionsapi.py(API,связанные с записью),models.py(первичная валидация типов входных данных),
CommonFunctions.py(функции обработки,проверки и вывода,общие функции)
Для написания программ были использованы : Python,Fast Api.
Для форматирования кода:black
2. Для запуска api в консоли введите:
uvicorn main:app --port 8000
uvicorn transactionsapi:app1 --port 5000
3. BigStorage.txt -используется для поиска данных; listTransaction.txt- итоговое хранилище транзакциий;logjournal.txt-логирование действий
4. opentransact.txt - используется для проверка состояния транзакции(открыта или нет)
5. transactions.txt - список временный транзакций не перемещенных  в итоговое хранилище
6. storage.txt -временное хранилище даты до переноса
7. Для задач записи имеет значение открыта транзакция или нет ,поэтому происходит проверка флага(открыта транзакция или нет)
8. В случае с задачи чтения,это не имеет значения так как мы работаем только с хранилищем финальным



1.This application consists of several files: main.py (application launch, APIs related to opening a transaction and reading), transactionssapi.py (APIs related to writing), models.py (primary validation of input data types), CommonFunctions.py ( processing, checking and output functions, general functions) .
The following were used to write programs: Python, Fast Api.
To format the code: black </br>
2.To run the api in the console, enter: uvicorn main:app --port 8000 uvicorn transactionsapi:app1 --port 5000  </br>
3.BigStorage.txt - used to search for data; listTransaction.txt - final transaction storage; logjournal.txt - logging of actions  </br>
4.opentransact.txt - used to check the status of the transaction (open or not)  </br>
5.transactions.txt - list of temporary transactions not moved to the final storage  </br>
6.storage.txt - temporary date storage before transfer  </br>
7.For recording tasks, it matters whether the transaction is open or not, so the flag is checked (whether the transaction is open or not)  </br>
8.In the case of reading tasks, this does not matter since we only work with the final storage  </br>
