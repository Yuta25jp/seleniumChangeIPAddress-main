# seleniumChangeIPAddress

Selenium で IP アドレスを切り替える方法

## 最も一般的な方法(Tor の利用)

Tor とは <br>
https://ja.wikipedia.org/wiki/Tor

### Mac

- step 0(準備)<br>
  Terminal で以下のコマンドを走らせる<br>
  `brew install tor`

- step 1<br>
  ローカルに仮想環境を作る<br>
  mamba, conda, pyenv, venv 等

- step 2<br>
  そこにこのリポジトリをコピーする<br>

- step2<br>
  必要ライブラリのインストール<br>
  `pip install -r requirements.txt`

- step3<br>
  settings.py を開き、BASE_PATH="" に path を記述する<br>

- step4<br>
  テストコードを実行<br>
  `python testTor.py`

[注意事項]<br>
プロキシサーバに torserver 等の認識される値、及び国外のサーバとなりやすいため、セキュリティの高いサイトだと、ブロックされる可能性あり。<br>
また、Tor は PC 側でのネットワーク設定となるため、切り替え(reload)のタイミングで一旦ネットワークが切れるので、マルチスレッドなどで動かす場合、ネットワークが途中で切れるスレッドが発生し、エラーハンドリングが難しくなる。<br>

## 一般的なプロキシを通す

上記の Tor が使えない場合、一般的なプロキシサーバを使うしかありません。<br>
プロキシの説明:<br>
https://jp.itopvpn.com/blog/osusume-proxy-severs-1420

無料プロキシサーバ<br>
http://free-proxy.cz/ja/proxylist/country/JP/all/ping/all

## 基本的な実装手順

プロキシを刺すのは一緒ですが、<br>
無料プロキシサーバのリストが必要になるので、<br>
まず、上記のような無料プロキシのリストがあるサイトのスクレイピング<br>
その後、それを for 文などで回し、引数で渡し selenium(chromedriver)を起動する<br>

こちらは chrome でプロキシを設定しているので、マルチスレッド対応可。<br>
とはいえ、プロキシが生きていない場合もあるので、タイムアウト等で生きていないプロキシの場合のエラーハンドリングが必要<br>

`python test.py`
