from django import forms
from .models import Comment, Post
"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('user', 'email', 'body')
"""
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
                'slug',
                'title',
                'content',
                'd_p_b_o',
                'd_t_o_p_z',
                'd_p_a_v_e_f',
                'n_e_p_v_i_s',
                'n_c_k',
                'r_o_z',
                'r_o_i_k',
                'category',
                'status',
                'user'
                )
        widgets = {
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'd_p_b_o': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'd_t_o_p_z': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'd_p_a_v_e_f': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'n_e_p_v_i_s': forms.Select(attrs={'class': 'form-control'}),
            'n_c_k': forms.NumberInput(attrs={'class': 'form-control'}),
            'r_o_z': forms.NumberInput(attrs={'class': 'form-control'}),
            'r_o_i_k': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }
