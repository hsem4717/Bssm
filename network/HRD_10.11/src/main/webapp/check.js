function addCheck(){
	if(document.frm.id.value.length == 0){
		alert("교과목 코드가 입력되지 않았습니다");
		frm.d.focus();
		return false;
	}
}