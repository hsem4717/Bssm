<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert</title>
</head>
<body>
<script type = "text/javascript" src="check.js"></script>
<jsp:include page="header.jsp"></jsp:include>
<section>
<h1>교과목 추가</h1>
<form method="post" action="action.jsp" name="frm">
<input type="hidden" name = "mode" value="insert">
<table border="1" style="width:70%; text-align:center">
<tr>
<td>과목 코드</td>
<td><input type="text" name="id" style="width: 100%"></td>
</tr>
<tr>
<td>과목명</td>
<td><input type="text" name="name" style="width: 100%"></td>
</tr>
<tr>
<td>학점</td>
<td><input type="text" name="credit" style="width: 100%"></td>
</tr>
<tr>
<td>당담강사</td>
<td><select name="lecturer" style="width: 100%"></td>
</tr>
</form>
</section>
</body>
</html>