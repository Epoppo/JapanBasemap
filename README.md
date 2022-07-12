# Qgis3用 国土基本図図郭, 地域メッシュ生成プラグイン
寝て起きたらまたお仕事めう<br>
基本図のなんやかんやについていちいち調べて生成し直したり、必要以上に大きく読み込んでから切り取ったりするのが面倒なのでQgisのプラグインとして開発<br>
指定したベクタレイヤに交差する国土基本図図郭の図郭ポリゴン、もしくは地域メッシュを生成するプラグイン<br>
<br>


## 使用方法
処理範囲となるベクタを用意して下記の操作を行う。<br><br>
国土基本図図郭と地域メッシュの必要となる方の機能を起動
<br>
    -- 基本図図郭が必要な場合 -- <br>
    1. 「国土基本図図郭生成」をダブルクリック
    <br>
    <img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/v2_0_0/01_01_01_target_area.png" width=1200>
    <br>
    <br>
    2. 日本における平面直角座標系01系\~19系のいずれかの座標系、及び必要となる地図情報レベルを選択し、生成範囲となるベクタを設定して「実行」を押下
    <br>
    <img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/v2_0_0/01_02_01_plugin_window_basemap.png" width=1200>
    <br>
    <br>
    3. 設定したベクタに交差する図郭が出力されるので、スタイルを弄って完成<br>
    以下サンプル<br>
    地図情報レベル1000の生成
    <br>
    <img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/v2_0_0/01_03_01_basemapsample_base1000.png" width=1200>
    <br>
    地図情報レベル5000,1000,500の生成テスト
    <br>
    <img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/v2_0_0/01_03_02_basemapsample.png" width=1200>
    <br>
    <br><br>
    -- 地域メッシュが必要な場合 --<br>
    1. 「地域メッシュ生成」をダブルクリック<br>
    (国土基本図図郭の際とは投影系が異なるため、引き伸ばされたように見えますが同じベクタを用いております。)
    <br>
    <img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/v2_0_0/02_01_01_target_area.png" width=1200>
    <br>
    <br>
    2. 世界測地系と日本測地系で必要な座標系、及び必要なメッシュ種別を選択し、生成範囲となるベクタを設定して「実行」を押下
    <br>
    <img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/v2_0_0/02_02_01__plugin_window_regional.png" width=1200>
    <br>
    <br>
    3. 設定したベクタに交差するメッシュが出力されるので、スタイルを弄って完成<br>
    以下サンプル<br>
    3次メッシュの生成
    <br>
    <img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/v2_0_0/02_03_01_meshsample_3rdmesh.png" width=1200>
    <br>
    2次~6次メッシュの生成テスト
    <br>
    <img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/v2_0_0/02_03_02_meshsample_2nd_6thmesh.png" width=1200>
    <br>
    100mメッシュの生成テスト
    <br>
    <img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/v2_0_0/02_03_03_100m_mesh.png" width=1200>
    <br>
    <br><br>

## 作成可能な種類
図郭名はフィールドに持たせてあります。
+ 国土基本図図郭
    + 地図情報レベル 50000
    + 地図情報レベル 5000
    + 地図情報レベル 2500
    + 地図情報レベル 1000
    + 地図情報レベル 500
    + 地図情報レベル 250
+ 地域メッシュ
    + 1次メッシュ(80kmメッシュ)
    + 2次メッシュ(10kmメッシュ)
    + 5倍地域メッシュ(5kmメッシュ)
    + 2倍地域メッシュ(2kmメッシュ)
    + 3次メッシュ(1kmメッシュ)
    + 4次メッシュ(500mメッシュ)
    + 5次メッシュ(250mメッシュ)
    + 6次メッシュ(125mメッシュ)
    + 3次メッシュ1/10細分区画(100mメッシュ)

<br>

## 当プラグインが対応するQgisのバージョン
Qgis 3.10と3.16と3.24で動作確認 <br>
Qgis3.0以降が搭載する「Python 3.6」で動作可能であるように書いたつもりではあるが、手元に環境が無いので詳細不明。何か問題あれば教えていただけると幸いです。
<br>
<br>

