# DS-Intern


Тестовое задание на позицию Intern DataScientist в VK


Была решена задача по оценке успешности объекта ритейлинга. Итоговый файл ответов на test.csv - final_submission.csv


В файла train.py и solution.py используются файлы prepared_train.csv и prepared_test.csv для ускорения работы. Эти файлы содержат конкатенацию исходных файлов с features.csv как усреднее показателей ближайших 5 объектов. Также в обработанных файлах содержится информация о городе, округе, численности населения города, в котором расположен объект, и использован тип объекта.


Для компиляции докер файла:
```make build```
Для запуска докер файла:
```make run```