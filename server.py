import tornado.ioloop#tornadoイベントグループを管理するモジュール
#サーバの起動と非同期処理の核
import tornado.web#tornadoのWebフレームワーク機能を提供モジュール
#リクエストハンドラ、ルーティングなどを含む

#tornado.webの.RequestHandlerを継承
class MainHandler(tornado.web.RequestHandler):
    def get(self):#getリクエストを処理
        self.write("Hello, world!")#hello.worldを返す

#tornado.web.のApplicationクラスのインスタンスを作成
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),#ルートパスと対応するハンドラをマッピング
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # サーバはポート8888でリッスンします
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()  # サーバを起動し、リクエストを待機します
