import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import random
import os


class QuoteGeneratorApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.quotes_file = 'motivational_quotes.txt'
        self.favorites_file = 'favorite_quotes.txt'
        self.quotes = self.load_quotes()
        self.current_quote = None

    def load_quotes(self):
        """Load quotes from a text file, create if it doesn't exist."""
        if not os.path.exists(self.quotes_file):
            default_quotes = [
                "Believe you can and you're halfway there. - Theodore Roosevelt",
                "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
                "The only way to do great work is to love what you do. - Steve Jobs",
                "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
                "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
            ]
            with open(self.quotes_file, 'w') as f:
                for quote in default_quotes:
                    f.write(quote + '\n')

        with open(self.quotes_file, 'r') as f:
            return [line.strip() for line in f if line.strip()]

    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Quote display area with scrollview
        self.quote_label = Label(
            text="Click 'Generate Quote' to start!",
            text_size=(300, None),
            halign='center',
            valign='middle',
            size_hint_y=None,
            height=200
        )
        quote_scroll = ScrollView(size_hint=(1, 0.6))
        quote_scroll.add_widget(self.quote_label)
        layout.add_widget(quote_scroll)

        # Buttons section
        button_layout = BoxLayout(size_hint_y=0.2, spacing=10)

        generate_btn = Button(
            text='Generate Quote',
            on_press=self.generate_quote,
            background_color=(0.2, 0.6, 0.8, 1)
        )
        save_btn = Button(
            text='Save Favorite',
            on_press=self.save_favorite,
            background_color=(0.4, 0.8, 0.4, 1)
        )

        button_layout.add_widget(generate_btn)
        button_layout.add_widget(save_btn)

        layout.add_widget(button_layout)

        return layout

    def generate_quote(self, instance=None):
        """Generate and display a random quote."""
        if self.quotes:
            self.current_quote = random.choice(self.quotes)
            self.quote_label.text = self.current_quote
        else:
            self.quote_label.text = "No quotes available!"

    def save_favorite(self, instance=None):
        """Save the current quote to favorites file."""
        if self.current_quote:
            with open(self.favorites_file, 'a') as f:
                f.write(self.current_quote + '\n')
            # Optional: Add a visual feedback
            self.quote_label.text = f"Quote saved!\n{self.current_quote}"


def main():
    QuoteGeneratorApp().run()


if __name__ == '__main__':
    main()