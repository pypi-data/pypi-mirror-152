Changelog
=========

metalfinder 1.2.0 (20220527)
----------------------------

* change: rename --cache to --cache-dir
* fix: handle broken symlinks gracefully
* fix: don't crash when an artist is removed from the scanned directory
* add: implement METALFINDER_BIT_APPID environment variable
* add: make it possible to run using an externally generated artist list
* add: make it possible to run using "python3 -m metalfiner"


metalfinder 1.1.1 (20220519)
----------------------------

* fix: stop crashes for versions of requests earlier than 2.27


metalfinder 1.1.0 (20220519)
----------------------------

* add: implement event cache


metalfinder 1.0.2 (20220510)
----------------------------

* modified: general improvements to Bandsintown API logic
* fix: extract artists from MP3 files properly
* fix: update cache when files are removed


metalfinder 1.0.1 (20220509)
----------------------------

* fix: split artist names on '/', '+' and '&'


metalfinder 1.0.0 (20220507)
----------------------------

* Initial release
