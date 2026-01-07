[app]
title = TITAN TV
package.name = titan.iptv.exoplayer
package.domain = org.titan
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Gereksinimlere 'requests' ve 'urllib3' gibi ağ kütüphanelerini de ekledik
requirements = python3,kivy==2.2.1,android,pyjnius,requests,certifi

orientation = landscape

# TV ve Video için gerekli izinler eklendi
android.permissions = INTERNET, WAKE_LOCK, ACCESS_NETWORK_STATE, FOREGROUND_SERVICE

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# EXOPLAYER İÇİN KRİTİK AYARLAR
android.enable_androidx = True
android.gradle_dependencies = 'com.google.android.exoplayer:exoplayer:2.18.1'

# Build hızlandırma ve hata azaltma
android.archs = arm64-v8a
android.skip_update = False
android.copy_libs = 1

# Log seviyesi (Hata ayıklamak için 2 kalsın)
log_level = 2
warn_on_root = 1

[buildozer]
bin_dir = ./bin
