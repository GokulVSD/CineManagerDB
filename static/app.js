var username = null;
var password = null;
var date = null;
var movieID = null;
var type = null;
var seatNo = null;
var seatClass = null;
var movieTime = null;
var showID = null;

function login(){
	if(username === null){
		username = $("[name='username']")[0].value;
		password = $("[name='password']")[0].value;
	}
	var form = {
		'username' : username,
		'password' : password
	};
	$.ajax({
		type: 'POST',
		url: '/login',
		data: form,
		success: function(response){
			$('#dynamic').html(response);
			$('.login-header').addClass('after-login');
			$('.module').addClass('module-after-login');
			$('#datepicker-cashier').pickadate({
				min : new Date(),
				formatSubmit: 'yyyy/mm/dd',
 				hiddenName: true,
 				onSet: function( event ) {
 					if ( event.select ) {
 						$('#datepicker-cashier').prop('disabled', true);
 						getMoviesShowingOnDate(this.get('select', 'yyyy/mm/dd' ));
 					}
 				}
			});
		}
	});
}

function getMoviesShowingOnDate(mdate){
	date = mdate;
	$.ajax({
		type: 'POST',
		url: '/getMoviesShowingOnDate',
		data: {'date' : date},
		success: function(response){
			$('#movies-on-date').html(response);
		}
	});
}

function selectMovie(movID, mtype){
	movieID = movID;
	type = mtype;
	$.ajax({
		type: 'POST',
		url: '/getTimings',
		data: {
			'date' : date,
			'movieID': movieID,
			'type' : type
		},
		success: function(response){
			$('#movies-on-date button').prop('disabled', true);
			$('#timings-for-movie').html(response);
		}
	});
}

function selectTiming(mtime){
	movieTime = mtime;
	$.ajax({
		type: 'POST',
		url: '/getShowID',
		data: {
			'date' : date,
			'movieID': movieID,
			'type' : type,
			'time' : movieTime
		},
		success: function(response){
			$('#timings-for-movie button').prop('disabled', true);
			showID = response['showID'];
			getSeats();
		}
	});
}

function getSeats(){
	$.ajax({
		type: 'POST',
		url: '/getAvailableSeats',
		data: {'showID' : showID},
		success: function(response){
			$('#available-seats').html(response);
		}
	});
}

function selectSeat(no, sclass){
	seatNo = no;
	seatClass = sclass;
	$.ajax({
		type: 'POST',
		url: '/getPrice',
		data: {
			'showID' : showID,
			'seatClass' : seatClass
			},
		success: function(response){
			$('available-seats button').prop('disabled', true);
			$('#price-and-confirm').html(response);
		}
	});
}

function confirmBooking(){
	$.ajax({
		type: 'POST',
		url: '/insertBooking',
		data: {
			'showID' : showID,
			'seatNo' : seatNo
			},
		success: function(response){
			$('#price-and-confirm').html(response);
		}
	});
}