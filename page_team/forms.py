from django import forms

from page_team.models import ShopComment

class ShopCommentForm(forms.ModelForm):
    class Meta:
        model = ShopComment
        fields = ['text' , 'recommend']