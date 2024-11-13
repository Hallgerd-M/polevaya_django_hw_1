from django.core.exceptions import ValidationError
from django.forms import ModelForm

from catalog.models import Product

forbidden_words = [
    "крипта",
    "криптовалюта",
    "казино",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("owner",)

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите наименование"}
        )
        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )
        self.fields["image"].widget.attrs.update({"class": "form-control"})
        self.fields["category"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Выберите категорию"}
        )
        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену"}
        )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError("Вы использовали слово из запрещенного списка")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError("Вы использовали слово из запрещенного списка")
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ("publication_status",)
