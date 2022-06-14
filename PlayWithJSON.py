#!/usr/bin/env python3


# THIS TOOLS OR PROGRAM USING INDONESIA LANGUAGE.


def play_with_json(created_by = "Ruben Leonardo Sigalingging"):
	from os import system
	system("chmod 777 PlayWithJSON.py")
	system("clear")
	from sys import version_info, exit
	from time import time, sleep
	from pyfiglet import figlet_format
	tema = figlet_format("Json",font="slant")
	print(tema)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Selasa, 14 Juni 2022, Pukul 23:27 PM.")
	print("[!] Menggunakan: Bahasa Pemrogramman Python Versi 3.8.10")


	# Semangat!
	import urllib
	from urllib import request
	import json


	website_json = "https://api.github.com/users/RubenLeonardoSigalingging"
	# Kirim permintaan HTTP ke website json
	permintaan = request.urlopen(website_json)
	# Uraikan [Parsing] data dari website json
	uraikan_data_json = json.loads(permintaan.read())
	# Tampilkan hasilnya
	# print(uraikan_data_json)
	print("\n")
	print(f"[!] Login: {uraikan_data_json['login']}")
	print(f"[!] ID: {uraikan_data_json['id']}")
	print(f"[!] Node ID: {uraikan_data_json['node_id']}")
	print(f"[!] Avatar URL: {uraikan_data_json['avatar_url']}")
	print(f"[!] URL: {uraikan_data_json['url']}")
	print(f"[!] HTML URL: {uraikan_data_json['html_url']}")
	print(f"[!] Pengikut URL: {uraikan_data_json['followers_url']}")
	print(f"[!] Mengikuti URL: {uraikan_data_json['following_url']}")
	print(f"[!] Tipe: {uraikan_data_json['type']}")
	print(f"[!] Perusahaan: {uraikan_data_json['company']}")
	print(f"[!] Blog: {uraikan_data_json['blog']}")
	print(f"[!] Lokasi: {uraikan_data_json['location']}")
	print(f"[!] Email: {uraikan_data_json['email']}")
	print(f"[!] Bio: {uraikan_data_json['bio']}")
	print(f"[!] Dibuat Pada: {uraikan_data_json['created_at']}")
	print(f"[!] Diperbaharui Pada: {uraikan_data_json['updated_at']}")
play_with_json()