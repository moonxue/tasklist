<div class="span4">
		%for item in list_done:
			%if list_done.index(item) % 2 == mod:
			<div class="well">
				<a class="close pull-right" href="/remove/{{item['_id']}}">&times;</a>
				<div id="{{item['_id']}}">
					<p>
						<span class="{{item['tag_class']}}" id = "d_tag">{{item['tag']}}</span>
						<div id="d_title">{{item['title']}}</div>
					</p>
					<p id = "d_content">
					%for i in item['content'].split('\n'):
						{{i}}
						<br>
					%end
					</p>
				</div>
				<br>
			</div>
			%end
		%end
</div>