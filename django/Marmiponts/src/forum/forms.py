from django import forms
from forum.models import Thread
from forum.models import Post


class ThreadForm(forms.ModelForm):
	class Meta:
	    model = Thread
	    exclude = ('forum',)

class PostForm(forms.ModelForm):
	class Meta:
	    model = Post
	    exclude = ('thread',)
