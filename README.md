# Qgis3 国土基本図図郭生成プラグイン
寝て起きたらまたお仕事めう<br>
国土基本図図郭についていちいち調べて生成し直したり、必要以上に大きく読み込んでから切り取ったりするのが面倒なので、Qgisのプラグインとして開発<br>
指定したベクタレイヤの範囲に交差する地図情報レベル50000,5000,2500,1000,500,250の図郭コードを載せた国土基本図図郭の図郭ポリゴンの生成するだけのプラグイン<br>
<br>


## 使用方法
基本図図郭が欲しい範囲のベクタが用意してある事を前提としてます。<br>
1. この辺が欲しい<br>
<img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/01_sample_area.png" width=600)>
<br><br>

2. 当プラグインである「国土基本図図郭生成」を起動<br>
<img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/02_select_plugin.png" width=600)>
<br><br>

3. 必要となる平面直角座標系(JGD2011, JGD2000, Tokyoで1~19系のいずれか)の投影法、必要な地図情報レベルを指定し、出力範囲となるベクタ(1.)を指定<br>
<img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/03_plugin_window.png" width=600)>
<br><br>

4. 指定した出力範囲のベクタを包括する国土基本図図郭が生成されます<br>
<img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/04_sample_export_1000.png" width=600)>
<br><br>

5. スタイル、ラベル、投影系を弄ったり、必要であれば異なる地図情報レベルで出したりしてイイ感じにする<br>
<img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/05_sample_1000.png" width=600)>
<img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/06_sample_2500.png" width=600)>
<img src="https://raw.githubusercontent.com/Epoppo/JapanBasemap/images/images/07_sample_5000.png" width=600)>
<br><br>
<br>

## 当プラグインが対応するQgisのバージョン
Qgis 3.10と3.16で動作確認 <br>
Qgis3以降が搭載するPython 3.6以降のバージョンなら大丈夫であるように書いたつもりではあるが、手元に環境が無いので不明
<br>
<br>

## インストール方法
-- 分かってる人向け --<br>
通常通りインストールを行っている場合、QGISがプラグインを読み込むディレクトリの<br>
C:\Users\\(ユーザ名)\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\BasemapGen <br>
に対して当リポジトリの内容を突っ込めば動きます。

<br>
-- zipを利用したインストール --<br>

1. 当リポジトリのReleaseで配布してるzipをDLしてローカルに保存
2. Qgisを開く
3. メニューバーの「プラグイン(P)」から「プラグインの管理とインストール」を押下
4. ポップしたウィンドウ左にある「ZIPからインストールする」を押下
5. 1.で保存したzipを指定
6. ウィンドウの「インストール済み」を押下し、「国土基本図図郭生成プラグイン(BasemapGen)」が導入され、チェックが入っていることを確認
7. プロセシングツールボックスに「BasemapGen」の行と、その配下に「国土基本図図郭」のプロセスが追加されていることを確認

<br>
<br>

## 地図情報レベル毎における図郭割り(解説)
公共測量標準様式にある数値地形図データファイル仕様の項の内、第84条と85条に従ったもの。
https://psgsv2.gsi.go.jp/koukyou/jyunsoku/pdf/r2/r2_junsoku_furoku7_0609.pdf

以下内容を適当に要約したもの
| 地図情報レベル | 1図郭のサイズ<br>(x*y) | 名称<br>(例) | 内容 |
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

## 測地系について
平面直角座標系については流石に割愛<br>
ココでは当プログラム中で系の判断に用いているEPSGコードについてのみ記載<br>
下記に挙げるEPSGのいずれかでのみ当プラグインは動作し、それ以外を指定した場合は処理を行わないようになっています。 <br>
<br>
詳細な割り当てについては下記を参照<br>
https://www.gsi.go.jp/LAW/heimencho.html
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

## 今後の実装予定
・空間インデックスの有無<br>
・出力時のデフォルトレイヤ名<br>

## 他
個人的に必要だから作っただけなので、間違い等多くあるかもしれません。
もし見つけた場合は教えて頂けると幸いです。