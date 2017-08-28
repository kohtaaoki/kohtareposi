/**
 * getStartEnd
 * @param obj
 * @return
 * @author yamaguchi
 */
function getStartEnd(obj){
	var start = 0;
	var end = 0;
	if(navigator.userAgent.indexOf("MSIE") != -1){
		obj.focus();
		var range = document.selection.createRange();
		var clone = range.duplicate();
		clone.moveToElementText(obj);
		clone.setEndPoint('EndToEnd', range);
		start = clone.text.length - range.text.length;
		end = clone.text.length - range.text.length + range.text.length;
	}
	else{
		start = obj.selectionStart;
		end = obj.selectionEnd;
	}
	return {start:start, end:end};
}


/**
 * insertFontTag
 * @param text
 * @param property
 * @param value
 * @return
 * @author yamaguchi
 */
function insertFontTag(text, property, value){

	if(property == "size"){
		property = "font-size";
	}
	var obj = document.forms['main'].elements[text];
	var selectArea = getStartEnd(obj);
	obj.value = obj.value.substr(0, selectArea.end) + "</span>" + obj.value.substr(selectArea.end);
	obj.value = obj.value.substr(0, selectArea.start) + '<span @__PROPERTY__@="@__VALUE__@">' + obj.value.substr(selectArea.start);
	obj.value = obj.value.replace("@__PROPERTY__@", "style");
	obj.value = obj.value.replace("@__VALUE__@", property + ":" + value);
}

/**
 * insertDivTag
 * @param text
 * @param property
 * @param value
 * @return
 * @author yamaguchi
 */
function insertDivTag(text, property, value){
	var obj = document.forms['main'].elements[text];
	var selectArea = getStartEnd(obj);
	obj.value = obj.value.substr(0, selectArea.end) + "</div>" + obj.value.substr(selectArea.end);
	obj.value = obj.value.substr(0, selectArea.start) + '<div @__PROPERTY__@="@__VALUE__@">' + obj.value.substr(selectArea.start);
	obj.value = obj.value.replace("@__PROPERTY__@", property);
	obj.value = obj.value.replace("@__VALUE__@", value);
}

/**
 * insertBoldTag
 * @param text
 * @return
 * @author yamaguchi
 */
function insertBoldTag(text){

	var obj = document.forms['main'].elements[text];
	var selectArea = getStartEnd(obj);
	obj.value = obj.value.substr(0, selectArea.end) + "</b>" + obj.value.substr(selectArea.end);
	obj.value = obj.value.substr(0, selectArea.start) + "<b>" + obj.value.substr(selectArea.start);
}

/**
 * insertItalicTag
 * @param text
 * @return
 * @author yamaguchi
 */
function insertItalicTag(text){
	var obj = document.forms['main'].elements[text];
	var selectArea = getStartEnd(obj);
	obj.value = obj.value.substr(0, selectArea.end) + "</i>" + obj.value.substr(selectArea.end);
	obj.value = obj.value.substr(0, selectArea.start) + "<i>" + obj.value.substr(selectArea.start);
}

/**
 * insertStrikeTag
 * @param text
 * @return
 * @author yamaguchi
 */
function insertStrikeTag(text){
	var obj = document.forms['main'].elements[text];
	var selectArea = getStartEnd(obj);
	obj.value = obj.value.substr(0, selectArea.end) + "</s>" + obj.value.substr(selectArea.end);
	obj.value = obj.value.substr(0, selectArea.start) + "<s>" + obj.value.substr(selectArea.start);
}

/**
 * insertUnderbarTag
 * @param text
 * @return
 * @author yamaguchi
 */
function insertUnderbarTag(text){
	var obj = document.forms['main'].elements[text];
	var selectArea = getStartEnd(obj);
	obj.value = obj.value.substr(0, selectArea.end) + "</u>" + obj.value.substr(selectArea.end);
	obj.value = obj.value.substr(0, selectArea.start) + "<u>" + obj.value.substr(selectArea.start);
}

/**
 * insertAnchorTag
 * @param text
 * @return
 * @author yamaguchi
 */
function insertAnchorTag(text, url, target){
	var obj = document.forms['main'].elements[text];
	var selectArea = getStartEnd(obj);
	var t = "";
	if(target == "_blank"){
		t = " target=\"_blank\"";
	}
	obj.value = obj.value.substr(0, selectArea.end) + "</a>" + obj.value.substr(selectArea.end);
	obj.value = obj.value.substr(0, selectArea.start) + "<a href=\"" + url + "\"" + t + ">" + obj.value.substr(selectArea.start);
}

/**
 * openSubwin
 * @return
 * @author yamaguchi
 */
function openSubwin(target, idx){
	var id = "anchor";
	if(idx == 2){
		id = "palette";
	}
	if(idx == 3){
		id = "fontsize";
	}
	id = id + "_" + target;
	var p = document.getElementById(id);
	var sub_win = document.getElementById("sub_win_" + target);
	if(sub_win.innerHTML.substr(0, 50) != p.innerHTML.substr(0, 50)){
		sub_win.innerHTML = p.innerHTML;
		sub_win.style.display = "block";
	}
	else{
		sub_win.innerHTML = "";
		sub_win.style.display = "none";
	}
}

/**
 * closeSubwin
 * @return
 * @author yamaguchi
 */
function closeSubwin(target){
	var sub_win = document.getElementById("sub_win_" + target);
	sub_win.innerHTML = "";
	sub_win.style.display = "none";
}