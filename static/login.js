// function ins(){
// 	var name = $("#inname")[0].value;
// 	var lang = $("#inlang")[0].value;
// 	var len = $("#inlen")[0].value;
// 	send("ins",[name,lang,len]);
// }
// function del(){
// 	var cond = $("#delcond")[0].value;
// 	send("del",cond);
// }
// function upd(){
// 	var cont = $("#updcont")[0].value;
// 	var cond = $("#updcond")[0].value;
// 	send("upd",[cont,cond]);
// }
// function send(type,params){
// 	var qtype,d;
// 	if(type==="upd"){
// 		qtype = "/update";
// 		d = {'uname':$("#uname")[0].value,
// 			'pswd':$("#pswd")[0].value,
// 			'cont':params[0],
// 			'cond':params[1]};
// 	}
// 	if(type==="del"){
// 		qtype = "/delete";
// 		d = {'uname':$("#uname")[0].value,
// 			'pswd':$("#pswd")[0].value,
// 			'cond':params};
// 	}
// 	if(type==="ins"){
// 		qtype = "/insert";
// 		d = {'uname':$("#uname")[0].value,
// 			'pswd':$("#pswd")[0].value,
// 			'name':params[0],
// 			'lang':params[1],
// 			'len':params[2]};
// 	}
// 	console.log(qtype);
// 	console.log(d);
// 	$.ajax({
// 		type: "POST",
// 		url: qtype,
// 		data: d,
// 		success: function(data){
// 			var res = data['res'];
// 			$("#status")[0].innerHTML="Status: "+res;
// 		},
// 		error: function(data){
// 			$("#status")[0].innerHTML="Status: Login failure";
// 		}
// 	});
// }

function login(){
	var form = {
		'username' : $("[name='username']")[0].value,
		'password' : $("[name='password']")[0].value
	};
	$.ajax({
		type: 'POST',
		url: '/login',
		data: form,
		success: function(response){
			$('html').html(response);
		}
	});
}