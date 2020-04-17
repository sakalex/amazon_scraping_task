## Task for scraping Amazon offers-list page

### Запуск

> на компьютере должен быть установлен python 3.6 или выше

Скопируйте содержимое репозитория в папку на компьютере.

`git clone https://github.com/SokolDuck/amazon_scraping_task`

Откройте терминал(PowerShel для Windows) в папке с файлами.

`cd amazon_scraping_task`

Запустите последоватльно команды: 
1. Для Windows  
 - `pip install virtualenv`
 - `python -m venv env`
 - `.\env\Scripts\activate.bat`
 - `pip install -r requirements.txt`
 - `python main.py`
 - `.\env\Scripts\deactivate.bat`
2. Для Linux  
  - `pip3 install virtualenv`
  - `python3 -m venv env`
  - `source env/bin/activate`
  - `pip3 install -r requirements.txt`
  - `python3 main.py`
  
После удачного завершения выполнения программы в конволь выведится надпись "Task ended."

Файл с результатами работы будет лежать в папке files.

Для изменения начальной страницы для "скрапинга", надо заменить переменную _START_URL_ в файле _src/constants.py_

По умолчанию 
> START_URL = 'https://www.amazon.co.uk/AMD-Ryzen-3900X-Processor-Cache/dp/B07SXMZLP9/'
