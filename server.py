import tornado.ioloop#tornadoイベントグループを管理するモジュール
#サーバの起動と非同期処理の核
import tornado.web#tornadoのWebフレームワーク機能を提供モジュール
#リクエストハンドラ、ルーティングなどを含む
import os

#tornado.webの.RequestHandlerを継承　実際アクセスしたら表示される部分
class MainHandler(tornado.web.RequestHandler):
    def get(self):#getリクエストを処理
        self.render("index.html")#render関数はtornadoのrequestHandlerクラスのメソッド
        #テンプレートファイルを読み込んで、HTMLとしてクライアントに送信できる。（必要なデータだけ選ぶことも可能）

    def post(self):
        user_input = self.get_body_argument("input", default="No input received")
        self.write(f"Received input: {user_input}")#入力されたinputの中身を表示、なければno input received


#tornado.web.のApplicationクラスのインスタンスを作成
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),#ルートパスと対応するハンドラをマッピング
        #メインハンドラがそのままなら、/、違うならまた別で違う対応関数を書いてあげる
    ],
    template_path=os.path.join(os.path.dirname(__file__),"Web_page")#renderで指定するテンプレートフォルダの場所の初期設定
    )

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # サーバはポート8888でリッスンします
    print("Server running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()  # サーバを起動し、リクエストを待機します
