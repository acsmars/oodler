function oodley(oodle,doodle) {
	oodle = oodle.toLowerCase();
	function listGet(list,index) {
		if ((index < 0) || (index > list.length - 1)) return ' ';
		return list[index];
	}
	if ("aeiou ".indexOf(listGet(oodle,doodle+1)) > -1) return false;
	if (("aeiou ".indexOf(listGet(oodle,doodle-1)) > -1) && (listGet(oodle,doodle+1) !== ' ')) return false;
	return true;
}

function oodlr(oodle) {
	mode = $('input[name=mode]:checked', '#oodleForm').val();
	noodle = '';
	var doodle = 0;
	switch (mode) {
		case 'accent':
			for (doodle = 0; doodle < oodle.length; doodle++ ) {
				switch (oodle[doodle]) {
					case 'a':
						noodle += "oôdle";
						break;
					case 'e':
						noodle += "oödle";
						break;
					case 'i':
						noodle += "oòdle";
						break;
					case 'o':
						noodle += "oódle";
						break;
					case 'u':
						noodle += "oōdle";
						break;
					case 'y':
						if (oodley(oodle,doodle)) {noodle += "oodle";}
						else {noodle += oodle[doodle];}
						break;
					case 'A':
						noodle += "Oôdle";
						break;
					case 'E':
						noodle += "Oödle";
						break;
					case 'I':
						noodle += "Oòdle";
						break;
					case 'O':
						noodle += "Oódle";
						break;
					case 'U':
						noodle += "Oōdle";
						break;
					case 'Y':
						if (oodley(oodle,doodle)) {noodle += "oodle";}
						else {noodle += oodle[doodle];}
						break;
					default:
						noodle += oodle[doodle];
						break;
				}
			}
			break;
		case "binary":
			for (doodle = 0; doodle < oodle.length; doodle++ ) {
				switch (oodle[doodle]) {
					case 'a':
						noodle += "oodlE";
						break;
					case 'e':
						noodle += "oodLe";
						break;
					case 'i':
						noodle += "oodLE";
						break;
					case 'o':
						noodle += "ooDle";
						break;
					case 'u':
						noodle += "ooDlE";
						break;
					case 'y':
						if (oodley(oodle,doodle)) {noodle += "ooDLe";}
						else {noodle += oodle[doodle];}
						break;
					case 'A':
						noodle += "OodlE";
						break;
					case 'E':
						noodle += "OodLe";
						break;
					case 'I':
						noodle += "OodLE";
						break;
					case 'O':
						noodle += "OoDle";
						break;
					case 'U':
						noodle += "OoDlE";
						break;
					case 'Y':
						if (oodley(oodle,doodle)) {noodle += "ooDLe";}
						else {noodle += oodle[doodle];}
						break;
					default:
						noodle += oodle[doodle];
						break;
				}
			}
			break;
		case 'default':
			for (doodle = 0; doodle < oodle.length; doodle++ ) {
				if (("aeiou".indexOf(oodle[doodle]) > -1) || (oodle[doodle] === 'y' && oodley(oodle,doodle))) {noodle += "oodle";}
				else if (("AEIOU".indexOf(oodle[doodle]) > -1) || (oodle[doodle] === 'Y' && oodley(oodle,doodle))) {noodle += "Oodle";}
				else {noodle += oodle[doodle];}
			}
		break;
	}
	return noodle;
}

function updateOodle() {
	$('#oodleOutput').val(oodlr($('#oodleInput').val()));
}

// Refresh if the radio is switched
$('#oodleForm div').change(function(){
	updateOodle();
});

// Refresh if the oodle button is pressed
$('#oodleButton').click(function() {
	updateOodle();
});

// Refresh if the textarea is updated
$('#oodleInput').keyup(function() {
	updateOodle();
});