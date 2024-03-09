
# タスク管理くん

LINEと連携したタスク管理ツールです<br>
LINEのBotにメッセージを送ってタスクを追加できます<br>
追加したタスクはWebサイトで管理することができます<br>
<a href="https://mi8150jo.com">Webタスク管理くん</a>

![](webscreen.png)
<br>
ログイン前の画面<br>

![](webscreenlogin.png)
ログイン後の画面<br>

# 使用技術

## 主な使用技術一覧
<table>
    <!-- ヘッダ -->
    <tr>
        <td>言語</td>
        <td>ライブラリ・フレームワーク</td>
        <td>ミドルウェア</td>
        <td>エディタ</td>
        <td>クラウド</td>
    </tr>
    <!-- ボディ -->
    <tr>
    <!-- 言語 -->
        <td>
            <img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat">
            <br>
            <img src="https://img.shields.io/badge/-CSS3-1572B6.svg?logo=css3&style=flat">
            <br>
            <img src="https://img.shields.io/badge/-HTML5-333.svg?logo=html5&style=flat">
        </td>
    <!-- ライブラリ・フレームワーク -->
        <td>
            <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=flat">
            <br>
            <img src="https://img.shields.io/badge/-DjangoAllauth-092E20.svg?logo=django&style=flat">
            <br>
            <img src="https://img.shields.io/badge/-Bootstrap-563D7C.svg?logo=bootstrap&style=flat">
            <br>
        </td>
    <!-- ミドルウェア -->
        <td>
            <img src="https://img.shields.io/badge/-Nginx-269539.svg?logo=nginx&style=flat">
            <br>
            <img src="https://img.shields.io/badge/Sqlite3-%2307405e.svg?logo=sqlite&style=flat">
            <br>
            <img src="https://img.shields.io/badge/-Gunicorn-199848.svg?logo=gunicorn&style=flat">
        </td>
    <!-- エディタ -->
        <td>
            <img src="https://img.shields.io/badge/-Visual%20Studio%20Code-007ACC.svg?logo=visual-studio-code&style=flat">
        </td>
    <!-- クラウド -->
        <td>
            <img src="https://img.shields.io/badge/-Amazon%20aws-232F3E.svg?logo=amazon-aws&style=flat">
        </td>
    </tr>
  </table>

## requirements.txt
asgiref==3.7.2<br>
certifi==2024.2.2<br>
cffi==1.16.0<br>
charset-normalizer==3.3.2<br>
cryptography==42.0.5<br>
defusedxml==0.7.1<br>
Django==5.0.1<br>
django-allauth==0.61.0<br>
django-bootstrap5==23.4<br>
django-debug-toolbar==4.3.0<br>
gunicorn==21.2.0<br>
idna==3.6<br>
oauthlib==3.2.2<br>
packaging==23.2<br>
pycparser==2.21<br>
PyJWT==2.8.0<br>
pysqlite3==0.5.2<br>
pysqlite3-binary==0.5.2.post3<br>
python-dateutil==2.8.2<br>
python-decouple==3.8<br>
python3-openid==3.2.0<br>
requests==2.31.0<br>
requests-oauthlib==1.3.1<br>
six==1.16.0<br>
sqlparse==0.4.4<br>
urllib3==2.2.1<br>

## AWS構成図
![](aws.png)

# 機能一覧
<ul>
    <li>Lineログイン機能</li>
    <li>LineBotの応答からタスク追加</li>
    <li>Lineのユーザー名表示</li>
    <li>Lineのアイコン表示</li>
    <li>CRUD</li>
    <ul>
        <li>タスクの表示</li>
        <li>タスクをクリックして詳細表示</li>
        <li>タスクの削除</li>
        <li>タスクの編集</li>
        <li>タスクの追加</li>
        <li>過去のタスク表示（今日より前のタスク)</li>
        <li>過去のタスク追加</li>
    </ul>

</ul>
