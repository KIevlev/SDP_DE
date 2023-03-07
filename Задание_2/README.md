# Задача 2
---
Базовая цель - найти потенциальные проблемы несовместимости
Дополнительная цель - предложить WA по решению несовместимостей для прикладных приложений.
---


## Решение

По результатам анализа release notes версий Spark 3.2.2 и 3.3.0
https://spark.apache.org/releases/spark-release-3-2-2.html

https://spark.apache.org/releases/spark-release-3-3-0.html

Были выявлены изменения, которые могут повлечь за собой несовместимости в некоторых прикладных приложениях.

### 1. Повышение версии Pandas


| Задача | Ссылка |
| ------ | ------ |
| PySpark tests failing on Pandas 0.23 | [https://issues.apache.org/jira/browse/SPARK-37465][pandas] |

##### Pandas 0.23 и 0.24 имеют обратно несовместимые изменения в API 

* Полный список несовместимостей можно посмотреть здесь <https://pandas.pydata.org/pandas-docs/version/0.24/whatsnew/v0.24.0.html#backwards-incompatible-api-changes>

##### WA: Создать базу методов, у которых изменилась сигнатура, найти, где они используются и изменить исходный код приложений.
---
### 2. Изменение версии log4j с 1 на 2

| Задача | Ссылка |
| ------ | ------ |
| Migrating from log4j 1 to log4j 2 | [https://issues.apache.org/jira/browse/SPARK-37814][log4j] |

##### WA: Изменение конфигурации log4j в дистрибутиве SDP Hadoop




   [pandas]: <https://issues.apache.org/jira/browse/SPARK-37465>
   [log4j]: <https://issues.apache.org/jira/browse/SPARK-37814>