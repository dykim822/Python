import threading, requests, time
class HtmlGet(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
    def run(self) -> None:
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url)
        print(resp.text)
print('소스를 보고 싶은 url')
url = input()
th = HtmlGet(url)
th.start()