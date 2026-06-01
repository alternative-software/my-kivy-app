[app]
title = My Simple App
package.name = simpleapp
package.domain = org.test
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
# Эти параметры оставьте пустыми — GitHub сам их подставит
android.api = 33
android.minapi = 21
android.ndk = 25b
android.gradle_dependencies =
