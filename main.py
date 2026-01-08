import flet as ft
import requests
import os

def main(page: ft.Page):
    page.title = "Deathless IPTV"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    
    lbl_info = ft.Text("Deathless IPTV Checker", size=25, weight="bold", color="blue")
    lbl_status = ft.Text("Hazır", color="white")
    
    txt_m3u = ft.TextField(label="M3U Linkleri Yapıştır", multiline=True, min_lines=5)
    
    def save_file(content):
        filename = "Deathless-Hits.txt"
        path = f"/storage/emulated/0/Download/{filename}"
        try:
            with open(path, "a", encoding="utf-8") as f:
                f.write(content + "\n")
            return f"Kaydedildi: {path}"
        except:
            return "Kaydetme hatası (İzin yok)"

    def start_check(e):
        if not txt_m3u.value:
            lbl_status.value = "Lütfen link yapıştırın!"
            page.update()
            return
            
        lbl_status.value = "Taranıyor..."
        page.update()
        
        lines = txt_m3u.value.splitlines()
        hits = 0
        
        for line in lines:
            line = line.strip()
            if "http" in line:
                try:
                    # Basit bağlantı testi
                    response = requests.get(line, timeout=5)
                    if response.status_code == 200:
                        hits += 1
                        save_file(line)
                        lbl_status.value = f"HIT Bulundu: {hits}"
                        page.update()
                except:
                    pass
        
        if hits == 0:
            lbl_status.value = "Tarama bitti, çalışan yok."
        else:
            lbl_status.value = f"Bitti! Toplam {hits} çalışan link kaydedildi."
        page.update()

    btn_start = ft.ElevatedButton("TARAMAYI BAŞLAT", on_click=start_check)
    
    page.add(
        lbl_info,
        txt_m3u,
        btn_start,
        lbl_status
    )

if __name__ == "__main__":
    ft.app(target=main)
    
