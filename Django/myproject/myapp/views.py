from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
import random



topics = [
    {'id':1, 'title':'routing', 'body':'Routing is ..'},
    {'id':2, 'title':'view', 'body':'View is ..'},
    {'id':3, 'title':'model', 'body':'Model is ..'}

]

def HTMLTemplate(articleTag):
    global topics
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''

def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django ha
    '''
    return HttpResponse(HTMLTemplate(article))

def create(request):
	global nextId
	if request.method == 'GET':  #get방식과 post방식으로 들어왔을때의 처리를 다르게 해준다
		article = '''
			<form action="/create/" method="post"> #포스트 방식으로 바꿔준다
				<p><input type="text" name="title" placeholder="title"></p> <!--글을 입력할 수 있는 칸을 만들고 title로 이름, placeholder로 보이는 글자를 생성-->
				<p><textarea name="body" placeholder="body"></textarea></p> <!--text area로 여러 줄의 text를 입력-->
				<p><input type="submit"></p>
			</form>  <!--데이터를 원하는 패쓰로 보내주기위해서는 폼태그로 감싸줘야 한다-->
		'''
    return HttpResponse(HTMLTemplate(article))
    
	elif request.method == 'POST'
		title = request.POST['title'] #request.POST로 들어온 값에 이름을 붙여준다
		body = request.POST['body']
		newTopic = {"id":nextId, "title":title, "body":body #위쪽에 있는 토픽에다 추가해 줘야 한다 nextId
		topics.append(newTopic) #새로운 토픽을 기존의 톡픽들에 추가해준다
		url = '/read/'+str(nextId) #nextId 문자열로 바꿔줘야 잘 추가됨
		nextId = n
extId + 1  #계속 id가 4가 아닌 다음 수가 되게 해준다
		return redirect(url) #의미없는 값을 반환해 주는 것이 아닌 nextId가 갱신되기 이전의 url로 이동해 준다

def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article))