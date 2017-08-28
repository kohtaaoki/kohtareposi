<?php require_once ("../../../lib/init_edit.php"); //設定ファイル 全ページに入れる ?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html lang="ja">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<script language="JavaScript">
<!--
function MM_jumpMenu(targ,selObj,restore){ //v3.0
  eval(targ+".location='"+selObj.options[selObj.selectedIndex].value+"'");
  if (restore) selObj.selectedIndex=0;
}
//-->
</script>
<style type="text/css">
<!--
body {
	background:url(img/bg.gif) #FFFFFF repeat-x;
}
-->
</style>
</head>
<body topmargin="0" leftmargin="0" marginwidth="0" marginheight="0" bgcolor="#EEEEEE">
<table width="100%" cellpadding="0" cellspacing="0" border="0">
<tr>
<td>
  <a href="/cgi-bin/edit/mk_index.cgi">
    <!-- <img src="img/title.jpg" border="0">-->
	更新
  </a>
</td>
<td align="right"><table cellpadding="2" cellspacing="2" border="0">
<tr>
<td><select name="menu1" onChange="MM_jumpMenu('parent.frames[\'main\']',this,0)">
<option value="blank.html">更新箇所を選択してください</option>


<option value="/cgi-bin/edit/bnr/index.cgi">├バナー</option>
<option value="/cgi-bin/edit/bnr_sns/index.cgi">├SNS バナー</option>
<option value="/cgi-bin/edit/bnr_link/index.cgi">├LINKバナー</option>
<option value="/cgi-bin/edit/news/index.cgi">├NEWS</option>
<option value="/cgi-bin/edit/blog/index.cgi">├BLOG-</option>
<option value="/cgi-bin/edit/biography/index.cgi">├BIOGRAPHY</option>
<option value="/cgi-bin/edit/profile/index.cgi">├PROFILE</option>
<!--
<option value="/cgi-bin/edit/counter.cgi">├カウンター</option>
-->
<option value="/cgi-bin/edit/wysiwyg/index.cgi">└下書き</option>
</select></td>
</tr>
</table></td>
</tr>
</table>
</body>
</html>
