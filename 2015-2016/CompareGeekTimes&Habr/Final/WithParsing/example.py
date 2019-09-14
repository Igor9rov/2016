#http://docs.grablib.org/ru/latest/spider/tutorial.html
import urllib
import csv
import logging

from grab.spider import Spider, Task

class ExampleSpider(Spider):
    # Список страниц, с которых Spider начнёт работу
    # для каждого адреса в этом списке будет сгенерировано
    # задание с именем initial
    initial_urls = ['http://habrahabr.ru/']

    def prepare(self):
        # Подготовим файл для записи результатов
        # Функция prepare вызываетя один раз перед началом
        # работы парсера
        self.result_file = csv.writer(open('result.txt', 'w'))
        # Этот счётчик будем использовать для нумерации
        # найденных картинок, чтобы создавать им простые имена файлов.
        self.result_counter = 0

    def task_initial(self, grab, task):
        print('Habrahabr home page')

        # Это функция-обработчик для заданий с именем initial
        # т.е. для тех заданий, что были созданы для
        # адреов указанных в self.initial_urls

        # Как видите интерфейс работы с ответом такой же,
        # как и в обычном Grab
        for elem in grab.xpath_list('//h1[@class="title"]/a[@class="post_title"]'):
            # Для каждой ссылки-заголовка создадим новое задание
            # с именем habrapost
            # Обратите внимание, что мы создаём задания с помощью
            # вызова yield - это сделано исключительно ради красоты
            # По сути, это равносильно следующему коду:
            # self.add_task(Task('habrapost', url=...))
            yield Task('habrapost', url=elem.get('href'))

    def task_habrapost(self, grab, task):
        print ('Habrahabr topic: %s' % task.url)

        # Эта функция, как вы уже догадываетесь,
        # получает результаты обработки запросов, которые
        # мы создали для кадого хабратопика, найденного на
        # главной странице хабры

        # Для начала сохраним адрес и заголовк топика в словарь
        post = {
            'url': task.url,
            'title': grab.xpath_text('//h1/span[@class="post_title"]'),
        }

        # Теперь создадим поисковый запрос картинок яндекса, обратите внимание,
        # что мы передаём объекту Task информацию о хабрапосте. Таким образом
        # в функции обработки поиска картинок мы будем знать, для какого именно
        # хабрапоста мы получили результат поиска картинки. Дело в том, что все
        # нестандартные аргументы конструктора Task просто запоминаются в созданном
        # объекте и доступны в дальнейшем как его атрибуты
        query = urllib.quote_plus(post['title'].encode('utf-8'))
        search_url = 'http://images.yandex.ru/yandsearch?text=%s&rpt=image' % query
        yield Task('image_search', url=search_url, post=post)

    def task_image_search(self, grab, task):
        print ('Images search result for %s' % task.post['title'])

        # В этой функции мы получили результат обработки поиска картинок, но
        # это ещё не сама картинка! Это только список найденных картинок,
        # Теперь возьмём адрес первой картинки и создадим задание для её
        # скачивания. Не забудем передать информацию о хабрапосте, для которого
        # мы ищем картинку, эта информация хранится в `task.post`.
        image_url = grab.xpath_text('//div[@class="b-image"]/a/img/@src')
        yield Task('image', url=image_url, post=task.post)

    def task_image(self, grab, task):
        print ('Image downloaded for %s' % task.post['title'])

        # Это последнняя функция в нашем парсере.
        # Картинка получена, можно сохранить результат.
        path = 'images/%s.jpg' % self.result_counter
        grab.response.save(path)
        self.result_file.writerow([
            task.post['url'].encode('utf-8'),
            task.post['title'].encode('utf-8'),
            path
        ])
        # Не забудем увеличить счётчик ответов, чтобы
        # следующая картинка записалась в другой файл
        self.result_counter += 1


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # Запустим парсер в многопоточном режиме - два потока
    # Можно больше, только вас яндекс забанит
    # Он вас и с двумя то потоками забанит, если много будете его беспокоить
    bot = ExampleSpider(thread_number=2)
    bot.run()