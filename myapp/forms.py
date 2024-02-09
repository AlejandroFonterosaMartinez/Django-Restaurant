from django import forms
from .models import Plato

class NuevoPlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre', 'categoria', 'descripcion', 'precio', 'imagen']

    def save(self, commit=True):
        # Guardar el formulario sin confirmar para obtener la instancia del modelo
        plato = super().save(commit=False)
        if self.cleaned_data['imagen']:
            # Obtener el nuevo nombre del archivo basado en el nombre del plato
            nuevo_nombre = f"{self.cleaned_data['nombre']}{self.cleaned_data['imagen'].name[self.cleaned_data['imagen'].name.rfind('.'):]}"
            # Guardar la imagen en la carpeta media con el nuevo nombre
            plato.imagen.name = nuevo_nombre
            plato.save()  # Guardar el objeto plato en la base de datos
        if commit:
            # Guardar el objeto plato en la base de datos
            plato.save()
        return plato
    

