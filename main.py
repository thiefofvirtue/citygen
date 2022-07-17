from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)

from city import City


class SubmitButton(Button):

    def update(self, output_object: Label, name=None, size_arg=None):
        new_city = City(name=name, size=size_arg)
        new_city.generate()
        city_data = f"""
        Name: {new_city.name}
        Population: {new_city.population} (children: {new_city.child_pop})
        Area: {new_city.area} square miles
        """
        output_object.text = city_data


class LayoutWidget(BoxLayout):
    submit = ObjectProperty(None)
    output = ObjectProperty(None)

    pass


class CityGenApp(App):

    def build(self):
        app = LayoutWidget()
        return app


if __name__ == '__main__':
    CityGenApp().run()
