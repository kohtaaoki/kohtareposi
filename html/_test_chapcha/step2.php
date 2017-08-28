<html>
<meta charset="utf-8">
<title></title>
<head>
</head>
<body>
<!--
g-recaptcha-response:<?php echo $_POST["g-recaptcha-response"]; ?><br>
name:<?php echo $_POST["name"]; ?><br>

<br>
<br>
<br>
-->

<?php

$secretkey = '6Lcv1Q4UAAAAAD5-MdrhcA0nIIg0Z6PTwmsNsA0O';

if($_POST["g-recaptcha-response"]){
	$url = 'https://www.google.com/recaptcha/api/siteverify?secret='.$secretkey.'&response='.$_POST["g-recaptcha-response"];

	$ch = curl_init();	// 1. 初期化
	curl_setopt( $ch, CURLOPT_URL, $url );	// 2. オプションを設定
	curl_setopt( $ch, CURLOPT_RETURNTRANSFER, true );
	$param = curl_exec( $ch );	// 3. 実行してデータを得る
	curl_close( $ch );	// 4. 終了

	// true or false
	echo $param;
}
?>
</body>
</html>
