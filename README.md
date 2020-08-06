# Beatswiper
converting custom beatsaber songs to custrom beatswiper songs

# What is this?

This repo simply hosts a script to convert beatmaps from betsaver to the betswiper format.

Beatswiper: https://apps.apple.com/us/app/beat-swiper/id1494755608

To inject them you need some kind of way to change the Beatswipers data, should be easier on android but ios I use a jailbrek to enable this. (ssh + sftp)

Then take an existing song in the apps song folder and plop the difficulty and the original song tn there.

Then open `SongsDataJson2.txt` and change totaltime and bpm.

It is possible to add a new song in the folder and edit the prefrences to reflect that but the app just errors out.


Now BeatSwiper is a unity game and i have tried to use uTinyRipper to exctact it and it does that fine except for the scripts. They're just not there.
If you find a way to extract them please message me in some way.
I have also included the .app folder from ios where the unity files reside.

Good luck!
