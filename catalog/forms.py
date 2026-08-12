from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):
    FORBIDDEN_WORDS = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "порно",
        "xxxx",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "image":
                field.widget.attrs["class"] = "form-control"

    def clean_name(self):
        name = self.cleaned_data.get("name").lower()
        for word in self.FORBIDDEN_WORDS:
            if word in name:
                raise ValidationError("Название продукта содержит запрещенное слово")
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description").lower()
        for word in self.FORBIDDEN_WORDS:
            if word in description:
                raise ValidationError(
                    "В описании продукта обнаружены недопустимые слова (спам)."
                )
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if not image:
            return image
        if image.size > 5242880:
            raise ValidationError("Размер файла не должен превышать 5 Мб")

        if not image.name.lower().endswith((".jpg", ".jpeg", ".png")):
            raise ValidationError("Допустимый формат файла JPEG или PNG.")

        return image
