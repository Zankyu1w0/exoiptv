import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
import requests

class IPTVChecker(App):
    def build(self):
        self.title = "Deathless IPTV Checker"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Başlık
        layout.add_widget(Label(text="DEATHLESS IPTV", font_size='24sp', size_hint_y=None, height=50))

        # Giriş Alanı
        self.txt_input = TextInput(hint_text="M3U Linklerini buraya yapıştırın...", multiline=True)
        layout.add_widget(self.txt_input)

        # Durum Etiketi
        self.lbl_status = Label(text="Durum: Hazır", size_hint_y=None, height=40)
        layout.add_widget(self.lbl_status)

        # Buton
        btn = Button(text="TARAMAYI BAŞLAT", size_hint_y=None, height=60, background_color=(0, 0, 1, 1))
        btn.bind(on_press=self.start_check)
        layout.add_widget(btn)

        return layout

    def start_check(self, instance):
        content = self.txt_input.text.strip()
        if not content:
            self.lbl_status.text = "Hata: Link girmediniz!"
            return

        links = content.splitlines()
        hits = 0
        self.lbl_status.text = "Taranıyor..."
        
        for link in links:
            link = link.strip()
            if link.startswith("http"):
                try:
                    # Sertifika hatasını görmezden gel (verify=False)
                    r = requests.get(link, timeout=5, verify=False)
                    if r.status_code == 200:
                        hits += 1
                        # Kayıt işlemi
                        with open("/storage/emulated/0/Download/Deathless_Hits.txt", "a") as f:
                            f.write(link + "\n")
                except:
                    continue
        
        self.lbl_status.text = f"Bitti! {hits} HIT indirilenlere kaydedildi."

if __name__ == "__main__":
    IPTVChecker().run()
