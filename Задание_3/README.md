# Задача 3
---
1. Разверни однонодный Hadoop кластер. Как вариант используй docker образ cloudera.
2. Положи в hdfs любой .csv файл с данными
3. Создай в Hive таблицу над файлом из п.2


Результатом будет:
- csv и hql скрипты в GitHub
- скринкаст с select-ом таблицы из п.3
Результат выложить в гитхаб, решением будет ссылка в ответном сообщении.
---

Развернул кластер двумя способами:
 - C cloudera quickstart
 - С кастомным набором связанных контейнеров

Cloudera очень прожорливая, чтобы запустить все сервисы нужно более 12GB RAM

В docker-compose проброшены основные порты веб-интерфейсов компонентов дистрибутива.

После окончания процесса запуска рекомендуется зайти на машину  через команду docker exec -it $(docker ps | grep cloudera/quickstart:latest | awk '{print $1}') bash
и запустить cloudera manager

sudo /home/cloudera/cloudera-manager --express --force

После этого станет доступен основной веб-интерфейс service-manager'a

Второй вариант потребляет меньше памяти и работает стабильнее. Состоит из Namenode, Datanode, Hive, Hue.

В обоих вариантах пробросил директорию shared_cloudera_quickstart, где и лежат файлы csv и hql


Решил сделать нормальный SELECT-запрос к HIVE.
Такой же результат получил в SparkSQL и PySpark через rdd-преобразования.
Посмотреть можно в директории "Доп_работа"

Ссылки на скринкасты:

HIVE             https://disk.yandex.ru/i/NwrMH20axsk9Pg
SPARK SQL        https://disk.yandex.ru/i/hzLyQB4-ZX6FrA
PySpark (rdd)    https://disk.yandex.ru/i/HRIfbiRk7wWCvQ