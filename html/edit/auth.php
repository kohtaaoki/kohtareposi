<?php require_once ("../../../lib/init_edit.php"); //設定ファイル 全ページに入れる ?>
<?php
if($allow_ip){
	if(preg_match("/$_SERVER[REMOTE_ADDR]/", $allow_ip)){
		$contents = "許可IPアドレス：$allow_ip<br />\n";
	}else{
		exit;
	}
}else{
	$contents = "許可IPアドレス：すべて可<br />\n";
}



$url = "http://$domain_name_sp/cgi-bin/auth/enter_m-up.cgi";
$url_encode = urlencode($url);


?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title></title>
<link rel="stylesheet" type="text/css" href="/edit/css/style.css">
</head>
<body>

<?php echo $contents; ?>
<br />
<br />

<?php echo $url; ?><br />
<img src="http://chart.apis.google.com/chart?chs=150x150&cht=qr&chl=<?php echo $url_encode; ?>&choe=UTF-8" alt="QRコード">


</body>
</html>