## インストール方法
-- 分かってる人向け --<br>
通常通りインストールを行っている場合、QGIS3がプラグインを読み込むディレクトリにフォルダを作成し、<br>
```
C:\Users\\(ユーザ名)\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\japan_basemap
```
に対して当リポジトリの内容を突っ込めば動きます。

<br>
-- zipを利用したインストール --<br>

1. 当リポジトリのReleaseで配布してるzip(もしくは下記)をDLしてローカルに保存
    - v2.0.1<br>
    <a href="https://github.com/Epoppo/JapanBasemap/releases/tag/v2_0_1" class="autolink" rel="nofollow noopener" target="_blank">https://github.com/Epoppo/JapanBasemap/releases/tag/v2_0_1</a>
2. Qgisを開く
3. メニューバーの「プラグイン(P)」から「プラグインの管理とインストール」を押下
4. ポップしたウィンドウ左にある「ZIPからインストールする」を押下
5. 1.で保存したzipを指定
6. ウィンドウの「インストール済み」を押下し、「Japan Basemap」が導入され、チェックが入っていることを確認
7. プロセシングツールボックスに「JapanBasemap」の行と、その配下に「国土基本図図郭生成」及び「地域メッシュ生成」のプロセスツールが追加されていることを確認

<br>
<br>


# 補足資料
## 国土基本図図郭について
### 地図情報レベル毎における図郭割り
公共測量標準様式にある数値地形図データファイル仕様の項の内、第84条と85条に従ったもの。

以下内容を適当に要約したもの

| 地図情報レベル | 図郭サイズ(x*y) | 名称(例) | 内容 |
|:---|:---|:---|:---|
|50000 |40km*30km |09JD| 平面直角座標の原点を中心として、南北600kmを20等分,東西320kmを8等分。10の位を南北でA\~T、1の位をを東西でA\~Hで表している。| 
|5000 |4km*3km |09JD55 | 地図情報レベル50000を10\*10に分割。10の位を南北で0\~9、1の位をを東西で0\~9で表している。|
|2500 |2km*1.5km |09JD554| 地図情報レベル5000を2\*2に分割。北西を1,北東を2,南西を3,南東を4とする|
|1000 |800m*600m |09JD553D| 地図情報レベル5000を5\*5に分割。10の位を南北で0\~4、1の位を東西でA\~Eで表している。|
|500 |400m*300m |09JD5576| 地図情報レベル5000を10\*10に分割。10の位を南北で0\~9、1の位を東西で0\~9で表している。|
|250 |200m*150m |09JD55FT| 地図情報レベル5000を20\*20に分割。10の位を南北でA\~T、1の位を東西でA\~Tで表している。|


他、2500を更に4等分した地図情報レベル1250と呼称される図郭割りを一度だけ見たことがあるが、<br>
名称の付け方など公的に記載された資料が見つからなかったので今回は見送り。<br>
<br>
<br>

### 測地系について
平面直角座標系については流石に割愛<br>
ココでは当プログラム中で系の判断に用いているEPSGコードについてのみ記載<br>
下記に挙げるEPSGのいずれかで当プラグインは動作し、それ以外を指定した場合は処理を行わないようになっています。 <br>
<br>
詳細な割り当てについては地理院HPを参照<br>

<br>
以下は系とEPSG、それに対応するざっくりとしたエリアの記載


