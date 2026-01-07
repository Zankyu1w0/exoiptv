import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview import RecycleView
from kivy.properties import StringProperty
from jnius import autoclass, cast

# Android Native sınıfları
def play_in_exoplayer(url):
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Intent = autoclass('android.content.Intent')
    Uri = autoclass('android.net.Uri')
    
    intent = Intent(Intent.ACTION_VIEW)
    # ExoPlayer'ın m3u8'i tanıması için video/mp4 yerine video/* veya application/x-mpegURL kullanılır
    intent.setDataAndType(Uri.parse(url), "video/*")
    
    current_activity = cast('android.app.Activity', PythonActivity.mActivity)
    current_activity.startActivity(intent)

class ChannelItem(FocusBehavior, BoxLayout):
    text = StringProperty()
    logo = StringProperty()
    url = StringProperty()

    def on_press(self):
        play_in_exoplayer(self.url)

class TitanTV(App):
    def build(self):
        self.title = "TITAN TV"
        # Senin m3u8 listeni buraya bağladım
        channels = [
            {'text': 'Şömine', 'logo': 'https://i.hizliresim.com/5unr56e.png', 'url': 'https://playlist.fasttvcdn.com/pl/mymfdhjrcpjziy5lmdkujw/somine-keyfi/playlist/3.m3u8'},
            {'text': 'TRT 1 HD', 'logo': 'https://i.ibb.co/5KpsVpx/TRT-1.png', 'url': 'https://tv-trt1.medya.trt.com.tr/master.m3u8'},
            {'text': 'TRT 2 HD', 'logo': 'https://i.ibb.co/hBv8Ck2/TRT-2.png', 'url': 'https://tv-trt2.medya.trt.com.tr/master.m3u8'},
            {'text': 'ATV HD', 'logo': 'https://i.imgur.com/Bhpp3ZI.png', 'url': 'https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/atv/atv.m3u8'},
            {'text': 'STAR HD', 'logo': 'https://i.ibb.co/DCkPJ9N/Star-TV.png', 'url': 'https://dogus.daioncdn.net/startv/startv.m3u8?app=startv_web'},
            {'text': 'KANAL D HD', 'logo': 'https://i.ibb.co/CHd1VJg/Kanal-D.png', 'url': 'https://demiroren.daioncdn.net/kanald/kanald.m3u8?app=kanald_web'},
            {'text': 'SHOW HD', 'logo': 'https://i.ibb.co/hHxzpFy/Show-TV.png', 'url': 'https://ciner.daioncdn.net/showtv/showtv.m3u8?app=showtv_web'},
            {'text': 'NOW HD', 'logo': 'https://i.ibb.co/rZfkSXC/NOW-FOX-TV.png', 'url': 'https://uycyyuuzyh.turknet.ercdn.net/nphindgytw/nowtv/nowtv_720p.m3u8'},
        ]
        rv = self.root.ids.channel_list
        rv.data = channels
        return self.root

if __name__ == '__main__':
    TitanTV().run()
