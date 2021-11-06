class Interval:

    # когда ты пишешь self ты просишь класс переменную с каким-то именем
    # если ты указала self - то менять перемнную можно в любом методе
    def __init__(self, first_point, last_point):
        self.first_point = first_point
        self.last_point = last_point

    def empty(self):
        if self.first_point == None and self.last_point == None:
            return True
        return False

    def cross(self, other):

        print(other.first_point)

    # vcs
    # share project on github
    # https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

    # Create git repository (optional)
    # Ctrl + K  (и 1 и 2 фаза)
    # Ctrl + shift + k




    # 3 фазы
    # 1 (выбираешь файлы для архива) git add - выбираешь файлы которые хочешь запомнить
    # 2 (создаёшь архив) git commit - фиксируешь изменения локально и пишешь комментарий почему ты изменила эти фалы (делаешь коммит - можно рассматривать как архив)
    # 3 (отправляешь архив на гихаб) git push - отправляешь коммит в гитхаю

    # 1
    # добавить в stage area
    # ctrl + K

    # i = Interval(None, None)
    # k = Interval(4, 8)
    # print(i.empty())
    # print(k.empty())


a = Interval(4, 10)
b = Interval(6, 11)
a.cross(b)
