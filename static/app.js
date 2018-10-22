var username = null;
var password = null;
var date = null;
var movieID = null;
var type = null;
var seatNo = null;
var seatClass = null;
var movieTime = null;
var showID = null;
var startShowing = null;
var endShowing = null;

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

			// Only for cashier, doesn't do anything when logged in as a manager
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

// Functions for cashier

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
			'seatNo' : seatNo,
			'seatClass' : seatClass
			},
		success: function(response){
			$('#available-seats button').prop('disabled', true);
			$('#price-and-confirm').html(response);
		}
	});
}

// Functions for manager
function viewBookedTickets(){
	$('#options button').prop('disabled', true);
	$('#manager-dynamic-1').html('<input id="datepicker-manager-1" placeholder="Pick a date">');

	$('#datepicker-manager-1').pickadate({
				formatSubmit: 'yyyy/mm/dd',
 				hiddenName: true,
 				onSet: function( event ) {
 					if ( event.select ) {
 						$('#datepicker-manager-1').prop('disabled', true);
 						getShowsShowingOnDate(this.get('select', 'yyyy/mm/dd' ));
 					}
 				}
	});
}

function getShowsShowingOnDate(mdate){
	date = mdate;
	$.ajax({
		type: 'POST',
		url: '/getShowsShowingOnDate',
		data: {'date' : date},
		success: function(response){
			$('#manager-dynamic-2').html(response);
		}
	});
}

function selectShow(mshowID){
	showID = mshowID;
	$.ajax({
		type: 'POST',
		url: '/getBookedWithShowID',
		data: {'showID' : showID},
		success: function(response){
			$('#manager-dynamic-2 button').prop('disabled', true)
			$('#manager-dynamic-3').html(response);
		}
	});
}

function insertMovie(){
	$('#options button').prop('disabled', true);
	$.ajax({
		type: 'GET',
		url: '/fetchMovieInsertForm',
		success: function(response){
			$('#manager-dynamic-1').html(response);

			$('#datepicker-manager-2').pickadate({
				formatSubmit: 'yyyy/mm/dd',
 				hiddenName: true,
 				onSet: function( event ) {
 					if ( event.select ) {
 						startShowing = this.get('select', 'yyyy/mm/dd' );
 					}
 				}
			});

			$('#datepicker-manager-3').pickadate({
				formatSubmit: 'yyyy/mm/dd',
 				hiddenName: true,
 				onSet: function( event ) {
 					if ( event.select ) {
 						endShowing = this.get('select', 'yyyy/mm/dd' );
 					}
 				}
			});
		}
	});
}

function filledMovieForm(){
	availTypes = $('[name="movieTypes"]')[0].value.toUpperCase().trim();
	movieName = $('[name="movieName"]')[0].value;
	movieLang = $('[name="movieLang"]')[0].value;
	movieLen = $('[name="movieLen"]')[0].value;

	types = ($('[name="movieTypes"]')[0].value.toUpperCase().trim()).split(' ');
	atleastTypes = ['2D', '3D', '4DX'];
	allTypes = [undefined].concat(atleastTypes);

	if($('#datepicker-manager-2')[0].value == '' || $('#datepicker-manager-3')[0].value == '' ||
	movieName == '' || movieLang == '' || movieLen == '' || $('[name="movieTypes"]')[0].value == '')

		$('#manager-dynamic-2').html('<h5>Please Fill In All Fields</h5>');

	else if(!( atleastTypes.includes(types[0]) && allTypes.includes(types[1]) && allTypes.includes(types[2])) )

		$('#manager-dynamic-2').html('<h5>Invalid Format For Movie Types</h5>');

	else if(! $.isNumeric(movieLen))

		$('#manager-dynamic-2').html('<h5>Movie Length Needs To Be A Number</h5>');

	else if(Date.parse(startShowing) > Date.parse(endShowing) || startShowing === endShowing)

		$('#manager-dynamic-2').html("<h5>Premiere Date Must Be Before Last Date In Theatres</h5>");

	else{
		movieLen = parseInt(movieLen, 10);

		$.ajax({
		type: 'POST',
		url: '/insertMovie',
		data: {
			'movieName' : movieName,
			'movieLen' : movieLen,
			'movieLang' : movieLang,
			'types' : availTypes,
			'startShowing' : startShowing,
			'endShowing' : endShowing
		},
		success: function(response){
			$('#manager-dynamic-2').html(response);
		}
	});
	}
}