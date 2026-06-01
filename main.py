from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class SimpleApp(App):
    def build(self):
        # Создаем контейнер
        layout = BoxLayout(orientation='vertical', padding=20)
        
        # Добавляем надпись
        label = Label(
            text='Привет!',
            font_size='50sp',
            color=(1, 1, 1, 1)
        )
        layout.add_widget(label)
        
        return layout

if __name__ == '__main__':
    SimpleApp().run()
