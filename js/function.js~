function modify(recode){
	if ($('#form_recode').is(":visible")) {
		$('#form_recode').hide()
	}
	$('#f_id').attr('value',recode.attr('id'))
	$('#f_title').attr('value',recode.find('#d_title').html())
	$('#f_content').attr('value',recode.find('#d_content').html().replace(/<br>/g,'').replace(/\n\n/g,'\n').replace(/\n/,'').replace(/\t/g,'').replace('\r',''))
	$('#f_tag').val(recode.find('#d_tag').html())
	$('#form_recode').fadeIn()
	$('#addrecode').fadeOut()
}
function closeform(){
	if ($('#form_recode').is(":visible")) {
		$('#form_recode').hide()
	}
	$('#f_id').attr('value',"")
	$('#f_title').attr('value',"")
	$('#f_content').attr('value',"")
	$('#f_tag').selectedIndex=0
	$('#addrecode').fadeIn()
}
function showform(){
	if ($('#form_recode').is(":visible")) {
		closeform()
		$('#form_recode').fadeIn()
	}
	else{
		$('#form_recode').fadeIn()
	}
	$('#addrecode').fadeOut()
}
