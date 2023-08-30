from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone
from django.db.models import Q,Count
from django.contrib.auth.decorators import login_required
from ..models import Comment,Answer
from ..forms import CommentForm
from django.contrib import messages


@login_required(login_url='common:login')
def comment_create(request, answer_id):
    # pybo 답글 등록
    answer=get_object_or_404(Answer ,pk=answer_id)
    if request.method == "POST":
        form=CommentForm(request.POST)
        # Form이 유효한지 체크
        if form.is_valid():
            comment = form.save(Commit=False)
            comment.author=request.user
            comment.create_date = timezone.now()
            comment.answer=answer
            comment.save()
            return redirect('pybo:detail', question_id=comment.answer.question.id)
        
    else:
        form = CommentForm()
    context={'form':form}
    return render(request,'pybo/comment_form.html',context)

@login_required(login_url='common:login')
def comment_modify(request, comment_id):
    comment=get_object_or_404(Comment, pk=comment_id)
    if request.user!= comment.author:
        messages.error(request, "수정 권한이 없습니다.")
        return redirect('pybo:detail', question_id= comment.answer.question.id)
    
    if request.method == "POST":
        form=CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('pybo:detail',question_id=comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    context={'form':form}
    return render(request,'pybo/comment_form.html',context)    
                                      
        

@login_required(login_url='common:login')
def comment_delete(request, comment_id):
    comment=get_object_or_404(Comment, pk= comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글 삭제 권한이 없습니다')
        return redirect('pybo:detail',question_id=comment.answer.question.id)
    else:
        comment.delete()
    
    return redirect('pybo:detail',question_id=comment.answer.question.id)
