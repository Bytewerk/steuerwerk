/*
 * Small script to make XMLHttpRequests from the infrared control page
 * so that buttons will respond more swiftly.
 */
"use strict";

function sendCmd(target,cmd){
	var req = new XMLHttpRequest();
	var param = encodeURIComponent(cmd);
	req.open("POST",target);
	req.onreadystatechange = function() {
		/* stop the web server from delivering the site content which the user can't see */
		if (req.readyState == 2){ req.abort(); }
	}
	req.setRequestHeader("Content-type", "application/x-www-form-urlencoded"); // necessary to correctly submit the parameters
	req.send("cmd="+cmd);
}

function initButtons(){
	var forms = document.getElementsByTagName("form");
	for(var f=0; f<forms.length; ++f){
		var form = forms[f];
		console.log(form);
		var buttons = form.getElementsByClassName("button");
		for(var i=0; i<buttons.length; ++i){
			var button = buttons[i];
			button.onclick = function(target, cmd){ return function(){
					sendCmd(target, cmd);
					return false;
			}}(form.action,button.value);
			/* defining a function in place and calling it right away
			 * avoids a nasty closure surprise.
			 */
		}
	}
}

initButtons();
