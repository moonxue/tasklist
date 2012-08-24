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
	<form method="post" action="/login">
   {{!form.csrf_token }}
   用户名:{{!form.username(size=20) }}<br/>
   密 码 :{{!form.pw(size=20) }}<br/>
   {{!form.submit() }}
</form>
</body>
</html>