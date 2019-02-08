# API Gateway

- 開発者があらゆる規模で API の公開、保守、モニタリング、セキュリティ保護を簡単に行えるフルマネージドサービス
- アプリケーションの正面玄関となる API を作成可能

(対応)

- EC2 で稼働中のアプリケーション
- ECS で稼働中のアプリケーション
- Elastic Beanstalk で稼働中のアプリケーション
- Lambda で稼働中のコード
- 任意のウェブアプリケーション

(できること)

- 計測 ... API へのトラフィックを自動で計測可能
- セキュリティ ... IAM や Cognito などの AWS 管理ツールやセキュリティツールを利用して、API へのアクセス認証ができる
- 回復性 ... スロットリングによってトラフィックを管理できるので、バックエンド動作はトラフィックの激増に耐えられる。API コールに対する出力をキャッシュし、バックエンドシステムへの不要な呼び出しを避けることによって、レスポンスを  早く返せる
  - スロットリング ... 一定時間内に送信できるリクエスト数を制限すること
- リアルタイム双方向通信 ... チャットアプリ、ストリーミングダッシュボード、通知といったリアルタイム双方向通信アプリケーションを構築する。 => WebSocket API

(対応タイプ)

- HTTP/REST API
- WebSocket API

(料金)

- https://aws.amazon.com/jp/api-gateway/pricing/