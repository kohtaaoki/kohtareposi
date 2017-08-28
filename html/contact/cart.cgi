#!/usr/local/bin/perl



#if($ENV{'REMOTE_ADDR'} ne '122.216.245.82'){
#&error('�V�X�e�������e�i���X���̈׌��݂����p���������܂���B<br />�������e�i���X���I�����敜���ƂȂ�܂��B���炩���߂��������������B');
#}



use Time::Local;



# �J�[�g�p�X
$cart_dir = '/home/httpd/session';

# �A�C�e���t�@�C��
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
	# �Z�b�V����ID�擾
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
		&error('���i��I�����ĉ������B');
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
			&error('���ʂ͐����œ��͂��ĉ������B');
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

		# ���ʃ`�F�b�N
		if($num){$stock = $num - $buynum;}
		if($stock < 0){
			$error .= '<br>�w�������݌ɐ��𒴂��Ă��܂��B';
		}elsif($num <= 0){
			$error .= '<br>���̏��i�͊������܂����B';
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

		if($id eq 'NG-019'){$error = '<br>���̏��i�͔����O�̏��i�ł��B';}	# 151125�ǉ�

		if($error){$error = "<font color=\"#FF0000\">$error</font>"}

		$items.=<<EOF;
<tr>
<td>$id</td>
<td>$title$error</td>
<td>$price�~</td>
<td><select name="$id">
$select_cart_num
</select></td>
<td>$subtotal�~</td>
<td><a href="cart.cgi?DEL=$id">�폜</a></td>
</tr>
EOF

	}
}


if($itemflag1 && $itemflag2){&error('�\�񏤕i�Ƃ��̑��̏��i�͓����ɍw������Ƃ��ł��܂���B');}


# �Z�b�V�����ɏ�������
open(DB,">$cart_dir/$FORM{'cartid'}.txt");
print DB $newcook;
close(DB);
chmod(0777, "$cart_dir/$FORM{'cartid'}.txt");



if(!$items){&error('�V���b�s���O�J�[�g�ɂ͏��i�������Ă��܂���B');}



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
<li class="howto"><a href="http://officialstore.jp/negicco/pc/howto.html">�w�����@</a></li>
<li class="payment"><a href="http://officialstore.jp/negicco/pc/payment.html">���x�����@�E����</a></li>
<li class="tokutei"><a href="http://officialstore.jp/negicco/pc/tokutei.html">���菤����@�Ɋւ���L��</a></li>
<li class="inquiry"><a href="https://ssl.officialstore.jp/store/form/?site=CV" target="_blank">���₢���킹</a></li>
</ul>
</div>
</div>
<!-- //HEADER -->

<!-- CONTENT -->
<div id="content">
<div id="contentInner">
<h2>����������</h2>
<p class="caption">�������̂����ɂ́A�ȉ��̏��i���I������Ă��܂��B<br />
����ύX�������ꍇ�́A���ʗ��ɍw�����ʂ�I�����ĉ��́u���ʍČv�Z�{�^���v�������ĉ������B<br />
�폜����ꍇ�͉E�[�̍폜�{�^���������Ă��������B</p>

<!-- CART -->
<form action="cart.cgi" method="POST">
<input type="hidden" name="change" value="1">
<table class="shoppingcart" title="����������">
<tr>
<th>���i�R�[�h</th>
<th>���i��</th>
<th>���i�i�ō��j</th>
<th>����</th>
<th>���v</th>
<th>�폜</th>
</tr>
$items
<tr class="recalculation">
<td colspan="6"><div  align="right"><input type="submit" value="���ʍČv�Z" /></div>
</td>
</tr>
</table>
</form>
<div class="submit">
<input type="button" value="�������𑱂���" onClick="location.href='http://officialstore.jp/negicco/'">&nbsp;&nbsp;
<form action="https://ssl.officialstore.jp/cgi-bin/negicco/pc/form.cgi" method="post">
<input type="hidden" name="cartid" value="$FORM{'cartid'}">
<input name="submit" type="submit" value="������ʂ֐i��" />
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
<li class="howto"><a href="http://officialstore.jp/negicco/pc/howto.html">�w�����@</a></li>
<li class="payment"><a href="http://officialstore.jp/negicco/pc/payment.html">���x�����@�E����</a></li>
<li class="tokutei"><a href="http://officialstore.jp/negicco/pc/tokutei.html">���菤����@�Ɋւ���L��</a></li>
<li class="inquiry"><a href="https://ssl.officialstore.jp/store/form/?site=CV" target="_blank">���₢���킹</a></li>
</ul>
</div>
</div>
<!-- //HEADER -->

<!-- CONTENT -->
<div id="content">
<div id="contentInner">
<h2>�G���[</h2>
<p class="caption">$error
<br>
<a href="http://officialstore.jp/negicco/">���i�ꗗ�ɖ߂�</a></p>
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


