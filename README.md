## Приложение классификации изображений

Это веб-приложение, созданное с использованием Django, которое выполняет классификацию изображений с использованием предварительно обученной модели ResNet-50 из torchvision. Пользователи могут загружать изображения, и приложение будет классифицировать изображение в один из классов ImageNet.

### Возможности
*    Загрузка изображения для классификации.
*    Отображение ширины, высоты и названия класса загруженного изображения.
*    Возможность загрузить другое изображение для классификации.

### Установка
1. Клонируйте репозиторий и перейдите в каталог:
   ```bash
   git clone https://github.com/NViQ/Image_classification.git
   cd image_classification

2. Установка зависимостей:
    
    ```bash
   pip install -r requirements.txt

### Использование
1. Запуск сервера из корневого каталога приложения:
   ```bash
   python manage.py runserver

2. Откройте веб-браузер и перейдите по адресу http://localhost:8000/, чтобы получить доступ к приложению.

3. Загрузите изображение, используя кнопку "Выбрать файл".

   P.S. можно выбрать из имеющихся в репозитории

4. Нажмите кнопку "Upload", чтобы начать процесс классификации изображения.

5. Приложение отобразит ширину, высоту и название класса загруженного изображения.

6. Чтобы загрузить другое изображение, нажмите ссылку "Upload Another Image".
