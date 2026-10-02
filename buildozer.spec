[app]
title = Accessibility Companion
package.name = accessibilitycompanion
package.domain = org.accessibility
source.dir = .
source.exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.min_api = 21
android.skip_update = False
android.accept_sdk_license = True

# (str) python-for-android branch to use
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
