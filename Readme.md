### Проект по созданию REST api для сайта ФСТР


#### Задание:

На сайте https://pereval.online/ ФСТР ведёт базу горных перевалов, которая пополняется туристами.

ФСТР заказала разработать мобильное приложение для Android и IOS, с помощью которого туристы 
могли бы отправлять данные о перевале.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять 
их в ФСТР, как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те 
в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

#### В ходе решения задания были выполнены такие задачи:

-Создание базы данных. База данных использовалась postgresql. Подключение к базе данных вынесено в переменные окружения:
FSTR_DB_NAME, FSTR_DB_LOGIN, FSTR_DB_PASS, FSTR_DB_HOST, FSTR_DB_PORT

-Создание классов по работе с данными, с помощью которых можно добавлять новые значения в таблицу перевалов
и рнедактировать сущестующие. 

-Написание REST API, который будет вызывать методы из классов по работе с данными.
* метод POST submitData/ - создание новой записи о перевале.
* метод GET /submitData/id_записи - получение записи о перевале по её id.
* метод PATCH /submitData/id_записи - редактирование записи о перевале, если она в статусе new.
* метод GET /submitData/?user__email=email_пользователя - получение записей обо всех перевалах, которые пользователь с почтой <email> 
отправил на сервер.

Пример JSON в теле запроса с информацией о перевале:

{

  "beauty_title": "пер. ",
  
  "title": "Пхия",
  
  "other_titles": "Триев",
  
  "connect": "", // что соединяет, текстовое поле
  
 
  "user": {"email": "qwerty@mail.ru", 
  
        "fam": "Пупкин",
	
        "name": "Василий",
   
        "otc": "Иванович",
   
        "phone": "+71112223344"}, 
 
   "coords":{
   
  "latitude": "45.3842",
  
  "longitude": "7.1525",
  
  "height": "1200"}
 
 
  level:{"winter": "", //Категория трудности. В разное время года перевал может иметь разную категорию трудности
  
  "summer": "1А",
  
  "autumn": "1А",
  
  "spring": ""},
 
   images: [{data:"https://example.jpg", title:"Седловина"}, {data:"https://example.jpg", title:"Подъём"}]
}
 
Приложение для работы с REST API было опубликовано на хостинге pythonanywhere.com
* вызов метода POST доступен по адресу http://myrsinsergey.pythonanywhere.com/submitData/
* вызов методов GET и PATCH доступен по адресу http://myrsinsergey.pythonanywhere.com/submitData/id_записи
* вызов метода GET для получения всех записей по определенному email доступен по адресу 
http://myrsinsergey.pythonanywhere.com//submitData/?user__email=email_пользователя