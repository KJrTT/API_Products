# Скриншоты работы программы

## Начальный экран
<img width="1007" height="441" alt="image" src="https://github.com/user-attachments/assets/5bb16792-160f-4a4d-949a-91c01de798e8" />


----

## Swagger

<img width="1218" height="754" alt="image" src="https://github.com/user-attachments/assets/8b616eae-91be-4ad6-9ff3-3cdcb874afb9" />

## Get-запросы

<img width="1168" height="926" alt="image" src="https://github.com/user-attachments/assets/a9e20796-83f7-4437-b491-2433efba1ea1" />
<img width="1153" height="796" alt="image" src="https://github.com/user-attachments/assets/c8c18d66-8f07-4070-a4b1-d99684971101" />

## Post-запрос

<img width="1167" height="878" alt="image" src="https://github.com/user-attachments/assets/c8a3a4ed-a3c1-4945-a7bd-0cc9ab437f0c" />

## Put-запрос

<img width="1163" height="963" alt="image" src="https://github.com/user-attachments/assets/4652aab1-cdab-448a-b0e0-7312c2d5f27b" />

## Delete-запрос

<img width="1177" height="651" alt="image" src="https://github.com/user-attachments/assets/2d6cb840-5a04-4b2c-8dbf-1cad0dea5cd3" />


#Запуск приложения

1. 
```
git clone https://github.com/KJrTT/API_Products.git

```

2. win + r => cmd + жмём enter

3. cd до нужной папки

4. python -m venv venv

5. Пишем эти команды 5.1 cd venv / 5.2 cd Scripts / 5.3 Activate

6. Переходим в папку backend

7. Команда для установки нужных библиотек
```
pip install -r requirements.txt

```
8. После установки в той же папки пишем
```
uvicorn main:app --reaload
```
