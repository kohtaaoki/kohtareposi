#!/usr/local/bin/perl



#if($ENV{'REMOTE_ADDR'} ne '122.216.245.82'){
#&error('システムメンテナンス中の為現在ご利用いただけません。<br />※メンテナンスが終了次第復旧となります。あらかじめご了承ください。');
#}



use Time::Local;



# カートパス
$cart_dir = '/home/httpd/session';

# アイテムファイル
$item_file = '/home/httpd/officialstore/cgi-bin/negicco/edit/item.log';


if ($ENV{'REQUEST_METHOD'} eq "POST") { read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'}); }
else { $buffer = $ENV{'QUERY_STRING'}; }

@pairs = split(/&/,$buffer);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$FORM{$name} = $value;
}



$cookie = $ENV{'HTTP_COOKIE'};
@pairs = split(/;/, $cookie);
foreach $pair (@pairs) {
	local($name,$value) = split(/=/, $pair);
	$name =~ s/\s//g;
	$COOKIE{$name} = $value;
}



if(!$COOKIE{'cartid'}){
	# セッションID取得
	@session = (0..9,'a'..'z','A'..'Z');
	$session .= $session[int(rand(@session))] while length($session) < 64;
	$session =~ s/[\/\.\-\$\#\@\!\%\:]//g;
	print "Set-Cookie: cartid=$session; path=/cgi-bin/negicco/pc/\n";
	$COOKIE{'cartid'} = $session;
}


$FORM{'cartid'} = $COOKIE{'cartid'};



open(DB,"$cart_dir/$FORM{'cartid'}.txt");
$cook = <DB>;
close(DB);


if($ENV{'HTTP_USER_AGENT'} !~ 'compatible; MSIE 6'){
	open(DB, "/home/httpd/officialstore/html/negicco/pc/ssi/xml.inc");
	while(<DB>){$xml.=$_;}
	close(DB);
}



@pairs = split(/,/, $cook);
foreach $pair (@pairs) {
	local($name,$value) = split(/:/, $pair);
	$CART{$name} = $value;
}



if($FORM{'item'}){

	if($FORM{'item'} eq 'select'){
		&error('商品を選択して下さい。');
	}

	$FORM{'iid'} = $FORM{'item'};
	$iidlink = "&iid=$FORM{'iid'}";
	$newitem = $FORM{'item'};
	$CART{$newitem} = "1";
	$cook = "$newitem:1,$cook";
}elsif($FORM{'DEL'}){
	$cook = '';
	foreach $cc (keys %CART){
		if($cc ne $FORM{'DEL'}){
			$cook = "$cc:$CART{$cc},$cook";
		}else{
			$CART{$cc} = 0;
		}
	}
}elsif($FORM{'change'}){
	$cook = '';
	foreach $cc (keys %CART){

		if($FORM{$cc} =~ /\D/){
			&error('数量は数字で入力して下さい。');
		}

		$cook = "$cc:$FORM{$cc},$cook";
		$CART{$cc} = $FORM{$cc};
	}
}



open(DB,"$item_file");
@lines = <DB>;
close(DB);

foreach $line (@lines){
	local($id, $title, $intax, $body1, $body2,$num, $date1, $date2, $ip)=split(/	/,$line);
	$id{$id}=$id;
	$title{$id}=$title;
	$intax{$id}=$intax;
	$num{$id}=$num;
}



foreach $iid (keys %CART){
	$id = $id{$iid};
	$title = $title{$iid};
	$intax = $intax{$iid};
	$num = $num{$iid};

	$buynum = $CART{$iid};
	if($buynum > 0){

		$error = '';

		# 数量チェック
		if($num){$stock = $num - $buynum;}
		if($stock < 0){
			$error .= '<br>購入数が在庫数を超えています。';
		}elsif($num <= 0){
			$error .= '<br>この商品は完売しました。';
		}

		$newcook = "$iid:$buynum,$newcook";

		$subtotal = $intax * $buynum;
		$price = $intax;
		$stotal += $subtotal;

		1 while $price =~ s/(\d+)(\d\d\d)/$1,$2/;
		1 while $subtotal =~ s/(\d+)(\d\d\d)/$1,$2/;

		$select_cart_num='';

		$max_num = 10;

		for ($i=0; $i<=$max_num; $i++) {
			if($i eq $buynum){$selected=' selected';}else{$selected='';}
			$select_cart_num .= "<option value=\"$i\"$selected>$i</option>\n";
		}

		if($id eq 'NG-019'){$error = '<br>この商品は発売前の商品です。';}	# 151125追加

		if($error){$error = "<font color=\"#FF0000\">$error</font>"}

		$items.=<<EOF;
<tr>
<td>$id</td>
<td>$title$error</td>
<td>$price円</td>
<td><select name="$id">
$select_cart_num
</select></td>
<td>$subtotal円</td>
<td><a href="cart.cgi?DEL=$id">削除</a></td>
</tr>
EOF

	}
}


if($itemflag1 && $itemflag2){&error('予約商品とその他の商品は同時に購入するとができません。');}


# セッションに書きこみ
open(DB,">$cart_dir/$FORM{'cartid'}.txt");
print DB $newcook;
close(DB);
chmod(0777, "$cart_dir/$FORM{'cartid'}.txt");



if(!$items){&error('ショッピングカートには商品が入っていません。');}



1 while $stotal =~ s/(\d+)(\d\d\d)/$1,$2/;



print "Content-type: text/html\n\n";
print<<EOF;
$xml<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=shift_jis" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<title>Negi Goods Store</title>
<meta name="description" content="Negi Goods Store" />
<meta name="keywords" content="Negi Goods Store" />
<link rel="stylesheet" href="/negicco/pc/css/styleCart.css" type="text/css" media="screen" />
<!--[if IE 6]><script src="/negicco/pc/js/DD_belatedPNG_0.0.8a-min.js"></script><script>DD_belatedPNG.fix('#header,#content,#footer');</script><![endif]-->
</head>
<body>
<div id="wrapper">

<!-- CONTAINER -->
<div id="container">

<!-- HEADER -->
<div id="header">
<a name="top" id="top"></a>
<h1><a href="http://officialstore.jp/negicco/pc/">Negi Goods Store</a></h1>
<div id="globalNav">
<ul>
<li class="howto"><a href="http://officialstore.jp/negicco/pc/howto.html">購入方法</a></li>
<li class="payment"><a href="http://officialstore.jp/negicco/pc/payment.html">お支払方法・送料</a></li>
<li class="tokutei"><a href="http://officialstore.jp/negicco/pc/tokutei.html">特定商取引法に関する記載</a></li>
<li class="inquiry"><a href="https://ssl.officialstore.jp/store/form/?site=CV" target="_blank">お問い合わせ</a></li>
</ul>
</div>
</div>
<!-- //HEADER -->

<!-- CONTENT -->
<div id="content">
<div id="contentInner">
<h2>買い物かご</h2>
<p class="caption">買いものかごには、以下の商品が選択されています。<br />
個数を変更したい場合は、数量欄に購入数量を選択して横の「数量再計算ボタン」を押して下さい。<br />
削除する場合は右端の削除ボタンを押してください。</p>

<!-- CART -->
<form action="cart.cgi" method="POST">
<input type="hidden" name="change" value="1">
<table class="shoppingcart" title="買い物かご">
<tr>
<th>商品コード</th>
<th>商品名</th>
<th>価格（税込）</th>
<th>数量</th>
<th>小計</th>
<th>削除</th>
</tr>
$items
<tr class="recalculation">
<td colspan="6"><div  align="right"><input type="submit" value="数量再計算" /></div>
</td>
</tr>
</table>
</form>
<div class="submit">
<input type="button" value="買い物を続ける" onClick="location.href='http://officialstore.jp/negicco/'">&nbsp;&nbsp;
<form action="https://ssl.officialstore.jp/cgi-bin/negicco/pc/form.cgi" method="post">
<input type="hidden" name="cartid" value="$FORM{'cartid'}">
<input name="submit" type="submit" value="注文画面へ進む" />
</form>
</div>
<!-- //CART -->

</div>
</div>
<!-- CONTENT -->

<!-- FOOTER -->
<div id="footer">
<address>&copy;Dreamusic Inc / &copy;M-UP</address>
</div>
<!-- //FOOTER -->

</div>
<!-- //CONTAINER -->

</div>

</body>
</html>
EOF





sub error{
	$error = $_[0];
	print "Content-type: text/html\n\n";
	print<<EOF;
$xml<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ja" lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=shift_jis" />
<meta http-equiv="Content-Script-Type" content="text/javascript" />
<meta http-equiv="Content-Style-Type" content="text/css" />
<title>Negi Goods Store</title>
<meta name="description" content="Negi Goods Store" />
<meta name="keywords" content="Negi Goods Store" />
<link rel="stylesheet" href="/negicco/pc/css/styleCart.css" type="text/css" media="screen" />
<!--[if IE 6]><script src="/negicco/pc/js/DD_belatedPNG_0.0.8a-min.js"></script><script>DD_belatedPNG.fix('#header,#content,#footer');</script><![endif]-->
</head>
<body>
<div id="wrapper">

<!-- CONTAINER -->
<div id="container">

<!-- HEADER -->
<div id="header">
<a name="top" id="top"></a>
<h1><a href="http://officialstore.jp/negicco/">Negi Goods Store</a></h1>
<div id="globalNav">
<ul>
<li class="howto"><a href="http://officialstore.jp/negicco/pc/howto.html">購入方法</a></li>
<li class="payment"><a href="http://officialstore.jp/negicco/pc/payment.html">お支払方法・送料</a></li>
<li class="tokutei"><a href="http://officialstore.jp/negicco/pc/tokutei.html">特定商取引法に関する記載</a></li>
<li class="inquiry"><a href="https://ssl.officialstore.jp/store/form/?site=CV" target="_blank">お問い合わせ</a></li>
</ul>
</div>
</div>
<!-- //HEADER -->

<!-- CONTENT -->
<div id="content">
<div id="contentInner">
<h2>エラー</h2>
<p class="caption">$error
<br>
<a href="http://officialstore.jp/negicco/">商品一覧に戻る</a></p>
</div>
</div>
<!-- CONTENT -->

<!-- FOOTER -->
<div id="footer">
<address>&copy;Dreamusic Inc / &copy;M-UP</address>
</div>
<!-- //FOOTER -->

</div>
<!-- //CONTAINER -->

</div>

</body>
</html>
EOF
	exit;
}


