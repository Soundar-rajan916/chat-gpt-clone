from django.shortcuts import render, get_object_or_404, redirect
from django.http import StreamingHttpResponse ,HttpResponse
from django.contrib.auth.decorators import login_required
from .llm import stream_chat_response, generate_title
from .models import Thread, Message
from langchain_core.messages import HumanMessage, AIMessage
@login_required
def home(request):
    return render(request, "home.html")

@login_required
def view_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id, user=request.user)
    return render(request, "home.html", {"active_thread": thread})

@login_required
def new_message(request, thread_id):
    if request.method == "POST":
        thread = get_object_or_404(Thread, id=thread_id, user=request.user)
        message_content = request.POST.get("message", "")

        if message_content:
            Message.objects.create(thread=thread, role="user", content=message_content)
            
            
            if thread.messages.count() == 1:
                thread.title = generate_title(message_content)
                thread.save()

        db_messages = thread.messages.order_by('created_at')
        history = []
        for msg in db_messages:
            if msg.role == "user":
                history.append(HumanMessage(content=msg.content))
            elif msg.role == "assistant":
                history.append(AIMessage(content=msg.content))
        previous_history = history[:-1][-20:] if history else []

        def response_stream():
            full_response = ""
            for chunk in stream_chat_response(previous_history, message_content):
                full_response += chunk
                yield chunk
            
            
            if full_response:
                Message.objects.create(thread=thread, role="assistant", content=full_response)

        return StreamingHttpResponse(
            response_stream(),
            content_type="text/plain"
        )

@login_required
def user_threads(request):      
    threads = Thread.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, "user_threads.html", {"threads": threads})

@login_required
def new_message_initial(request):
    if request.method == "POST":
        message_content = request.POST.get("message", "")
        if not message_content:
            return redirect("chat:home")
            
        thread = Thread.objects.create(user=request.user, title="New Chat")
        Message.objects.create(thread=thread, role="user", content=message_content)
        
        thread.title = generate_title(message_content)
        thread.save()
        
        def response_stream():
            full_response = ""
            for chunk in stream_chat_response([], message_content):
                full_response += chunk
                yield chunk
            
            if full_response:
                Message.objects.create(thread=thread, role="assistant", content=full_response)
                
            # Yield metadata cleanly so the frontend can parse it and update the UI without script tags
            yield f'\n\n---REDIRECT---/chat/{thread.id}/---TITLE---{thread.title}'

        return StreamingHttpResponse(
            response_stream(),
            content_type="text/plain"
        )
    return redirect("chat:home")