=========
bulk_meta
=========
-----------------------------------------------
A bulk metadata downloader for private trackers
-----------------------------------------------


This is a long-lived python program that downloads all the metadata
(`*.torrent` files) on a private tracker. It does this by adding magnet links
to a bittorrent client, waiting for peers to send us metadata, then storing
that metadata. No actual data is downloaded. The magnet link approach minimizes
load on the tracker site.


For any torrents which are active for too long without getting
metadata from peers, the downloader falls back to downloading the metadata from
http.


Currently, btn is the only supported tracker, and deluge is the only supported
torrent client. It requires a specialized plugin to work.


*NOTE*: This relies on behavior of some peers that is probably bad and
insecure; peers shouldn't send metadata for torrents marked private. I wrote
this in order to construct a proof of concept of yatfs on btn, and only then
because it's so useful to have the file structure of a torrent without needing
to download it.
