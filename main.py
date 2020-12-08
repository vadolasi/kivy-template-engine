import jinja2
from kivy.app import App
from kivy.lang import Builder


class Main(App):
    def build(self):
        environment = jinja2.Environment(loader=jinja2.FileSystemLoader("interface"))
        main_interface = environment.get_template("main.kv")

        return Builder.load_string(main_interface.render())


if __name__ == "__main__":
    Main().run()
