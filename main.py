from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
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
    pass


class CityGenApp(App):

    def build(self):
        app = LayoutWidget()
        return app


if __name__ == '__main__':
    CityGenApp().run()
