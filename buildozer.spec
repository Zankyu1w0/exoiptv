[app]
title = TITAN TV
package.name = titan.iptv.exoplayer
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,android,pyjnius

# EXO PLAYER VE ANDROID AYARLARI
android.gradle_dependencies = 'com.google.android.exoplayer:exoplayer:2.18.1'
android.permissions = INTERNET, WAKE_LOCK
android.api = 31
android.minapi = 21
orientation = landscape
android.archs = arm64-v8a, armeabi-v7a
