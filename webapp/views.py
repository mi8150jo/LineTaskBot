from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from taskmanagement.models import Task
import logging
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from datetime import timedelta
from django.utils import timezone
from django import forms
from django.http import HttpResponse, HttpResponseRedirect

def home(request):
    # ログインしているとき
    if request.user.is_authenticated:
        social_accounts = SocialAccount.objects.filter(user=request.user)
        tasks = Task.objects.filter(user_ID=request.user, date__gte=timezone.now().date()).order_by('date', 'startTime')
        logging.debug(tasks)

        return render(request, "remindbot/home.html", {
            "social_accounts": social_accounts,
            "tasks": tasks,
        })

def pastTask(request):
    if request.user.is_authenticated:
        social_accounts = SocialAccount.objects.filter(user=request.user)
        tasks = Task.objects.filter(user_ID=request.user, date__lt=timezone.now().date()).order_by('date', 'startTime')
        logging.debug(tasks)

        return render(request, "remindbot/pastTask.html", {
            "social_accounts": social_accounts,
            "tasks": tasks,
        })

class TaskForm(forms.ModelForm):
    content = forms.CharField(label="タスク", widget=forms.TextInput(attrs={'class': 'custom-class'}))
    date = forms.DateField(label="日付", widget=forms.DateInput(attrs={'type': 'date'}))
    startTime = forms.TimeField(label="開始時刻", widget=forms.TimeInput(attrs={'type': 'time'}))
    endTime = forms.TimeField(label="終了時刻", widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Task
        fields = ['content', 'date', 'startTime', 'endTime']

class TaskCreateView(CreateView):
    """
    新規登録
    """

    form_class = TaskForm
    template_name = "remindbot/task_form.html"


    def form_valid(self, form):
        # ログインしているユーザーの情報を取得
        user_id = self.request.user

        # フォームのuser_IDにユーザーのIDを設定
        form.instance.user_ID = user_id

        # リマインドする日をフォームのデータがバリデーションを通過した後のdateを取得する
        remind_date = form.cleaned_data['date'] - timedelta(days=1)

        # 過去の日付が入力された場合
        if remind_date < timezone.now().date():
            form.add_error('date', '過去の日付は指定できません')
            return self.form_invalid(form)

        # フォームのremind_dateに設定
        form.instance.remind_date = remind_date

        # フォームが有効なら保存
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    """
    編集
    """

    model = Task

    # 更新項目
    # fields = ['content', 'date', 'startTime', 'endTime']
    form_class = TaskForm

    # テンプレートファイル名の接尾辞の指定
    template_name = 'remindbot/update_form.html'


class TaskDeleteView(DeleteView):
    """
    削除
    """

    model = Task

    template_name = 'remindbot/task_confirm_delete.html'

    # 削除完了後のリダイレクト先
    success_url = reverse_lazy('webapp:home')

class TaskDetailView(DetailView):
    model = Task
    template_name = 'remindbot/task_detail.html'
    context_object_name = 'task'