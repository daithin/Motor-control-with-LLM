import tornado.ioloop#tornadoイベントグループを管理するモジュール
#サーバの起動と非同期処理の核
import tornado.web#tornadoのWebフレームワーク機能を提供モジュール
#リクエストハンドラ、ルーティングなどを含む

#tornado.webの.RequestHandlerを継承　実際アクセスしたら表示される部分
class MainHandler(tornado.web.RequestHandler):
    def get(self):#getリクエストを処理
        self.write("""
        <html><body><form action="/" method="post">
        <input type="text" name="input">
        <input type="submit" value="Submit">
        </form></body></html>
        """)

    def post(self):
        user_input = self.get_body_argument("input", default="No input received")
        self.write(f"Received input: {user_input}")


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