|系  | JGD2011 | JGD2000 | TokyoDatum | 都道府県|
|:---|:---|:---|:---|:---|
|01 | 6669 | 2443 | 30161 | 長崎県、鹿児島県の一部
|02 | 6670 | 2444 | 30162 | 福岡県、佐賀県、熊本県、大分県、宮崎県、鹿児島県の一部
|03 | 6671 | 2445 | 30163 | 山口県、島根県、広島県
|04 | 6672 | 2446 | 30164 | 香川県、愛媛県、徳島県、高知県
|05 | 6673 | 2447 | 30165 | 兵庫県、鳥取県、岡山県
|06 | 6674 | 2448 | 30166 | 京都府、大阪府、福井県、滋賀県、三重県、奈良県、和歌山県
|07 | 6675 | 2449 | 30167 | 石川県、富山県、岐阜県、愛知県
|08 | 6676 | 2450 | 30168 | 新潟県、長野県、山梨県、静岡県
|09 | 6677 | 2451 | 30169 | 東京都の一部、福島県、栃木県、茨城県、埼玉県、千葉県、群馬県、神奈川県
|10 | 6678 | 2452 | 30170 | 青森県、秋田県、山形県、岩手県、宮城県
|11 | 6679 | 2453 | 30171 | 北海道の一部
|12 | 6680 | 2454 | 30172 | 北海道の一部
|13 | 6681 | 2455 | 30173 | 北海道の一部
|14 | 6682 | 2456 | 30174 | 東京都の一部
|15 | 6683 | 2457 | 30175 | 東京都の一部
|16 | 6684 | 2458 | 30176 | 沖縄県の一部
|17 | 6685 | 2459 | 30177 | 沖縄県の一部
|18 | 6686 | 2460 | 30178 | 東京都の一部
|19 | 6687 | 2461 | 30179 | 東京都の一部

<br>
<br>
<br>

## 地域メッシュについて
基本的にJIS規格(JIS X 0410)で定められている内容通り。<br>
JIS規格で定められていないものについては、個人の認識ですが3次メッシュ1/10細分区画(100mメッシュ)はよく利用されているので作成できるようにし、1/20細分区画(50mメッシュ)などの更に細分されたメッシュ種別や、逆に世界メッシュコードなどの拡張概念は現状あまり利用されていない認識なので実装見送り。
<br>
他不明点は参考資料をご参照願います。

### メッシュコード
名づけは一般的に普及しているJIS規格と統計局の資料に沿ってに作成<br>
緯度経度の間隔は度分秒で記載しておりますが、処理の際は全部秒に単位を合わせて計算やってます。1度は3600秒で1分は60秒。<br>
以下サンプル<br>

生成可能なメッシュ種別

|No. |標準地域メッシュ内の種別|JIS規格上の名称|よく使用される名称|
|:---|:---|:---|:---|
|0|-|第1次地域区画|1次メッシュ
|1|-|第2次地域区画|2次メッシュ
|2|統合地域メッシュ|5倍地域メッシュ|5倍地域メッシュ
|3|統合地域メッシュ|2倍地域メッシュ|2倍地域メッシュ
|4|基準地域メッシュ|第3次地域区画|3次メッシュ
|5|分割地域メッシュ|2分の1地域メッシュ|4次メッシュ
|6|分割地域メッシュ|4分の1地域メッシュ|5次メッシュ
|7|分割地域メッシュ|8分の1地域メッシュ|6次メッシュ
|8|-|-|3次メッシュ1/10細分区画<br>(100mメッシュ)

<br>

各種別と詳細

|No.|よく使用される名称|緯度の間隔|経度の間隔|一辺の長さ|名称桁数|名称<br>(例)|
|:---|:---|:---|:---|:---|:---|:---|
|0|1次メッシュ|40 [分]|1 [度]|約 80 [km]|4桁|5339
|1|2次メッシュ |5 [分]|7.5 [分]|約 10 [km]|6桁|533903
|2|5倍地域メッシュ|2.5 [分]|3.75[分]|約 5 [km]|7桁|5339034
|3|2倍地域メッシュ|1 [分]|1.5 [分]|約 2 [km]|9桁|533903665
|4|3次メッシュ|30 [秒]|45 [秒]|約 1 [km]|8桁|53390387
|5|4次メッシュ|15 [秒]|22.5 [秒]|約 500 [m]|9桁|533903874
|6|5次メッシュ|7.5 [秒]|11.25 [秒]|約 250 [m]|10桁|5339038742
|7|6次メッシュ|3.75 [秒]|5.625 [秒]|約 125 [m]|11桁|53390387423
|8|100mメッシュ|3 [秒]|4.5 [秒]|約 100 [m]|10桁|5339038757

<br>

各種別と名称の作成方法

