from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

"""
class Post(models.Model): – この行が今回のモデルを定義します (これが オブジェクト です)。

classはオブジェクトを定義してますよ、ということを示すキーワードです。
Post はモデルの名前で、他の名前をつけることもできます（が、特殊文字と空白は避けなければいけません）。モデルの名前は大文字で始めます。
models.Model はポストがDjango Modelだという意味で、Djangoが、これはデータベースに保存すべきものだと分かるようにしています。
さて今度はプロパティを定義しましょう：title、text、created_date、published_date、それに author ですね。 それにはまずフィールドのタイプを決めなければいけません。（テキスト？ 数値？ 日付？ 他のオブジェクト、例えばユーザーとの関係？）

models.CharField – 文字数が制限されたテキストを定義するフィールド
models.TextField – これは制限無しの長いテキスト用です。ブログポストのコンテンツに理想的なフィールドでしょ？
models.DateTimeField – 日付と時間のフィールド
models.ForeignKey – これは他のモデルへのリンク
コードの細かいところまでは説明し出すと時間がかかるので、ここではしませんが、 モデルのフィールドや上記以外の定義のやり方について知りたい方は是非Djangoドキュメントを見てみて下さい。 (https://docs.djangoproject.com/ja/2.2/ref/models/fields/#field-types)

def publish(self): は何かと言うと、 これこそが先程お話ししたブログを公開するメソッドそのものです。 def は、これはファンクション（関数）/メソッドという意味です。publish はメソッドの名前で、 変えることもできます。 メソッドの名前に使っていいのは、英小文字とアンダースコアで、アンダースコアはスペースの代わりに使います。 （例えば、平均価格を計算するメソッドは calculate_average_price っていう名前にします）

メソッドは通常何かを return します。 一つの例が __str__ メソッドにあります。 このシナリオでは、__str__() を呼ぶと、ポストのタイトルのテキスト（string）が返ってきます。

def publish(self): と def __str__(self): の両方が class キーワードに続く行でインデントされているのに気づきましたか？ Pythonにモデルのメソッドだと伝えるために、class キーワードに続く行ではメソッドをインデントしましょう。 そうしないと、メソッドはモデルのものではなくなり、思ってもみない振る舞いをするでしょう。

もしモデルがまだはっきりつかめないようだったら、気軽にコーチに聞いて下さい！ 特にオブジェクトとファンクションを同時に習ったときはとても複雑なのはよく分かってますから。 でも前ほど魔法みたいじゃないといいですけど！

データベースにモデ"""