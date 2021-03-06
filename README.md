apple.com/ru/ UI Testing project
========================
Небольшой проект, написаный для изучения автоматизированного UI тестирования
-------------------------
При его создании не ставилась цель обеспечить максимальное покрытие и рассмотреть все возможные кейсы. Просто небольшой пример кода.
-------------------------
Используемый стэк: 
* Python 3.8.1
* Pytest 5.4.3
* Selenium 3.141.0
* Allure-pytest 2.8.16
* Pytest-xdist 1.34.0
* Docker 19.03.12
* Docker-compose 1.26.2
* Selenoid 1.10.0
* Allure Docker Service
***
Для того, чтобы запустить проект с помощью селеноида требуется установить Docker и Docker-compose. Запустить проект в селеноиде можно как из папки проекта, так и из собранного проекта в докер-контейнере под названием tests.

Для того чтобы собрать и запустить контейнеры, откройте команду строку, перейдите в директорию проекта и введите:
>docker-compose up -d

Для того чтобы остановить и удалить контейнеры введите:
>docker-compose down

Пример команды запуска тестов в докер контейнере с помощью селеноида в командной строке:
>docker exec tests pytest --alluredir=allure_results -n 5

Пример команды для запуска тестов в докер контейнере с помощь селеноида в Docker CLI: 
>pytest --alluredir=allure_results -n 5

Чтобы посмотреть собранный отчет allure, перейдите по ссылке:
>http://localhost:5050/allure-docker-service/latest-report

Чтобы собрать allure отчет в html-файл локально - после завершения работы проекта введите в командную строку
>allure serve allure_results
***
Для того, чтобы запустить проект локально требуется, чтобы на хосте были установлены требуемые вебдрайверы и прописаны к ним переменные окружения, либо прописать путь к драйверам в коде, установлен python 3.8.1, также должны быть установленны все зависимости с помощью команды pip install -r requirements.txt, а также прописать параметр запуска --executor local

Пример команды запуска проекта локально:
>pytest --executor "selenoid" --browser "chrome" --alluredir=allure_results -n 5
***
Параметры запуска проекта
> --browser по умолчанию стоит chrome, принимает chrome, firefox, opera
>
> --executor по умолчанию стоит selenoid, принимает local, selenoid
>
> -n [num] - количество потоков, при работе в селеноиде не использовать больше пяти
>
Дополнительные параметры для селеноида:
> --vnc по умолчанию disable, принимает enable, disable
>
> --video по умолчанию disable, принимает enable, disable
>
Чтобы allure вел отчет - в параметрах запуска передайте параметр:
>--alluredir=allure_results
>

Allure Docker Service ведет постоянную сборку allure отчетов. После каждого прогона тестов можно перейти по ссылке указанной ниже и получить полный отчет с графиками и таймлайном.
>http://localhost:5050/allure-docker-service/latest-report

P.S. Чтобы отчет велся обязательно в параметрах запуска передавайте параметр --alluredir=allure_results
***