|No.|よく使用される名称|名称桁数|名称<br>(例)| 名称の作成方法 |
|:---|:---|:---|:---|:---|
|0|1次メッシュ|4桁|5339|緯度*1.5を上2桁、経度%100を下2桁とする。
|1|2次メッシュ|6桁|533903|1次メッシュを縦横8等分し、各区画に南と西から順に0~7の番号を振って縦の番号を5桁目、横の番号を6桁目とする。
|2|5倍地域メッシュ|7桁|5339034|2次メッシュを4等分し、南西を1、南東を2、北西を3、北東を4とする数値を7桁目とする。
|3|2倍地域メッシュ|9桁|533903665|2次メッシュを縦横5等分し、各区画に南と西から順に0,2,4,6,8の番号を振って縦の番号を7桁目、横の番号を8桁目とし、5を9桁目とする。
|4|3次メッシュ|8桁|53390387|2次メッシュを縦横10等分し、各区画に南と西から順に0~9の番号を振って縦の番号を7桁目、横の番号を8桁目とする。
|5|4次メッシュ|9桁|533903874|3次メッシュを4等分し、南西を1、南東を2、北西を3、北東を4とする数値を9桁目とする。
|6|5次メッシュ|10桁|5339038742|4次メッシュを4等分し、南西を1、南東を2、北西を3、北東を4とする数値を10桁目とする。
|7|6次メッシュ|11桁|53390387423|5次メッシュを4等分し、南西を1、南東を2、北西を3、北東を4とする数値を11桁目とする。
|8|100mメッシュ|10桁|5339038757|3次メッシュを10等分し、各区画に南と西から順に0~9の番号を振って縦の番号を9桁目、横の番号を10桁目とする。

<br>

+ 統合地域メッシュの内JIS規格で言及されている「10倍地域メッシュ」は2次メッシュと同じものであるため割愛
+ JIS規格上で言及されていない「3次メッシュ1/10細分区画」(100mメッシュ)については、一般に普及しているものと同じ命名になるよう作成。<br>
<br>

### 測地系について
世界測地系と日本測地系の違い等は割愛<br>
国土基本図図郭が平面直角座標を用いるのに対し、地域メッシュでは地理座標系(緯度経度)を用いている。<br>

|  | JGD2011 | JGD2000 | TokyDatum | 対象|
|:---|:---|:---|:---|:---|
|EPSG | 6668 | 4612 | 4301 | 日本全域

<br>

## 全体
### 参考資料
公共測量標準様式(令和2年度版)<br>
<a href="https://psgsv2.gsi.go.jp/koukyou/jyunsoku/pdf/r2/r2_junsoku_furoku7_0609.pdf" class="autolink" rel="nofollow noopener" target="_blank">https://psgsv2.gsi.go.jp/koukyou/jyunsoku/pdf/r2/r2_junsoku_furoku7_0609.pdf</a>
<br>

平面直角座標系（平成十四年国土交通省告示第九号） | 国土地理院<br>
<a href="https://www.gsi.go.jp/LAW/heimencho.html" class="autolink" rel="nofollow noopener" target="_blank">https://www.gsi.go.jp/LAW/heimencho.html</a>
<br>

総務省 統計局ホームページ/地域メッシュ統計の概要<br>
<a href="https://www.stat.go.jp/data/mesh/gaiyou.html" class="autolink" rel="nofollow noopener" target="_blank">https://www.stat.go.jp/data/mesh/gaiyou.html</a>
<br>

総務省 統計局ホームページ/地域メッシュ統計の概要/地域メッシュ統計の特質・沿革.pdf<br>
<a href="https://www.stat.go.jp/data/mesh/pdf/gaiyo1.pdf" class="autolink" rel="nofollow noopener" target="_blank">https://www.stat.go.jp/data/mesh/pdf/gaiyo1.pdf</a>
<br>

JISC 日本産業標準調査会<br>
<a href="https://www.jisc.go.jp/index.html" class="autolink" rel="nofollow noopener" target="_blank">https://www.jisc.go.jp/index.html</a>
<br>

epsg.io<br>
<a href="https://epsg.io/" class="autolink" rel="nofollow noopener" target="_blank">https://epsg.io/</a>
<br>
<br>
<br>

## 他
個人的に必要だから作っただけなので、間違い等多くあるかもしれません。<br>
もし見つけた場合は教えて頂けると幸いです。<br>
