[app]
# (str) Title of your application
title = TITAN TV

# (str) Package name
package.name = titan.iptv.exoplayer

# (str) Package domain (needed for android packaging)
package.domain = org.titan

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
# pyjnius ve android paketleri ExoPlayer'ı tetiklemek için şarttır
requirements = python3,kivy,android,pyjnius,requests

# (str) Supported orientations (one of landscape, sensorLandscape, portrait or all)
orientation = landscape

# (list) Permissions
android.permissions = INTERNET, WAKE_LOCK, ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android NDK directory (if empty, it will be automatically downloaded)
android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded)
android.sdk_path =

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Android application architectures to build for
# Sadece arm64-v8a bırakmak build süresini yarı yarıya indirir ve hata payını azaltır
android.archs = arm64-v8a

# (bool) skips dist cleaning to speed up subsequent builds
android.skip_update = False

# (bool) If True, then skip trying to update the Android sdk
android.accept_sdk_license = True

# (str) Gradle dependencies (EXOPLAYER BURADA EKLENİYOR)
android.gradle_dependencies = 'com.google.android.exoplayer:exoplayer:2.18.1'

# (list) The Android architectures to build for.
android.copy_libs = 1

# (str) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) display warning if buildozer is run as root (0 = no, 1 = yes)
warn_on_root = 1

[buildozer]
# (str) Path to build artifacts
bin_dir = ./bin
