<?php
// 日付取得
$date_now = date("YmdHi");


# プロフィール
$log_file = "/home/httpd/7th-avenue.co.jp/pc/cgi-bin/edit/profile/profile.log";
$array = array();
$lines = file($log_file);
foreach($lines as $line){
	list($id, $flag, $name, $alphabet, $image1, $image2, $image3, $year, $month, $day, $from_1, $bloodtype_1, $constellation1, $other_1, $from_2, $bloodtype_2, $constellation2, $other_2, $from_3, $bloodtype_3, $constellation3, $other_3, $date1, $date2, $ip) = explode("	", $line);

	// UP時刻を設定している時
	if($date_now < $hiduke1){continue;}
	// DOWN時刻を設定している時
	if($date_now >= $hiduke2 && $hiduke2){continue;}
	// タレント名
	$talent_name = $talent_name_list[$select];

	// カテゴリ名
	$category = mb_strtolower($category_name[$category]);

	if( ($before_category <> $category and !empty($before_category)) or empty($before_category) ){
		$contents .= <<<EOF
<br>
<h4 class="$category"></h4>
EOF;
	}

	$contents .= <<<EOF
<li>
<a href="$url" target="_blank">
  <img src="/img/uploads/bnr_link/$image" alt="$title">
</a>
<span>
  <span class="cateIcon $select">$talent_name</span>
  <span class="linkname">$title</span>
  <a href="$url" target="_blank">$url</a>
</span>
</li>
EOF;

  $before_category = $category;
}
?>


<!DOCTYPE html>
<html lang="ja">
<head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# website: http://ogp.me/ns/website#">
<!--[if IE]>
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta http-equiv="imagetoolbar" content="no">
<![endif]-->
<meta charset="utf-8">
<title>PROFILE ｜ seventh avenue</title>
<meta name="description" content="PROFILE ｜ seventh avenue">
<meta name="keywords" content="PROFILE,seventh avenue">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<meta name="format-detection" content="telephone=no">
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
<link rel="stylesheet" href="../css/profile.css" type="text/css">

<!--[if lt IE 9]><script src="/js/html5shiv.js"></script><![endif]-->

<!-- Google Analytics-->
<!--#include virtual="/ssi/ga.html"-->
</head>
<body id="profile">

<div id="container">

<!--#include virtual="/ssi/header.html"-->

<!-- CONTENTS -->
<div id="contents">

<!-- ARTICLE -->
<article>
<section id="list">
<h2>PROFILE</h2>

<div class="inner">
	<div class="caram">

			<ul>
				<li class="talent">
				  <div>
					  <span class="photo">
					    <img src="../img/profile/matsushima_thum.jpg" alt="松嶋菜々子 NANAKO MATSUSHIMA">
					  </span>
					  <nav class="profNav">
					    <ul>
					    <li class="profNav_profile">
					      <a href="./detail.php">PROFILE</a>
					    </li>
					    <li class="profNav_talentNews">
					      <a href="/talent_news/">NEWS</a>
					    </li>
					    <li class="profNav_biography">
					      <a href="/biography/">BIOGRAPHY</a>
					    </li>
					    </ul>
					  </nav>
				  </div>
				</li>


				<li class="talent">
				  <div>
					  <span class="photo">
					    <img src="../img/profile/fujisawa_thum.jpg" alt="藤澤恵麻 EMA FUJISAWA">
					  </span>
					  <nav class="profNav">
					    <ul>
					    <li class="profNav_profile">
					      <a href="./detail.php">PROFILE</a>
					    </li>
					    <li class="profNav_talentNews">
					      <a href="/talent_news/">NEWS</a>
					    </li>
					    <li class="profNav_biography">
					      <a href="/biography/">BIOGRAPHY</a>
					    </li>
					    <li class="profNav_insta">
					      <a href="/blog/">BLOG</a>
					    </li>
					    </ul>
					  </nav>
				  </div>
				</li>


			<li class="talent">
			  <div>
				  <span class="photo">
				    <img src="../img/profile/ito_thum.jpg" alt="伊藤歩 AYUMI ITO">
				  </span>
				  <nav class="profNav">
				    <ul>
				    <li class="profNav_profile">
				      <a href="./detail.php">PROFILE</a>
				    </li>
				    <li class="profNav_talentNews">
				      <a href="/talent_news/">NEWS</a>
				    </li>
				    <li class="profNav_biography">
				      <a href="/biography/">BIOGRAPHY</a>
				    </li>
				    <li class="profNav_insta">
				      <a href="/biography/">INSTAGRAM</a>
				    </li>
				    </ul>
				  </nav>
			  </div>
			</li>

			<li class="talent">
			  <div>
				  <span class="photo">
				    <img src="../img/profile/ito_thum.jpg" alt="伊藤歩 AYUMI ITO">
				  </span>
				  <nav class="profNav">
				    <ul>
				    <li class="profNav_profile">
				      <a href="./detail.php">PROFILE</a>
				    </li>
				    <li class="profNav_talentNews">
				      <a href="/talent_news/">NEWS</a>
				    </li>
				    <li class="profNav_biography">
				      <a href="/biography/">BIOGRAPHY</a>
				    </li>
				    <li class="profNav_insta">
				      <a href="/biography/">INSTAGRAM</a>
				    </li>
				    </ul>
				  </nav>
			  </div>
			</li>
			<li class="talent">
			  <div>
				  <span class="photo">
				    <img src="../img/profile/ito_thum.jpg" alt="伊藤歩 AYUMI ITO">
				  </span>
				  <nav class="profNav">
				    <ul>
				    <li class="profNav_profile">
				      <a href="./detail.php">PROFILE</a>
				    </li>
				    <li class="profNav_talentNews">
				      <a href="/talent_news/">NEWS</a>
				    </li>
				    <li class="profNav_biography">
				      <a href="/biography/">BIOGRAPHY</a>
				    </li>
				    <li class="profNav_insta">
				      <a href="/biography/">INSTAGRAM</a>
				    </li>
				    </ul>
				  </nav>
			  </div>
			</li>
			<li class="talent">
			  <div>
				  <span class="photo">
				    <img src="../img/profile/ito_thum.jpg" alt="伊藤歩 AYUMI ITO">
				  </span>
				  <nav class="profNav">
				    <ul>
				    <li class="profNav_profile">
				      <a href="./detail.php">PROFILE</a>
				    </li>
				    <li class="profNav_talentNews">
				      <a href="/talent_news/">NEWS</a>
				    </li>
				    <li class="profNav_biography">
				      <a href="/biography/">BIOGRAPHY</a>
				    </li>
				    <li class="profNav_insta">
				      <a href="/biography/">INSTAGRAM</a>
				    </li>
				    </ul>
				  </nav>
			  </div>
			</li>
		</ul>
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
