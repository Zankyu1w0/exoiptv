[app]
title = TITAN TV
package.name = titan.iptv.player
package.domain = org.titan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.1.0

# ExoPlayer'ı sildik, yerine ffpyplayer ekledik (Standart Kivy Motoru)
requirements = python3,kivy==2.2.1,requests,ffpyplayer

orientation = landscape
android.permissions = INTERNET, WAKE_LOCK, ACCESS_NETWORK_STATE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Karmaşık ayarları sildik, sadeleştirdik
android.archs = arm64-v8a
android.skip_update = False
android.copy_libs = 1

log_level = 2
warn_on_root = 1

[buildozer]
bin_dir = ./bin
