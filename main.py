import flet as ft
import requests

def main(page: ft.Page):
    # Sayfa Ayarları
    page.title = "Deathless IPTV"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    
    # UI Elemanları (Tasarım Burası)
    lbl_title = ft.Text("DEATHLESS IPTV CHECKER", size=25, weight="bold", color="blue")
    txt_links = ft.TextField(label="M3U Linklerini Buraya Yapıştır", multiline=True, min_lines=5)
    lbl_result = ft.Text("Durum: Hazır", color="white")
    
    def start_check(e):
        if not txt_links.value:
            lbl_result.value = "Hata: Link girmediniz!"
            page.update()
            return
            
        links = txt_links.value.splitlines()
        hits = 0
        lbl_result.value = "Tarama başladı..."
        page.update()
        
        for link in links:
            link = link.strip()
            if link.startswith("http"):
                try:
                    # verify=False ve timeout ile çökme engellenir
                    r = requests.get(link, timeout=5, verify=False)
                    if r.status_code == 200:
                        hits += 1
                        # Dosyaya kaydet
                        with open("/storage/emulated/0/Download/Deathless_Hits.txt", "a") as f:
                            f.write(link + "\n")
                except:
                    continue
        
        lbl_result.value = f"İşlem Tamam: {hits} HIT bulundu ve indirilenlere kaydedildi."
        page.update()

    btn_check = ft.ElevatedButton("TARAMAYI BAŞLAT", on_click=start_check, width=250)

    # Sayfaya Ekleme
    page.add(
        ft.Column([
            lbl_title,
            ft.Divider(),
            txt_links,
            btn_check,
            lbl_result
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    # view=None Android'de en stabil açılış şeklidir
    ft.app(target=main)
