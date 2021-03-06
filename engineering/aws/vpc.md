#### VPC(Virtual Private Cloud)

- ユーザー専用(EC2 インスタンス同士を接続する仮想ネットワーク環境)のプリベートなクラウド環境を提供するサービス

- クラウド内で論理的に分離したセクションをプロビジョニングし、ユーザーが定義する仮想ネットワークで AWS リソースを起動できる
  - プロビジョニング ... ネットワーク設備やシステムリソースなどを事前に用意しておき、ユーザーの要求に応じてそれを割り当てて迅速にサービスの提供を行うこと

### サブネット

- 分離したリソースグループを格納する場所を指定する VPC の IP アドレス範囲
- アベイラビリティゾーン毎に設定
- サブネット内の最初の４つと最後の１つの IP 以外を EC2 インスタンス  用に使用可能

### ルートテーブル

- サブネットと VPC 内での通信（ネットワークトラフィック）を関連付ける道標のようなもの

### インターネットゲートウェイ(IGW)

- VPC とパブリックインターネットを接続するためのゲートウェイ

### NAT ゲートウェイ

- 高い可用性を持つマネージド型のネットワークアドレス変換 (NAT) サービスで、プライベートサブネットにあるリソースからインターネットへの接続に利用する
- インターネットから接続される必要がないインスタンスについて、インターネットからの  接続を遮断しつつ自身はインターネットに接続できるようにする  
  => 外部からの接続の危険性を減らし、ライブラリの取得などで必要になる外部への接続を可能にする

### ネットワーク ACL

- サブネットへのネットワークアクセスを制御する。

### バーチャルプライベートゲートウェイ(VGW)

- VPN 接続の Amazon VPC 側
- １つの VPC に１つの VGW のみアタッチ可能

### Elastic IP

-  アカウントに紐付けされる固定のパブリック IP

### ピアリング接続

- ２つの VPC 間のトラフィックをプライベート IP アドレス経由でルーティングできる

### ネットワークインターフェース(ENI)

- VPC 上のネットワークに接続する最小単位
