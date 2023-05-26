<h1>TeamsToDo</h1>
<h2>Описание:</h2>
Сервис поиска ближайших машин для перевозки грузов.

<h2>Порядок установки:</h2>
Клонируем репозиторий:
	
	
	https://github.com/oneMayday/TeamsToDo.git
  
Запускаем проект командой:
	
	
	docker-compose up --build
  
<h2>Список эндпоинтов:</h2>


	0.0.0.0:8000/api/cargo

'GET' - получение списка грузов; Имеется фильтрация по весу
'POST' - создание нового груза (поля weight, description, pickup zip, delivery zip (почтовые индексы, берется из полей локации)


	0.0.0.0:8000/api/cargo/<int>/

'GET' - получение информации о конкретном грузе
'PUT', 'PATCH' - обновление информации о грузе (поля weight, description)
'DELETE' - удаление груза


	0.0.0.0:8000/api/location
  
'GET' - получение списка локаций


	0.0.0.0:8000/api/deliverycar
  
'GET' - получение списка машин

	0.0.0.0:8000/api/deliverycar/<int>/
  
'GET' - получение информации о машине
'PUT' - обновление информации о машине (поле current_location (zip -почтовый индекс, берется из полей локации)
