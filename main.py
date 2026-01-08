import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.recycleview import RecycleView
from kivy.clock import Clock
from urllib.parse import urlparse, parse_qs
import requests
import datetime
import threading

class IPTVChecker(App):
    def build(self):
        self.title = "Deathless IPTV Checker - Pro Edition"
        self.hits = []
        
        # Ana Layout
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Başlık ve İstatistikler
        stats_layout = BoxLayout(size_hint_y=None, height=100, spacing=5)
        self.lbl_total = Label(text="Toplam\n0", halign='center')
        self.lbl_hits = Label(text="Aktif (HIT)\n0", color=(0.13, 0.77, 0.36, 1), halign='center')
        self.lbl_bad = Label(text="Pasif\n0", color=(0.93, 0.26, 0.26, 1), halign='center')
        stats_layout.add_widget(self.lbl_total)
        stats_layout.add_widget(self.lbl_hits)
        stats_layout.add_widget(self.lbl_bad)
        root.add_widget(stats_layout)

        # Link Giriş Alanı
        self.txt_input = TextInput(
            hint_text="M3U Linklerini buraya yapıştırın...",
            multiline=True,
            background_color=(0.04, 0.06, 0.12, 1),
            foreground_color=(0.13, 0.77, 0.36, 1),
            size_hint_y=0.4
        )
        root.add_widget(self.txt_input)

        # Durum Çubuğu
        self.lbl_status = Label(text="Hazır", size_hint_y=None, height=30, font_size='12sp')
        root.add_widget(self.lbl_status)

        # Kontrol Butonları
        btn_layout = BoxLayout(size_hint_y=None, height=60, spacing=10)
        btn_start = Button(text="KONTROLÜ BAŞLAT", background_color=(0.38, 0.4, 0.94, 1))
        btn_start.bind(on_press=self.start_thread)
        
        btn_copy = Button(text="AKTİFLERİ KAYDET", background_color=(0.28, 0.33, 0.41, 1))
        btn_copy.bind(on_press=self.save_hits_to_file)
        
        btn_layout.add_widget(btn_start)
        btn_layout.add_widget(btn_copy)
        root.add_widget(btn_layout)

        return root

    def start_thread(self, instance):
        threading.Thread(target=self.process_links).start()

    def process_links(self):
        content = self.txt_input.text.strip()
        if not content:
            Clock.schedule_once(lambda dt: setattr(self.lbl_status, 'text', "Hata: Link girmediniz!"))
            return

        lines = [l.strip() for l in content.splitlines() if len(l) > 15]
        total = len(lines)
        hit_count = 0
        bad_count = 0
        
        Clock.schedule_once(lambda dt: setattr(self.lbl_total, 'text', f"Toplam\n{total}"))

        for link in lines:
            result = self.check_account(link)
            if result and result['status'] == "Active":
                hit_count += 1
                self.hits.append(link)
                msg = f"HIT! {result['host']} | Bitiş: {result['exp']}"
            else:
                bad_count += 1
                msg = "Pasif hesap atlandı."

            # Arayüzü güncelle
            Clock.schedule_once(lambda dt, h=hit_count, b=bad_count, m=msg: self.update_ui(h, b, m))

    def update_ui(self, h, b, m):
        self.lbl_hits.text = f"Aktif (HIT)\n{h}"
        self.lbl_bad.text = f"Pasif\n{b}"
        self.lbl_status.text = m

    def check_account(self, m3u):
        try:
            parsed = urlparse(m3u)
            qs = parse_qs(parsed.query)
            user = qs.get('username', [None])[0]
            passw = qs.get('password', [None])[0]

            if not user or not passw: return None

            # PHP kodundaki apiTarget mantığı
            api_url = f"{parsed.scheme}://{parsed.netloc}/player_api.php?username={user}&password={passw}"
            
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            r = requests.get(api_url, timeout=12, verify=False, headers=headers)
            data = r.json()

            if data.get('user_info') and data['user_info'].get('status').lower() == "active":
                info = data['user_info']
                exp_timestamp = info.get('exp_date')
                exp_date = datetime.datetime.fromtimestamp(int(exp_timestamp)).strftime('%d.%m.%Y') if exp_timestamp else "Sınırsız"
                
                return {
                    "status": "Active",
                    "host": parsed.hostname,
                    "exp": exp_date
                }
        except:
            pass
        return {"status": "Inactive"}

    def save_hits_to_file(self, instance):
        if not self.hits:
            self.lbl_status.text = "Kaydedilecek HIT bulunamadı!"
            return
        
        try:
            path = "/storage/emulated/0/Download/Deathless_Pro_Hits.txt"
            with open(path, "w", encoding="utf-8") as f:
                f.write("\n".join(self.hits))
            self.lbl_status.text = f"İndirilenlere kaydedildi: {len(self.hits)} adet"
        except Exception as e:
            self.lbl_status.text = f"Kaydetme hatası: {str(e)}"

if __name__ == "__main__":
    IPTVChecker().run()
                
