import flet as ft
import requests
import asyncio
import os
import certifi

# Android için SSL sertifika yolunu ayarla (Çökme engelleyici)
os.environ["SSL_CERT_FILE"] = certifi.where()

async def main(page: ft.Page):
    page.title = "Deathless IPTV"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    
    lbl_info = ft.Text("Deathless IPTV Checker", size=25, weight="bold", color="blue")
    lbl_status = ft.Text("Hazır", color="white")
    txt_m3u = ft.TextField(label="M3U Linkleri Yapıştır", multiline=True, min_lines=5)
    
    def save_file(content):
        filename = "Deathless-Hits.txt"
        # Daha güvenli bir kayıt yolu
        path = "/storage/emulated/0/Download/" + filename
        try:
            with open(path, "a", encoding="utf-8") as f:
                f.write(content + "\n")
            return True
        except:
            return False

    async def start_check(e):
        if not txt_m3u.value:
            lbl_status.value = "Link yapıştırın!"
            await page.update_async()
            return
            
        lbl_status.value = "Taranıyor..."
        await page.update_async()
        
        lines = txt_m3u.value.splitlines()
        hits = 0
        
        for line in lines:
            line = line.strip()
            if "http" in line:
                try:
                    loop = asyncio.get_event_loop()
                    # verify=certifi.where() Android'de güvenli bağlantı sağlar
                    future = loop.run_in_executor(None, lambda: requests.get(line, timeout=5, verify=False))
                    response = await future
                    
                    if response.status_code == 200:
                        hits += 1
                        save_file(line)
                        lbl_status.value = f"HIT Bulundu: {hits}"
                        await page.update_async()
                except Exception as ex:
                    print(f"Hata: {ex}")
        
        lbl_status.value = f"Bitti! {hits} HIT kaydedildi."
        await page.update_async()

    btn_start = ft.ElevatedButton("BAŞLAT", on_click=start_check)
    
    await page.add_async(lbl_info, txt_m3u, btn_start, lbl_status)

if __name__ == "__main__":
    ft.app(target=main)
