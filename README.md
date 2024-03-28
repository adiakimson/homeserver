# homeserver
Home Server for my parents.

# Hardware specs
My home server is developed using HP Thin client t630.
It supports 2 M2 SATA disks (NOT NVME!), one of them uses FreeNAS, the other serves as storage disk.
This repo contains my roadpath to achieve multiple-task home server to support my parents in their everyday life.
You should also have at least 8GB of RAM. T630 supports DDR4.
Enjoy!

# NAS setup
Visit FreeNAS or TrueNAS website to obtain image and use a program like Rufus to create bootable USB pendrive. In BIOS settings (F10 for HP) change boot order to start with USB bootable device. DO NOT create swap on small disks! After installation check the local IP address provided on the opening window (Ethernet cable required). On other PC login to the control panel. Strongly recommend to create password just after installation and to create secure SSH connection.
This part is accomplished after configuring all the necessary stuff such as: user accounts, pool, databases, network location. When it is possible to obtain our storage as network location this step is finished successfully.
For FreeNAS 11 users creating plugins or jailing might be challenging. Should any issues occured, updating manually to the latest stable version is strongly recommended.

# Plugins/Extensions
FreeNAS/TrueNAS supports lots of ready-to-use plugins. All of them are listed here: https://www.ixsystems.com/documentation/freenas/11.2/plugins.html
Remember to choose your FreeNAS version in the docs. Via web panel you can download plugins and deploy them. Remember about jailing, otherwise further updates will erase your hard work.
Some I use:
- AdGuard - although might not working properly with: Gmail, Youtube, some other emails/popular platforms
- Nextcloud (as GUI for non-technical users)
- Virtual Machine

For easy installation you need to ensure your IPv4 configuration is proper. Check via ping in your shell if you can ping google.com. I recommend this setup:
- static IP
- for Nameserver 1/2 use Google DNS
- IPv4 default gateway 192.168.0.1

# Own plugin?
When a plugin and jailing is mastered, you may want to develop own plugin. Basic info again at: https://www.ixsystems.com/documentation/freenas/11.2/plugins.html#create-a-plugin
and: https://www.truenas.com/community/resources/create-an-unofficial-iocage-plugin.99/
Be a master of your own!
