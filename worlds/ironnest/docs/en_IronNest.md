# IRON NEST: Heavy Turret Simulator

## Where is the options page?

The [player options page for this game](../player-options) contains all the options you need to configure and export a
config file.

## What is IRON NEST: Heavy Turret Simulator?

APQuest is an original game made entirely by NewSoupVi.  
It is a minimal 8bit-era inspired adventure game with grid-like movement.  
It is about 20 seconds long. However, the client can seamlessly switch between different slots,
so if you want to have 10 of them, that should work pretty well.

Crucially, this game is entirely integrated into the client sitting inside its .apworld.  
If you have the .apworld installed into your [Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases/latest)
install, you can play APQuest.

## Why does APQuest exist?

APQuest is implemented to be an example .apworld that can be used as a learning tool for new .apworld developers.  
Its [source code](https://github.com/NewSoupVi/Archipelago/tree/apquest/worlds/apquest)
contains countless comments explaining how each part of the World API works.
Also, as of the writing of this setup guide (2025-08-24), it is up to date with all the modern Archipelago APIs.

The secondary goal of APQuest is to be a semi-minimal generic world that is owned by Archipelago.  
This means it can be used for Archipelago's unit tests without fear of eventual removal.

Finally, APQuest was designed to be the first ever "game inside an .apworld",
where the entire game is coded in Python and Kivy and is playable from within its CommonClient-based Client.  
I'm not actually sure if it's the first, but I'm not aware of any others.

