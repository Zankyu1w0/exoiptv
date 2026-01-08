[app]
title = Deathless IPTV
package.name = deathless.checker
package.domain = org.deathless
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0

# Flet sürümü 0.21.2 olarak sabitlendi
requirements = python3,flet==0.21.2,requests,urllib3,certifi,idna,charset-normalizer

orientation = portrait
permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.private_storage = True
android.accept_sdk_license = True
android.enable_androidx = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
