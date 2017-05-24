# How to configure Arch Linux ARM to use ALSA

Install packages  

    # pacman -S alsa-firmware alsa-utils alsa-plugins alsa-lib

Enable the audio kernel module adding the line `dtparam=audio=on` to `/boot/config.txt`

Add the user to the **audio** group  

    # usermod -a -G audio *username*

Reboot

You can use `alsamixer` to change the volume and `# alsactl store` to save the current configuration.
