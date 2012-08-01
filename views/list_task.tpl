<div class="span4">
		%for item in list_task:
			%if list_task.index(item) % 2 == mod:
			<div class="well">
				<a class="close pull-right" href="/remove/{{item['_id']}}">&times;</a>
				<div id="{{item['_id']}}">
					<p>
						<span class="{{item['tag_class']}}" id="d_tag">{{item['tag']}}</span>
						<div id="d_title">{{item['title']}}</div>
					</p>
					<p id="d_content">
					%for i in item['content'].split('\n'):
{{i}}<br>
					%end
					</p>
				</div>
				
				<a class="btn pull-right" href="/finish/{{item['_id']}}">完成</a>
				<a class="btn pull-right" href="javascirpt:void(0)" onclick="modify($('#{{item['_id']}}'))">修改</a>
				<br>
			</div>
			%end
		%end
</div>