from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from city import City, city_types
from kivy.properties import ListProperty, NumericProperty


class RemoveRaceButton(Button):

    def remove_me(self):
        self.parent.parent.remove_widget(self.parent)


class SubmitButton(Button):

    def update(self, output_object: Label, name=None, size_arg=None, races: BoxLayout = None):
        race_data = {box.children[2].text: float(box.children[1].text) for box in races.children}

        new_city = City(name=name, size=size_arg, race_populations=race_data)
        new_city.generate()
        city_data = f"""
        Name: {new_city.name}
        Population: {new_city.total_population} ({new_city.population})
        Area: {new_city.area} square miles
        """
        output_object.text = city_data


class RootWidget(BoxLayout):
    number_of_races = NumericProperty(0)

    def add_race_boxes(self):
        self.number_of_races += 1
        new_race_layout = BoxLayout(orientation="horizontal")
        new_race_layout.add_widget(TextInput())
        new_race_layout.add_widget(TextInput(input_filter="int", text="100"))
        new_race_layout.add_widget(RemoveRaceButton(text="X"))
        self.ids.race_layout.add_widget(new_race_layout)


class CityGenApp(App):
    city_sizes = ListProperty(city_types)

    def build(self):
        app = RootWidget()

        return app


if __name__ == '__main__':
    CityGenApp().run()
