# serverless

## What?

- アプリケーションサーバー … 「常駐型プロセス」を実行するインフラストラクチャ
- サーバレスアーキテクチャ … 「非常駐型プロセス」をイベントによってトリガーするインフラストラクチャ

常駐型プロセス => サーバー内に既に置いてあるファイルなど

様々な定義があるが AWS におけるサーバーレスとは、
「Amazon S3、DynamoDB、Lambda を活用することで、インスタンスベースの仮想サーバー（EC2、ElastiChache、Redshift など）を使わずにアプリケーションを開発するアーキテクチャ」

> 一般にシステムの運用には、プログラムを動かすためのサーバーが必要です。そしてそのサーバーは、  
> 常に稼働していなければなりません。サーバーレスは、サーバーを必要としないので、  
> それ自体のコストがかからないのはもちろん、運用や保守のコスト、  
> さらにシステムの開発工数を減らす効果もあり、コストの削減につながりやすいとされています。

[サーバーレスアーキテクチャとは何か？　 AWS の「Lambda」と「EC2」を比較して解説](https://www.sbbit.jp/article/cont1/32603)

## 主なサーバレスアーキテクチャ使用事例

- AWS 「Lambda」
- Google 「Google Cloud Functions」
- IBM 「OpenWhisk」
- Microsoft 「Azure Functions」

## AWS lambda

- クラウド上でアプリケーションを実行する新たなプラットフォーム
- 何らかのイベントをトリガーに事前に用意した処理を実行することが可能

  (ex:イベント)

  - S3 へのアップロード
  - DynamoDB のデータ更新

- インフラの管理をする必要がない(実行環境等は AWS 側が用意してくれる)
  - EC2 インスタンスの設定不要
  - イベントトリガーのため、起動・管理不要
  - 環境設定不要
  - オートスケーリング = イベントの発生レートに応じて自動でスケールをコントロールしてくれる(必要な場合に勝手に EC2 を立てて実行し、削除してくれる)

=> アプリケーションの開発と Lambda ファンクションとしてアップロードするだけいい。

(従来)

- イベントドリブンなアプリケーションの作成には手間がかかった

  (ex)

  - 変更を検知するためにポーリングし続ける仕組みの構築
    - ポーリング … 一定時間ごとに、機器やソフトウェアなどの状況を確認し、何らかの処理を行なう状態になったと判断したらそれを行なう方式。
  - 変更を検知したらそれに応じた適切な処理を行う仕組みを独自に実装

- インフラの構築管理の手間もかかった
  - AWS の場合、EC2 インスタンスの設定や OS や言語などの環境設定、起動、監視、スケール化などなど

### lambda ファンクション

- トリガーに対して実行する関数
- ステートレスに記述する必要がある
  - Lambda ファンクションは内部的にはコンテナとして実行されており、起動の都度生成され（一部例外はあるものの）終了時には破棄されるから
  - => Lambda ファンクション自身ではデータを永続化することができません

(記述方法)

- 実行コードの書き方は主に２種類

  - マネージメントコンソール画面上に用意されている組み込みエディタを使用
  - ローカル PC などで書いたコードを Zip 形式にしてアップロードする
    - ライブラリなども一緒に Zip 形式でアップロードが必要

- 実行のタイムアウト時間を設定する必要がある

  - デフォルトで 3 秒
  - 1~60 まで 1 秒刻み  
    => 比較的シンプルで小規模な処理をイベント発生ごとに実行するイベントドリブンアーキテクチャのためのプラットフォーム  
     既存のバッチジョブを代替するプラットフォームではないということ

- IAM ロールでファンクションの起動と実行に関わる権限を設定する必要がある

- lambda ファンクションとイベントの発生元となる AWS リソースを紐付ける
  - AWS リソース
    - S3
    - DynamoDB
    - Kinesis Stream  
      => この AWS リソースのことを AWS Lambda では「イベントソース」と呼ぶ
  - ※ このとき、Lambda ファンクションとイベントソースのリージョンは一致していなければならない

### イベントリソースによるファンクション起動時の挙動

- PUSH モデル (S3, カスタムイベントのとき)

  - イベント発生時に直接 lambda ファンクションを起動する
  - イベントの実行が順不同になる
  - ３回までのリトライ

  ![Pushモデル](https://codezine.jp/static/images/article/8446/8446_18.gif)

- PULL モデル (DynamoDB, Kinetics) Stream)

  - イベントを直接発行しない
  - Lambda が自らストリームからポーリングしてイベントを所得する
  - 順序もストリームに入ってきた順などで行われる
  - リトライはストリーム内のデータの期限切れまで無限に行われる

  ![Pullモデル（Amazon Kinesisの場合)](https://codezine.jp/static/images/article/8446/8446_19_s.gif)

### IAM ロール

- ２種類のロールを設定する必要がある
  - Invocation Role … 誰がファンクションを実行できるかを決定
  - Execution Role … ファンクションができること（どの AWS のリソースにどういったアクションを行えるか）を決定

* ref
  - [初めての AWS Lambda ～ AWS Lambda で始めるイベントドリブンアプリケーション](https://codezine.jp/article/detail/8446)
  - [Serverless Architectures](https://martinfowler.com/articles/serverless.html)
  - [初めてのサーバーレスアプリケーション開発 ～ Serverless Framework を使って AWS リソースをデプロイする～](https://dev.classmethod.jp/cloud/aws/serverless-first-serverlessframework/)
  - [Serverless とは何なのかと言われて答えられなかったため調べた。](https://qiita.com/m_ando_japan/items/e698f4949b5068b119f7)
