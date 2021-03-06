# リファクタリングの定義

外からの振る舞いを変えずにソフトウェアをわかりやすくし、安いコストで変更できるようにするために、ソフトウェアの内部構造に加えられる変更。

=> 可読性・変更性を高めること

# リファクタリングする時とそうでない時のスタンス

## ２つの帽子

「機能追加」と「リファクタリング」でやることを区別する考え方

- 機能追加の帽子 ... ただ新しい機能を追加する。既存のコードを書き換えない。テストを追加し、それが通ることを確認する。
- リファクタリングの帽子 ... 機能追加しない。コードの改造をする。テスト追加しない。テスト変更する場合は I/F の変更などで必要な時のみ。

# いつするべきか

- 3 度目の原則
  - 同じ処理や値を３回使った場合にそれをまとめる
- コードの理解が必要な時
  - 読みながらコードをわかりやすくすればより多くを理解できる
  - ex
    - 機能追加 <= 最も行われる
    - バグフィックス
    - コードレビュー
- その他

# いつしないべきか

- 0 から書き直しが必要な時
  - ex
    - コードが動かない時
- 納期が迫っている時
  - 得られる生産性の高まるを示せない or 実際にそこまで効果はない可能性もあり、納期後にやるのが望ましい
- アカデミックな目的でのリファクタリング
  - 変更性等が高まるわけでもないのに賛成できないコードだからという理由だけでコードを変える行為は意味を成さない

# コードの臭い

## コードの重複

(対処)
同じロジックはできるだけ１つにまとめる

## 行数の長いメソッド

(対処)
出来るだけ小さく１つの処理を行うメソッドにして、それらを上位で使うなどする。

## 大きなクラス

１つのクラスがしようとしていることが多すぎる状態
しばしば、インスタンス変数が多いことがある

(問題)
コードの重複や依存が多くなり、変更性が下がる

(対処)
責務に応じてクラスの抽出などを行う

## 長い引数リスト

(問題)
引数が多いと必要な値が増えた時に都度 I/F の変更等が必要になり、修正が多岐に及ぶ

(対処)
オブジェクトを渡すなどして、引数を減らす

## 変更系統の分岐

ある１つの変更によってクラス内で複数の方向に変更が必要な状態

(問題)
ある１つの変更によってクラス内で複数の方向に変更が必要になり、変更性が下がる

(対処)
ある１つの変更に対して１つの方向のみ変更が必要なようにクラスの抽出などを行う

##　ショットガン創の手術

１つの種類の変更の際に複数のクラスに変更が必要な状態
「変更系統の分岐」の逆向き

(問題)
1 変更 - 1 クラスの１方向とならない

(対処)
変更が１つのクラスに閉じるようにクラスをまとめる

## メソッドの浮気

あるメソッドが異なるクラスの値などを参照しがちな状態

(対象)
そのクラスにメソッドを移動する

## 群れたがるデータ

複数箇所で同じような構成のデータが参照等されている状態

(対処)
それらを１つのオブジェクトとして扱う

## プリミティブ強迫症

意味のある１つのオブジェクトにできるプリミティブ型の値の集合をそのままで持っている状態

(対処)
オブジェクトとしてまとめて扱う

## case 文

ポリモーフィズムを用いる

## パラレルな継承改装

あるクラスのサブクラスを作ると別のクラスのサブクラスも作る必要が出る状態
