from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages as django_messages
from .models import User, Message
from .forms import UserForm, MessageForm, MessageEditForm, MessageReturnForm


def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['user_id'] = user.id
            return redirect('chat')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def chat(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('register')

    user = User.objects.get(id=user_id)

    if request.method == "POST":

        if 'edit_message_id' in request.POST:
            message_id = request.POST['edit_message_id']
            message = get_object_or_404(Message, id=message_id)
            if message.user == user:
                form = MessageEditForm(request.POST, instance=message)
                if form.is_valid():
                    form.save()
                    django_messages.success(request, 'Сообщение успешно изменено!')  # ИСПРАВЛЕНО
                    return redirect('chat')


        elif 'delete_message_id' in request.POST:
            message_id = request.POST['delete_message_id']
            message = get_object_or_404(Message, id=message_id)
            if message.user == user:
                request.session['backup_user_id'] = message.user.id
                request.session['backup_content'] = message.content
                message.delete()
                django_messages.success(request, 'Message deleted successfully')  # ИСПРАВЛЕНО
                return redirect('chat')


        elif 'return_message' in request.POST or 'return_message_id' in request.POST:
            backup_content = request.session.get('backup_content')
            if backup_content:
                form = MessageReturnForm({'content': backup_content})
                if form.is_valid():
                    returnmessage = form.save(commit=False)
                    returnmessage.user = user
                    returnmessage.save()
                    django_messages.success(request, 'Message returned successfully')  # ИСПРАВЛЕНО
                    del request.session['backup_user_id']
                    del request.session['backup_content']
                    return redirect('chat')


        else:
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.user = user
                message.save()
                return redirect('chat')


    chat_messages = Message.objects.all().order_by('-timestamp')

    context = {
        'form': MessageForm(),
        'edit_form': MessageEditForm(),
        'chat_list': chat_messages,
        'user': user
    }
    return render(request, 'chat.html', context)