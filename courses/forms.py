from django import forms
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Text, Image, File, Video, Module, Course, Content, CourseAdmin
from accounts.models import User


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'overview', 'access_key']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'overview': forms.Textarea(attrs={'class': 'form-control'}),
            'access_key': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TextContentForm(forms.ModelForm):
    visible = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['visible'].widget.attrs.update({'class': 'form-check-input'})

    module_id = forms.CharField(widget=forms.HiddenInput, required=False)
    content_id = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Text
        fields = ['title', 'content', 'visible']


class TextContentCreateForm(forms.Form):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea())
    visible = forms.BooleanField(required=False)
    module_id = forms.CharField(widget=forms.HiddenInput, required=False)
    content_id = forms.CharField(widget=forms.HiddenInput, required=False)


    def save(self, owner=None, module=None, course=None):
        if not owner or not module or not course:
            raise ValidationError("siema")

        data = self.cleaned_data
        item = Text(
            title=data['title'], 
            content=data['content']
        )
        item.save()

        content = Content(
            module=module, 
            course=course, 
            owner=owner, 
            visible=data['visible'], 
            item=item
        )
        content.save()

        return content


class ImageContentCreateForm(forms.Form):
    title = forms.CharField(max_length=200)
    file = forms.ImageField()
    visible = forms.BooleanField(required=False)
    module_id = forms.CharField(widget=forms.HiddenInput, required=False)
    content_id = forms.CharField(widget=forms.HiddenInput, required=False)


    def save(self, owner=None, module=None, course=None):
        if not owner or not module or not course:
            raise ValidationError("siema")

        data = self.cleaned_data
        item = Image(
            title=data['title'], 
            file=data['file']
        )
        item.save()

        content = Content(
            module=module, 
            course=course, 
            owner=owner, 
            visible=data['visible'], 
            item=item
        )
        content.save()

        return content


class FileContentCreateForm(forms.Form):
    title = forms.CharField(max_length=200)
    file = forms.FileField()
    visible = forms.BooleanField(required=False)
    module_id = forms.CharField(widget=forms.HiddenInput, required=False)
    content_id = forms.CharField(widget=forms.HiddenInput, required=False)


    def save(self, owner=None, module=None, course=None):
        if not owner or not module or not course:
            raise ValidationError("siema")

        data = self.cleaned_data
        item = File(
            title=data['title'], 
            file=data['file']
        )
        item.save()

        content = Content(
            module=module, 
            course=course, 
            owner=owner, 
            visible=data['visible'], 
            item=item
        )
        content.save()

        return content


class VideoContentCreateForm(forms.Form):
    title = forms.CharField(max_length=200)
    file = forms.URLField()
    visible = forms.BooleanField(required=False)
    module_id = forms.CharField(widget=forms.HiddenInput, required=False)
    content_id = forms.CharField(widget=forms.HiddenInput, required=False)

    def save(self, owner=None, module=None, course=None):
        if not owner or not module or not course:
            raise ValidationError("siema")

        data = self.cleaned_data
        item = Video(
            title=data['title'], 
            file=data['file']
        )
        item.save()

        content = Content(
            module=module, 
            course=course, 
            owner=owner, 
            visible=data['visible'], 
            item=item
        )
        content.save()

        return content


class TextUpdateForm(forms.ModelForm):
    content_id = forms.CharField(widget=forms.HiddenInput, required=False)
    visible = forms.BooleanField(required=False)

    class Meta:
        model = Text
        fields = ['title', 'content']


class ImageUpdateForm(forms.ModelForm):
    content_id = forms.CharField(widget=forms.HiddenInput, required=False)
    visible = forms.BooleanField(required=False)

    class Meta:
        model = Image
        fields = ['title', 'file']


class FileUpdateForm(forms.ModelForm):
    content_id = forms.CharField(widget=forms.HiddenInput, required=False)
    visible = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = File
        fields = ['title', 'file']


class VideoUpdateForm(forms.ModelForm):
    content_id = forms.CharField(widget=forms.HiddenInput, required=False)
    visible = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Video
        fields = ['title', 'file']


class ModuleCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'autocomplete': 'off'})

    class Meta:
        model = Module
        fields = ['title', 'description', 'visible']


class AddUserToCourseForm(forms.ModelForm):
    participants = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['participants'].widget.attrs.update({'class': 'form-control', 'style': "max-height: 100px;"})

    class Meta:
        model = Course
        fields = ['participants']


class AddAdminsToCourseForm(forms.ModelForm):
    admins = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
    )

    def __init__(self, course, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.course = course
        self.fields['admins'].widget.attrs.update({
            'class': 'form-control', 
            'style': "max-height: 100px;"
        })
        self.fields['admins'].queryset = (self.fields['admins']
            .queryset.exclude(id=self.course.owner.id)
            .filter(teacher=True))


    class Meta:
        model = Course
        fields = ['admins']


class CourseAdminCreateForm(forms.ModelForm):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        required=False, 
        disabled=True,
        widget=forms.HiddenInput()
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
    )

    class Meta:
        model = CourseAdmin
        fields = [
            'user', 
            'course', 
            'can_edit_participants', 
            'can_edit_content', 
            'can_edit_course'
        ]

    def __init__(self, course, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.course = course
        self.fields['user'].queryset = self.fields['user'] \
                                        .queryset.exclude(id__in=course.admins.all().distinct())
        self.fields['user'].widget.attrs.update({
            'id': "search-user",
            "autocomplete":"off"
        })

        get_arg_str = "?course=%s" % self.course.id
        self.fields['user'].widget.attrs.update({'endpoint': reverse('api:users:user-search-no-admins') + get_arg_str })
        self.fields['user'].widget.template_name = "accounts/widgets/js_model_choice_field.html"


class CourseAdminUpdateForm(forms.ModelForm):
    class Meta:
        model = CourseAdmin
        fields = [
            'can_edit_participants',
            'can_edit_content',
            'can_edit_course'
        ]