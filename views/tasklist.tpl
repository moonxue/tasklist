<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
			<link rel="stylesheet" href="/css/bootstrap.css" type="text/css" />
			<title>TaskList</title>
	</head>
<body style="">
<div class="container">
	<div class="page-header">
	    <h1>TaskList <small>任务跟踪小工具</small></h1>
	</div>
	<div class="span2 pull-right btn btn-info" onclick="showform();" id="addrecode">添加事项</div>
	<h3 style="color:green;margin:0px 0px 5px 30px;">待办事项</h3>
	<div class="row-fluid span7">
	%include list_task.tpl list_task = list_task, mod = 0
	%include list_task.tpl list_task = list_task, mod = 1
	</div>
	<div class="span4 offset10" style="position:fixed">
			<form class="well" action="/update_recode" method="post" id="form_recode">
				<a class="close pull-right" onclick="closeform();">&times;</a>
				<input type="hidden" id="f_id" name="_id" value="">
				<label for="f_title">标题</label>
				<input type="text" class="span2" id="f_title" name="title">
				<label for="f_tag">标签</label>
				<select class="span2" id="f_tag" name="tag">
					<option>普通</option>
					<option>备忘</option>
					<option>重要</option>
				</select>
				<label for="f_content">内容</label>
				<textarea class="large" row="5" style="height:100px" id="f_content" name="content" value=""></textarea>
				<input type="submit" class="btn btn-success" value="保存计划" id="f_submit">
			<form>
	</div>
	<br>
	<h3 style="color:green;margin:0px 0px 5px 30px;">完成事项</h3>
	<div class="row-fluid span7">
	%include list_done.tpl list_done = list_done, mod = 0
	%include list_done.tpl list_done = list_done, mod = 1
	</div>	
</div>
	<script src="/js/jquery-1.7.1.min.js"></script>
	<script src="/js/bootstrap.js"></script>
	<script src="/js/function.js"></script>
	<script>
	$('#form_recode').hide()
	</script>
</body>
</html>