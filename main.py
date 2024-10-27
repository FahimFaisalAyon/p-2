from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout

# KV content as a string
kv = '''
<WidgetsExample>:
    cols: 1
    Button:
        text: root.text
        on_press: root.click()
        font_name: "fonts/Cute.ttf"
        font_size: "80dp"
        color: 1, 1, 1, 1
        background_normal: "images/red.jpg"
'''

# Load the KV design from the string
Builder.load_string(kv)

class WidgetsExample(GridLayout):
    text = StringProperty("Click here!")

    def click(self):
        self.text = "I love you"

class TheLabApp(App):
    def build(self):
        return WidgetsExample()

TheLabApp().run()














