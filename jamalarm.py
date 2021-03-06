#!/usr/bin/python
# -*- coding: utf-8 -*-
# Jamalarm
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Jamalarm

import os, sys, time, random
import subprocess as sp
from time import sleep
from time import strftime as tm

info = """
Nama        : Jamalarm
Versi       : 3.3 (Update: 31 Maret 2020, 10:00 AM)
Tanggal     : 20 September 2019
Author      : Nedi Senja
Tujuan      : Membangunkan umat manusia
              menggunakan jam alarm
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: https://tinyurl.com/wel4alo

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;47;1;90m[          Jamalarm, My Github: @stepbystepexe           ]\033[0m"""

logo = """
\033[0;93m  ▀▀▀▀█ █▀▀▀█ █▀▀█▀▀█   \033[0;96m█▀▀▀█ █    █▀▀▀█ █▀▀▀▄ █▀▀█▀▀█
\033[0;93m      █ █▀▀▀█ █  █  █   \033[0;96m█▀▀▀█ █    █▀▀▀█ █▀▀▀▄ █  █  █
\033[0;93m  ▀▀▀▀  ▀   ▀ ▀     ▀   \033[0;96m▀   ▀ ▀▀▀▀ ▀   ▀ ▀   ▀ ▀     ▀
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def opt():
      try:
            while True:
                  waktu = tm('%I:%M:%S %p')
                  if waktu == alarm:
                        lup = True
                        print()
                        print()
                        print('\033[0m[\033[92;1m#\033[0m] ALARMNYA SUDAH BUNYI\033[0m')
                        print()
                        print('\033[0m[\033[101;77;1m PESAN \033[0m] '+messg)
                        print()
                        print('\033[0m[\033[91;1m-\033[0m] \033[4mTekan Ctrl + C untuk menyetop\033[0m\n')
                        sp.call('mpv .nada',shell=True,stdout=sp.DEVNULL,stderr=sp.STDOUT)
                        restart()
                        break
                  else:
                        print('\r\033[0mSekarang Jam\033[91;2m',waktu,end=''),;sys.stdout.flush();sleep(0.5)
                        set = str(waktu)
      except KeyboardInterrupt:
            print()
            print()
            print('\033[0m[\033[91;1m!\033[0m] \033[77;1mBerhenti\033[0m')
            print()
            sleep(1)
            restart()

os.system('clear')
os.system('reset')
sleep(1)
print()
print(logo)
print(example)
print()
print("\033[0m[\033[1;96;2m1\033[0m] \033[1;77mAktifkan Alarm Sekarang")
print()
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print()
option = input("\033[0m(\033[45;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
if option.strip() in '1 aktifkan'.split():
    if __name__=='__main__':
          write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
          sleep(1)
          os.system('clear')
          os.system('reset')
          sleep(1)
          print()
          print(logo)
          print(example)
          print()
          write("\033[0m[ \033[32mINFO \033[0m] \033[3mAlarm ini bisa bikin bootlop, dan berfungsi untuk")
          write("         Hek wipi, pesbuk dan hancurin satelit Nasa. hehe\n\n")
          h = input('\033[0m[\033[41;77;1m  Jam  \033[0m] ')
          m = input('\033[0m[\033[43;90;1m Menit \033[0m] ')
          s = input('\033[0m[\033[44;77;1m Detik \033[0m] ')
          print()
          o = input('\033[0mAktifkan \033[0m[\033[93;1mAM\033[0m] atau \033[0m[\033[95;1mPM\033[0m]: ').upper()
          print()
          messg = input('\033[0m[\033[96;1m+\033[0m] \033[77;1mMasukan pesan: \033[0m')
          alarm = h+':'+m+':'+s+' '+o
          write('\n\033[0m[\033[94;1m#\033[0m] \033[77;1mMengaktifkan Alarm ...\033[0m')
          sleep(3)
          os.system('clear')
          os.system('reset')
          time.sleep(1)
          print()
          print(logo)
          print(example)
          print()
          write("\033[0m[\033[32m INFO \033[0m] \033[3mDi wajibkan sholat ngaji terlebih dahulu, tersus")
          write("         Tidur kalo tidak alarm ini gx bakalan bunyi hehe.\033[0m\n")
          print()
          print('Alarm diatur jam: \033[96;2m'+h+':'+m+' '+o)
          opt()
elif option.strip() in '& 2 lisensi'.split():
    print()
    os.system('nano LICENSE')
    print()
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Alarm')
    print(info)
    sleep(1)
    print()
    input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print()
    os.system('git pull origin master')
    print()
    input('\033[0m[ \033[32mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- keluar 0'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print()
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print()
    sleep(1)
    restart()
