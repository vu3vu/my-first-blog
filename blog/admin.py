from django.contrib import admin
from .models import Post

admin.site.register(Post)

"""
見て分かる通り、前回定義したPostモデルをimportしています。 
モデルをAdminページ（管理画面）上で見えるようにするため、admin.site.register(Post)でモデルを登録する必要があります。

ではPostモデルを見てみましょう。 Web サーバーを実行するコンソールで python manage.py runserver を実行してください。 
ブラウザに行って http://127.0.0.1:8000/admin/ とアドレスバーにタイプします。 こんなログインページが出ますね。

ログインするには、superuser （サイトの全てを管理するユーザー）を作る必要があります。 
コマンドラインに戻り、python manage.py createsuperuser と入力し、enter キーを押します。
"""