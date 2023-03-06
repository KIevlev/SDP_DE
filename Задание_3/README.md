start
docker-compose up --build

В docker-compose проброшены основные порты веб-интерфейсов компонентов дистрибутива.

После окончания процесса запуска рекомендуется зайти на машину  через команду docker exec -it $(docker ps | grep cloudera/quickstart:latest | awk '{print $1}') bash
и запустить cloudera manager

sudo /home/cloudera/cloudera-manager --express --force

После этого станет доступен основной веб-интерфейс service-manager'a