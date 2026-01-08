from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.utils import platform
from kivy.properties import ListProperty, StringProperty
from kivy.factory import Factory

if platform == 'android':
    from android.runnable import run_on_ui_thread
    from jnius import autoclass
    @run_on_ui_thread
    def set_landscape():
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        ActivityInfo = autoclass('android.content.pm.ActivityInfo')
        activity = PythonActivity.mActivity
        activity.setRequestedOrientation(ActivityInfo.SCREEN_ORIENTATION_LANDSCAPE)
    set_landscape()

class AnaEkran(Screen):
    kanallar = ListProperty([
        {'text': 'Şömine', 'logo': 'https://i.hizliresim.com/5unr56e.png', 'url': 'https://playlist.fasttvcdn.com/pl/mymfdhjrcpjziy5lmdkujw/somine-keyfi/playlist/3.m3u8'},
        {'text': 'TRT 1 HD', 'logo': 'https://i.ibb.co/5KpsVpx/TRT-1.png', 'url': 'https://tv-trt1.medya.trt.com.tr/master.m3u8'},
        {'text': 'TRT 2 HD', 'logo': 'https://i.ibb.co/hBv8Ck2/TRT-2.png', 'url': 'https://tv-trt2.medya.trt.com.tr/master.m3u8'},
        {'text': 'ATV HD', 'logo': 'https://i.imgur.com/Bhpp3ZI.png', 'url': 'https://rnttwmjcin.turknet.ercdn.net/lcpmvefbyo/atv/atv.m3u8'},
        {'text': 'STAR HD', 'logo': 'https://i.ibb.co/DCkPJ9N/Star-TV.png', 'url': 'https://dogus.daioncdn.net/startv/startv.m3u8?app=startv_web'},
        {'text': 'KANAL D HD', 'logo': 'https://i.ibb.co/CHd1VJg/Kanal-D.png', 'url': 'https://demiroren.daioncdn.net/kanald/kanald.m3u8?app=kanald_web'},
        {'text': 'SHOW HD', 'logo': 'https://i.ibb.co/hHxzpFy/Show-TV.png', 'url': 'https://ciner.daioncdn.net/showtv/showtv.m3u8?app=showtv_web'},
        {'text': 'NOW HD', 'logo': 'https://i.ibb.co/rZfkSXC/NOW-FOX-TV.png', 'url': 'https://uycyyuuzyh.turknet.ercdn.net/nphindgytw/nowtv/nowtv_720p.m3u8'},
    ])

class OynaticiEkran(Screen):
    video_url = StringProperty("")
    def on_enter(self, *args):
        self.ids.player.source = self.video_url
        self.ids.player.state = 'play'
    def on_leave(self, *args):
        self.ids.player.state = 'stop'

class TitanApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(AnaEkran(name='ana'))
        sm.add_widget(OynaticiEkran(name='oynat'))
        return sm
    def kanal_ac(self, url):
        self.root.get_screen('oynat').video_url = url
        self.root.current = 'oynat'

if __name__ == '__main__':
    TitanApp().run()
