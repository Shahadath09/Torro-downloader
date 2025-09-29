[app]
# (str) Title of your application
title = TORRO Downloader

# (str) Package name
package.name = torro

# (str) Package domain (needed for Android)
package.domain = org.torro

# (str) Application versioning. This is the fix.
version = 1.0

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let buildozer find them)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of modules to bundle with your app
requirements = python3, kivy==2.1.0, yt-dlp, certifi

# (str) Presplash background color (must be a hex value)
presplash.background_color = #121212

# (str) Presplash image
# presplash.filename = data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (one of landscape, portrait, all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen
fullscreen = 0

[buildozer]
# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# -----------------------------------------------------------------
# --- ANDROID SPECIFIC OPTIONS ------------------------------------
# -----------------------------------------------------------------
[android]
# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Android API to use
android.api = 31

# (int) Minimum API required
android.minapi = 21

# (int) Target API (same as android.api for new apps)
android.target_sdk = 31

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android build tools version
android.build_tools = 33.0.0

# (str) Python for android branch to use
p4a.branch = master
