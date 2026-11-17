# MASTER STREAM — Fire TV

Personalized development build based on the GPL-2.0 licensed Jellyfin Android TV v0.20.0.

## Build

Go to **Actions → Build MASTER STREAM Fire TV APK → Run workflow**.
When the job succeeds, download the artifact **MASTER-STREAM-FIRETV-APK** and unzip it to obtain the test APK.

- Local Jellyfin server: `http://192.168.0.23:8097`
- Remote via Tailscale, if available on device: `http://100.95.155.37:8097`

The app name is customized to MASTER STREAM. The logo and internal app identity remain upstream Jellyfin. This is a **debug APK**, not a verified or production-signed release. Signing may conflict with existing Jellyfin installation; uninstalling the original app may be required and can erase its local preferences.

Build uses the upstream official sources; compatibility and completion must be confirmed by the GitHub Actions logs. Fire TV devices using Vega OS cannot install Android APKs.

Upstream: https://github.com/jellyfin/jellyfin-androidtv

License: GPL-2.0. Preserve copyright notices and provide corresponding source when distributing modified versions.

Build validation requested for Fire TV.

Retry Android SDK build with corrected workflow.
