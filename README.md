<h2>Ссылка на задание:</h2>
https://faint-adasaurus-4bc.notion.site/web-Python-Middle-c1467cf373c24f0cafb8bfe0fe77cc79
<h2>Описание:</h2>
Сервис поиска ближайших машин для перевозки грузов.

<h2>Порядок установки:</h2>
Клонируем репозиторий:
	
	
	https://github.com/oneMayday/Welbex_test_backend.git
  
Запускаем проект командой:
	
	
	docker-compose up --build
  
  
При запуске контейнера проиходит автоматическое заполнение базы данных: создается 20 машин со случайным местонахождением и происходит парсинг и заполнение таблицы локаций. Также, раз в 3 минуты происходит обновление координат автомобилей.

<h2>Список эндпоинтов:</h2>


	0.0.0.0:8000/api/cargo

'GET' - получение списка грузов; Имеется фильтрация по весу <br>
'POST' - создание нового груза (поля weight, description, pickup zip, delivery zip (почтовые индексы, берется из полей локации)


	0.0.0.0:8000/api/cargo/<int>/

'GET' - получение информации о конкретном грузе <br>
'PUT', 'PATCH' - обновление информации о грузе (поля weight, description) <br>
'DELETE' - удаление груза


	0.0.0.0:8000/api/location
  
'GET' - получение списка локаций


	0.0.0.0:8000/api/deliverycar
  
'GET' - получение списка машин

	0.0.0.0:8000/api/deliverycar/<int>/
  
'GET' - получение информации о машине <br>
'PUT' - обновление информации о машине (поле current_location (zip -почтовый индекс, берется из полей локации)) <br>

<h2>PS:</h2>
1) В задании есть недочёт - в тексте указано: "Получение списка грузов (локации pick-up, delivery, количество ближайших машин до груза ( =< 450 миль))", т.е. подразумевается наличие полей pickup, delivery, cars_nearby, однако, дальше следует: "Фильтр списка грузов (вес, мили ближайших машин до грузов)", что подразумевает поля weight и distance. Фильтрацию реализовал, но эти поля в список грузов не добавлял.


<details>
<summary><h2> PSS: </h2></summary>
<br>
Реализовал всё, кроме фильтрации по расстоянию до груза. <br>
Скорее всего, данное тестовое задание мне прислали по ошибке, поскольку коммерческого опыта, за исключением фриланса, у меня нет :) <br>
Постарался реализовать максимально качественно, не хватило только времени написать тесты. Также, понимаю, что аггрегация полей distance и cars_nearby сделана не оптимально и сильно нагружает базу, порождая много запросов, на данный момент разбираюсь в этом вопросе, как сделать хорошо :). <br>
Буду рад любому фидбеку, спасибо за внимание!
</details>

