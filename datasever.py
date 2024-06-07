import datetime

def add_data(data):
    """
    Добавляет данные в файл. Записывает переданные данные и текущее время.
    """
    filename = f"{crypt()}.data"
    with open(filename, "a") as file:
        # Записываем данные, разделяя пробелами
        file.write(" ".join(map(str, data)) + " ")
        # Записываем текущее время
        current_time = datetime.datetime.now().strftime("%X")
        file.write(current_time + "\n")

def find_user_info(firstname, lastname):
    """
    Ищет информацию о пользователе в файле. Возвращает время, проведенное пользователем, и статус.
    """
    filename = f"{crypt()}.data"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()

        stats = []
        total_time = datetime.datetime.strptime("0:0:0", '%H:%M:%S')
        
        # Ищем строки, содержащие имя и фамилию пользователя
        for line in lines:
            if firstname in line and lastname in line:
                stats.append(line.split())
        
        for i, stat in enumerate(stats):
            if stat[4] == 's':  # Проверяем статус 's'
                try:
                    # Вычисляем разницу времени между записями
                    end_time_str = stats[i+1][6]
                    start_time_str = stat[6]
                    end_time = datetime.datetime.strptime(end_time_str, '%H:%M:%S')
                    start_time = datetime.datetime.strptime(start_time_str, '%H:%M:%S')
                    total_time += end_time - start_time
                except IndexError:
                    # Обрабатываем последний случай, если записи нет
                    start_time_str = stat[6]
                    start_time = datetime.datetime.strptime(start_time_str, '%H:%M:%S')
                    current_time_str = datetime.datetime.now().strftime("%X")
                    current_time = datetime.datetime.strptime(current_time_str, '%H:%M:%S')
                    total_time = current_time - start_time
                    return 1, total_time

        return str(total_time)[11:], 0

    except IOError:
        return "В файле нет записей", 0

def find_data(firstname, lastname):
    """
    Ищет последнюю запись о курении и еде пользователя в файле.
    """
    filename = f"{crypt()}.data"
    with open(filename, "a"):
        pass

    with open(filename, "r") as file:
        lines = file.readlines()

    # Ищем строки, содержащие имя и фамилию пользователя
    stats = [line.split() for line in lines if firstname in line and lastname in line]

    # Получаем последние значения курения и еды
    smokes = stats[-1][2] if stats else 0
    eats = stats[-1][3] if stats else 0

    return smokes, eats

def crypt():
    """
    Генерирует имя файла на основе текущей даты.
    """
    current_time = datetime.datetime.now()
    return f"{current_time.year}{current_time.day}{current_time.month}"
