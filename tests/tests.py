from conftest import *


def test_all_pets_have_different_names(go_to_my_pets):
    """Поверяем, что у всех питомцев на странице с моими питомцами разные имена """

    # В переменную pet_data сохраняем элементы с данными о питомцах
    pet_data = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    # Перебираем данные из pet_data, оставляем имя, возраст и породу, остальное меняем на пустую строку
    # И разделяем по пробелу. Выбираем имена и добавляем их в список pets_name.
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    # Перебираем имена, если имя повторяется, то прибавляем единицу к счетчику r.
    # Проверяем, если r == 0, то повторяющихся имен нет.
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0
    print(f'\n {r}')
    print(f'\n {pets_name}')


def test_all_pets_are_present(go_to_my_pets):
    """Проверяем, что на странице со списком моих питомцев есть питомцы"""

    # Сохраняем в переменную statistic элементы статистики
    statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")

    # Сохраняем в переменную pets элементы карточек питомцев
    pets = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    # Количество питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Количество карточек питомцев
    number_of_pets = len(pets)

    # Проверяем, что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == number_of_pets


def test_no_duplicate_pets(go_to_my_pets):
    """Поверка, что на странице со списком моих питомцев нет повторяющихся питомцев"""

    # Сохраняем в переменную pet_data элементы с данными о питомцах
    pet_data = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    # Перебираем данные из pet_data, оставляем имя, возраст и породу, остальное меняем на пустую строку
    # и разделяем по пробелу.
    list_data = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)

    # Соединяем имя, возраст и породу, получившиеся слова добавляем в строку
    # и между ними вставляем пробел
    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '

    # Получаем список из строки line
    list_line = line.split(' ')

    # Превращаем список в множество
    set_list_line = set(list_line)

    # Находим количество элементов списка и множества
    a = len(list_line)
    b = len(set_list_line)

    # Из количества элементов списка вычитаем количество элементов множества
    result = a - b

    # Если количество элементов == 0, то карточки с одинаковыми данными отсутствуют
    assert result == 0


def test_photo_availability(go_to_my_pets):
    """Поверка, что на странице со списком моих питомцев хотя бы у половины питомцев есть фото"""

    # Сохраняем в переменную statistic элементы статистики
    statistic = pytest.driver.find_elements_by_css_selector(".\\.col-sm-4.left")

    # Сохраняем в переменную images элементы с атрибутом img
    images = pytest.driver.find_elements_by_css_selector('.table.table-hover img')

    # Количество питомцев из данных статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Находим половину от количества питомцев
    half = number // 2

    # Находим количество питомцев с фотографией
    number_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_photos += 1

    # Проверка, что количество питомцев с фотографией больше или равно половине от количества питомцев
    assert number_photos >= half
    print(f'\nКоличество фото: {number_photos}')
    print(f'\nПоловина от числа питомцев: {half}')


def test_show_my_pets(go_to_my_pets):
    """Проверка, что мы находимся на странице Мои питомцы"""

    # Нажимаем на ссылку "Мои питомцы"
    pytest.driver.find_element_by_link_text("Мои питомцы").click()

    # Проверка, что мы находимся на странице "Мои питомцы"
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'


def test_there_is_a_name_age_and_gender(go_to_my_pets):
    """Поверка, что на странице со списком моих питомцев, у всех питомцев есть имя, возраст, фото и порода"""

    # Сохраняем в переменную pet_data элементы с данными о питомцах
    pet_data = pytest.driver.find_elements_by_css_selector('.table.table-hover tbody tr')

    # Перебираем данные из pet_data, оставляем имя, возраст и породу, остальное изменяем на пустую строку
    # и разделяем пробелом. Находим количество элементов в получившемся списке и сравниваем их
    # с ожидаемым результатом
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        result = len(split_data_pet)
        assert result == 3
        assert pet_data[i].get_attribute('src') != ''
