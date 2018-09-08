全文検索システム『ひまわり』 ver.1.6 (2018-07-18)
Copyright 2004-2018 山口昌也(大学共同利用機関法人 人間文化研究機構 国立国語研究所)

１．本パッケージの内容
　- Corpora/     ... 資料格納用フォルダ
                 ... jitaidic.xml (字体辞書)
  - jre/         ... JRE ver.1.8.0_181 (Windows 32bit版)
　- resources/   ... テキストインポート機能用ファイル

  - README.txt   ... このファイル
  - copyright.txt   ... 著作権および使用条件

  - config.xml   ... 『ひまわり』設定ファイル(config_aozora_sample.xmlと同一)
  - config_aozora_sample.xml    (全文検索のみ)
    config_aozora_sample.sd.xml (形態素解析結果付き)
                 ... 『ひまわり』設定ファイル(『青空文庫』サンプル用)

  - himawari.bat ... 『ひまわり』プログラム (Windows 専用/オプション見本)
  - himawari.exe ... 『ひまわり』プログラム (Windows 専用)
  - himawari_debug.exe
                 ... 『ひまわり』プログラム(Windows 専用/デバッグ用出力あり)
  - himawari.jar ... 『ひまわり』プログラム (Mac, Linux, Windows 共用)

  - .himawari_annotator_config.xml 
                 ... 形態素解析システムなどの外部アノテータの設定
  - .himawari_import_config.xml
                 ... インポート時の設定


２．利用方法
  - 利用方法は，『ひまわり』のホームページをご覧ください。
    (http://www2.ninjal.ac.jp/lrc の全文検索システム『ひまわり』)

  - ご使用にあたっては，著作権および使用条件に関する文書
    (copyright.txt)をお読みください。


３．変更履歴
　履歴のページを参照して下さい。

http://www2.ninjal.ac.jp/lrc/index.php?%C1%B4%CA%B8%B8%A1%BA%F7%A5%B7%A5%B9%A5%C6%A5%E0%A1%D8%A4%D2%A4%DE%A4%EF%A4%EA%A1%D9%2F%CD%FA%CE%F2


４．その他
  - 最新情報は，大学共同利用機関法人 人間文化研究機構 国立国語研究所
    の Web ページ（http://www2.ninjal.ac.jp/lrc/）で公開しています。
  - 不具合のご報告，ご意見などについては，himawari@ninjal.ac.jp までお
    願いいたします。お返事の約束はいたしかねますが，今後の開発に活用
    させていただきます。

　- 本パッケージの jre フォルダには，Windows 版 JRE が含まれています。
    これらのフォルダ中のファイルの著作権は，Oracle が保持しています。
    詳しくは，jre フォルダ 中の LICENSE, README.txt などをご覧ください。

　- 本パッケージの作成にあたっては，次のソフトウェア，および，デー
    タ，団体の支援を受けました。関係者の方々に深く感謝いたします。

    -- 『ひまわり』のアノテーション機能では，データの格納に H2
        (http://www.h2database.com/html/main.html) を使用しています。

        This software contains unmodified binary redistributions for
        H2 database engine (http://www.h2database.com/), which is dual
        licensed and available under the MPL 2.0 (Mozilla Public
        License) or under the EPL 1.0 (Eclipse Public License). An
        original copy of the license agreement can be found at:
        http://www.h2database.com/html/license.html

    -- himawari.exe は，himawari.jar を launch4j
       (http://launch4j.sourceforge.net/) で exe 形式に変換
       しました。
    -- jitaidic.xml は，高田智和氏（国立国語研究所）が作成したデー
       タをもとに作成しました。
    -- 『ひまわり』ver.1.3 開発の一部は，『博報「ことばと文化・教育」研
       究助成』(http://www.hakuhodo.co.jp/foundation/)を受けて行われま
       した。
    -- 『青空文庫』サンプルは，『青空文庫』(http://www.aozora.gr.jp)の
       収録作品を利用させていただきました。
    -- 『ひまわり』ver.1.5 開発の一部は，国立国語研究所共同研究プロジェ
       クト「文脈情報に基づく複合的言語要素の合成的意味記述に関する研究」
       の一貫として行ないました。
    -- 『ひまわり』ver.1.6 開発の一部は，国立国語研究所共同研究プロジェ
       クト「大規模日常会話コーパスに基づく話し言葉の多角的研究」，お
       よび，科研費基盤研究(B)『「昭和話し言葉コーパス」の構築による話
       し言葉の経年変化に関する実証的研究』(16H03426)の一環で行いまし
       た。
