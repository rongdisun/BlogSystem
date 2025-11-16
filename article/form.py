from django import forms
from tinymce.widgets import TinyMCE
from .models import Article


class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "summary", "cover", "content", "author", "category", "tags"]

        widgets = {
            "author": forms.HiddenInput(),
            # 单选 Select2（Category）
            "category": forms.Select(attrs={'class': 'select2-input'}),

            # 多选 Select2（Tag）
            "tags": forms.SelectMultiple(attrs={'class': 'select2-input'}),
        }
