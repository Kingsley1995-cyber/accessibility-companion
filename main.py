from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class AccessibilityApp(App):
    def build(self):
        # Main Layout
        root = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title Header
        title_label = Label(
            text='[b]Accessibility Companion AI[/b]',
            markup=True,
            font_size=24,
            size_hint_y=None,
            height=60
        )
        root.add_widget(title_label)
        
        # Status / Output Screen Area
        self.output_label = Label(
            text='Select a mode below to start listening...',
            font_size=18,
            halign='center',
            valign='middle'
        )
        self.output_label.bind(size=self.output_label.setter('text_size'))
        
        # Scrollable container for text bubbles
        scroll = ScrollView(size_hint=(1, 0.6))
        scroll.add_widget(self.output_label)
        root.add_widget(scroll)
        
        # Mode Selection Buttons
        btn_conv = Button(text='1. Conversation Mode (Shona/Eng)', font_size=16, size_hint_y=None, height=50)
        btn_conv.bind(on_press=self.start_conversation)
        root.add_widget(btn_conv)
        
        btn_env = Button(text='2. Environmental Alerts (Baby/Cars)', font_size=16, size_hint_y=None, height=50)
        btn_env.bind(on_press=self.start_environmental)
        root.add_widget(btn_env)
        
        btn_music = Button(text='3. Music & Lyrics Mode', font_size=16, size_hint_y=None, height=50)
        btn_music.bind(on_press=self.start_music)
        root.add_widget(btn_music)
        
        return root

    def start_conversation(self, instance):
        self.output_label.text = "💬 [CONVERSATION MODE ACTIVE]\nListening for speech..."

    def start_environmental(self, instance):
        self.output_label.text = "🚨 [ENVIRONMENTAL MODE ACTIVE]\nScanning for sirens, cars, or baby crying..."

    def start_music(self, instance):
        self.output_label.text = "🎵 [MUSIC MODE ACTIVE]\nSyncing live lyrics..."

if __name__ == '__main__':
    AccessibilityApp().run()
