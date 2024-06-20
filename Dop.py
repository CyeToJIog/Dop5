import time

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f"{nickname}")
                return
        print("Неправильный логин или пароль")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video.title not in [v.title for v in self.videos]:
                self.videos.append(video)

    def get_videos(self, search_word):
        result = [video.title for video in self.videos if search_word.lower() in video.title.lower()]
        print(result)

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        found_video = next((video for video in self.videos if video.title.lower() == title.lower()), None)
        if found_video:
            if found_video.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return
            for second in range(found_video.duration):
                print(second + 1, end=' ', flush=True)
                time.sleep(1)
            print("Конец видео")


# Проверка кода
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
ur.get_videos('лучший')
ur.get_videos('ПРОГ')

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
