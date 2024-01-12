# homeserver
Home Server for my parents

# Hardware specs
My home server is developed using HP Thin client t630.
It supports 2 M2 SATA disks (NOT NVME!), one of them uses FreeNAS, the other serves as storage disk.
This repo contains my roadpath to achieve multiple-task home server to support my parents in their everyday life.
Enjoy!

# FreeNAS setup
Visit FreeNAS or TrueNAS website to obtain image and use a program like Rufus to create bootable USB pendrive. In BIOS settings (F10 for HP) change boot order to start with USB bootable device. DO NOT create swap on small disks! After installation check the local IP address provided on the opening window (Ethernet cable required). On other PC login to the control panel. Strongly recommend to create password just after installation and to create secure SSH connection.
