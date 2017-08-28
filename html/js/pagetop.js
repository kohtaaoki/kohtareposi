// JavaScript Document

// page Topフェードイン・アウト
$(function(){
	$(window).bind("scroll", function() {
	if ($(this).scrollTop() > 200) { 
		$(".pageTop").fadeIn();
	} else {
		$(".pageTop").fadeOut();
	}
	// ドキュメントの高さ
	scrollHeight = $(document).height();
	// ウィンドウの高さ+スクロールした高さ→ 現在のトップからの位置
	scrollPosition = $(window).height() + $(window).scrollTop();
	// フッターの高さ
	footHeight = $("footer").height();
	
	// スクロール位置がフッターまで来たら
	if ( scrollHeight - scrollPosition  <= footHeight ) {
		// ページトップリンクをフッターに固定
		$(".pageTop a").css({"position":"absolute","bottom": "-25px"});
	} else {
		// ページトップリンクを右下に固定
		$(".pageTop a").css({"position":"fixed","bottom": "10px"});
		}
	});
});