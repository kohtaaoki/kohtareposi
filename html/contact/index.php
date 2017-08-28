<!DOCTYPE html>
<html lang="ja">
<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# website: http://ogp.me/ns/website#">
<!--[if IE]>
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta http-equiv="imagetoolbar" content="no">
<![endif]-->
<meta charset="utf-8">
<title>CONTACT ｜ seventh avenue</title>
<meta name="description" content="LINK ｜ seventh avenue">
<meta name="keywords" content="LINK,seventh avenue">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1" />
<meta name="format-detection" content="telephone=no" />
<meta http-equiv="X-UA-Compatible" content="IE=edge">

<!-- OpenGraph -->
<meta property="og:type" content="website">
<meta property="og:title" content="seventh avenue">
<meta property="og:description" content="松嶋菜々子,藤沢恵麻,井上真央,伊藤歩,白川由美が所属する事務所の公式ホームページ">
<meta property="og:url" content="http://www.7th-avenue.co.jp/">
<meta property="og:image" content="http://www.7th-avenue.co.jp/img/fb.jpg">
<meta property="og:site_name" content="seventh avenue">

<!-- favicon -->
<link rel="shortcut icon" sizes="16x16" href="/img/favicon.ico">
<!-- CSS -->
<link rel="stylesheet" href="../css/import.css" type="text/css">
<link rel="stylesheet" href="../css/contact.css" type="text/css">

<!--[if lt IE 9]><script src="/js/html5shiv.js"></script><![endif]-->

<!-- Google Analytics-->
<!--#include virtual="/ssi/ga.html"-->
</head>
<body id="link">

<div id="container">

<!--#include virtual="/ssi/header.html"-->

<!-- CONTENTS -->
<div id="contents">

<!-- ARTICLE -->
<article>
<section>
<h2>LINK</h2>

<div class="inner">
<div class="headtext">弊社所属タレントのTV、映画、広告出演などのお問い合わせにつきましては、<br>
下記フォームに必要事項を入力のうえ、送信ください。<br>
お問い合わせ内容によっては、お時間をいただくこともございますので、<br>
あらかじめご了承くださいませ。<br>
<br>
なお、タレントのプライベートに関するお問い合わせや<br>
HPに掲載していない情報につきましては、お答え出来ません。<br>
<br>
</div>

<form action="./clipmail.php" method="post" enctype="multipart/form-data">
<input type="hidden" name="need" value="お名前 連絡先 携帯番号 email タレント名 内容" />
<fieldset>

<table>
<tr>
  <th><label>*御社名・団体名</label></th>
  <td><input type="text" name="_会社名" value=""></td>
</tr>
<tr>
<th><label for="name1">*お名前</label></th>
<td><input type="text" name="お名前" value=""></td>
</tr>
<tr>
  <th><label>*メールアドレス</label></th>
  <td><input type="text" name="email" value=""></td>
</tr>

<tr>
  <th><label>*ご連絡先</label></th>
  <td><input type="text" name="_連絡先" value=""></td>
</tr>
<tr>
<th><label for="phone">*携帯番号</label></th>
<td><input type="text" name="_携帯番号" value=""></td>
</tr>

<tr>
  <th><label>*お問い合わせの<br>
所属タレント名</label></th>
  <td><input type="text" name="_タレント名" value=""></td>
</tr>

<tr>
  <th><label for="pr">*お問い合わせ内容</label></th>
  <td><textarea type="text" name="_内容"></textarea></td>
</tr>
</table>
</fieldset>

<div class="btnArea"><input name="" type="submit" value="確認" class="btn"></div>

</form>

</div>
  
</div>

</section>
</article>
<!-- //ARTICLE -->

</div>
<!-- //CONTENTS -->
</div>
<!-- //CONTAINER -->

<!--#include virtual="/ssi/footer.html"-->

</body>
</html>
