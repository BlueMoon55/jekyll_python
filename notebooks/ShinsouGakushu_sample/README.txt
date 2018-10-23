
===============================================
サンプルデータをお使いになる前に必ずお読みください
===============================================

●サンプルデータについて
　サンプルデータには『Pythonで動かして学ぶ！あたらしい深層学習の教科書』の本文で解説した第2章から第22章のサンプルをJupyter Notebook形式で用意しています。

●本書のサンプルのテスト環境
　本書は以下の環境でサンプルを実行しています（本書のP.xiv参照）。

OS：Windows 10
Python：3.6.1
Anaconda：5.2.0
ブラウザ：Google Chrome

●ライブラリのインストール
　本書のP.2から7でAnaconda Navigatorをインストールしたら、P.8から9を参照して、Anaconda Navigator付属のコマンドプロンプトを起動して、P.11の方法で以下のコマンドを仮想環境上で実行します。

-------------------------------
conda install jupyter
conda install matplotlib==2.2.2
pip install scikit-learn==0.19.1
pip install tensorflow==1.5.0
pip install keras==2.2.0
-------------------------------

　その他、必要なライブラリは表 0.1 の通りですので、以下のコマンドで、インストールしてください（P.11参照）。

-------------------------------
conda install <ライブラリ名>==<バージョン名>
-------------------------------

ライブラリ名	バージョン名
-------------------------------
opencv	3.4.2
pandas	0.22.0
pydot	1.2.4
requests	2.19.1
▲表 0.1：ライブラリ名とバージョン名

●Anacondaのバージョン
　本書執筆時点（2018 年 9 月現在）では、「Anaconda3-5.2.0-Windows-x86_64.exe」を利用しています。図 0.1 で提供されているバージョンはダウンロード時期によって変わる可能性がありますが、最新版のものを利用すれば基本的に問題ありません。本書の環境に合わせる場合は、以下のサイトからバージョンを指定
してダウンロードしてください（本書のP.7参照）。

・Anaconda installer archive
 URL https://repo.continuum.io/archive/

●サンプルデータの一覧
　サンプルデータのフォルダ構成は次の通りです。

ShinsouGakushu_sample
    +-- Chapter2_sample.ipynb【第2章のサンプル】
    +-- Chapter3_sample.ipynb【第3章のサンプル】
    +-- Chapter4_sample.ipynb【第4章のサンプル】
    +-- Chapter5_sample.ipynb【第5章のサンプル】
    +-- Chapter6_sample.ipynb【第6章のサンプル】
    +-- Chapter7_sample.ipynb【第7章のサンプル】
    +-- Chapter8_sample.ipynb【第8章のサンプル】
    +-- Chapter9_sample.ipynb【第9章のサンプル】
    +-- Chapter10_sample.ipynb【第10章のサンプル】
    +-- Chapter11_sample.ipynb【第11章のサンプル】
    +-- Chapter12_sample.ipynb【第12章のサンプル】
    +-- Chapter13_sample.ipynb【第13章のサンプル】
    +-- Chapter14_sample.ipynb【第14章のサンプル】
    +-- Chapter15_sample.ipynb【第15章のサンプル】
    +-- Chapter16_sample.ipynb【第16章のサンプル】
    +-- Chapter17_sample.ipynb【第17章のサンプル】
    +-- Chapter18_sample.ipynb【第18章のサンプル】
    +-- Chapter19_sample.ipynb【第19章のサンプル】
    +-- Chapter20_sample.ipynb【第20章のサンプル】
    +-- Chapter21_sample.ipynb【第21章のサンプル】
    +-- Chapter22_sample.ipynb【第22章のサンプル】
    +--cleansing_data【第15章で利用する画像サンプル】
    +-- README.txt【本ファイル】

●免責事項
　付属データの記載内容は、2018 年 9 月現在の法令等に基づいています。
　付属データに記載された URL 等は予告なく変更される場合があります。
　付属データの提供にあたっては正確な記述につとめましたが、著者や出版社などのいずれも、その内容に対して何らかの保証をするものではなく、内容やサンプルに基づくいかなる運用結果に関してもいっさいの責任を負いません。
 　付属データに記載されている会社名、製品名はそれぞれ各社の商標および登録商標です。

●著作権等について
　付属データおよび会員特典データの著作権は、著者および株式会社翔泳社が所有しています。
　個人で使用する以外に利用することはできません。許可なくネットワークを通じて配布を行うこともできません。個人的に使用する場合は、ソースコードの改変や流用は自由です。商用利用に関しては、株式会社翔泳社へご一報ください。

2018 年 9 月
株式会社翔泳社　編集部