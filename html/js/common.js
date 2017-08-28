/*スムーズスクロール*/
$(function(){
	$('a[href^=#]').click(function(){
		var speed = 500;
		var href= $(this).attr("href");
		var target = $(href == "#" || href == "" ? 'html' : href);
		var position = target.offset().top;
		$("html, body").animate({scrollTop:position}, speed, "swing");
		return false;
	});
});


/*コピーガード*/
jQuery.fn.protectImage = function(settings) {
	$("img[name=blank]").remove();

	settings = jQuery.extend({
		image: '../img/base/spacer.gif',
		zIndex: 10
	}, settings);
	return this.each(function() {
		var position = $(this).position();
		var height = $(this).height();
		var width = $(this).width();
		$('<img />').attr({
			width: width,
			height: height,
			src: settings.image,
			name : "blank"
		}).css({
			top: position.top,
			left: position.left,
			position: 'absolute',
			zIndex: settings.zIndex
		}).appendTo('#contents')
	});
};

$(window).bind('load', function() {
	$('.photo').protectImage();
});

$(window).bind('resize', function() {
	$('.photo').protectImage();
});
