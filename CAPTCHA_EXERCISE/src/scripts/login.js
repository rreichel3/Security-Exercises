
function login(form){
	if (form.username.value=="admin"){
		if (form.password.value=="5f4dcc3b5aa765d61d8327deb882cf99") {
			alert("Access Granted");
		} else {
			alert("Failed");
		}
	} else {
		alert("Failed");
	}
};