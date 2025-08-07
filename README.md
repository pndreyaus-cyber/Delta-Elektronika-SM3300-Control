## Documentation

Delta Elektronika has great documentation on the power supply. Here is the page, where you can find all of the manuals, code references, and firmware updates: <https://www.delta-elektronika.nl/products/sm3300-series#downloads>.

I used mainly these 3 files:

- “[Quick start manual SM3300 series](https://www.delta-elektronika.nl/sites/default/files/2025-04/SM3300_QuickStart_V202504_0.pdf)” in the “Manuals” section;
- “[Manual Ethernet and Sequencer programming SM3300 series](https://www.delta-elektronika.nl/sites/default/files/2025-06/SM3300_Parser_P0170_V202506.pdf)” in the “Manuals” section;
- “[Example Code and Software](https://www.delta-elektronika.nl/sites/default/files/2022-11/Example%20Code%20and%20Software_5.zip)” in the “Software” section.

## Connecting

I connected the power supply to my pc using an Ethernet cable. There is a LAN port at the back of the power supply.

To check if the connection is successful, I used the 2.1 section of the “Ethernet & Sequencer Programming SM3300” manual. To find the ip address of the power supply I used the LCD monitor. You can go to Menu -> Interfaces -> LAN -> Address .

## Programming

There are a lot of ways you can program the power supply. You can find all of them in the manual.

To switch between programming sources I used the LCD monitor of the power supply. Go to Menu -> Configuration -> Prg Source. There will be 2 settings: Vsettings and Isettings. So you can select programming source for current and voltage independently.

I tried 3 modes: “front”, “web”, “eth”.

### front

In this mode you program the power supply using knobs on its front panel.

For example, I set the output voltage to be 15V and the output current to be 5A.

So if the power supply is in the CV (constant voltage) mode, then the output voltage should be 15V and the output current may vary, but cannot be larger than 5A.

And if the power supply is in CC (constant current) mode, then the output current should be 5A and output voltage may vary, but cannot be larger than 15V.

To be honest I cannot figure out how to select CV or CC mode. The power supply chooses it automatically somehow. I could not find any button. Maybe you will.

### web

In this mode you program the power supply using web interface. I type in the ip address of the power supply in a web browser and it opens the web interface. I tried the same thing as in “front” mode: set output voltage to 15V and output current to 5A. It works the same as “front” mode. For more information about web interface you can go to the manual.

### eth

This mode lets you control the power supply using the TCP/IP protocol. To control the power supply you just send TCP/IP packets to it. Thus you can use any programming language or any tool, that is able to send and receive TCP/IP packets.

For example, to try out this “eth” mode I installed Hercules SETUP utility. It lets you send and receive TCP/IP packages in human-readable format. The interface is simple:

I entered the ip-address of the power supply in the ip-address field and the command in the empty field and clicked “SEND”. If it works, then you should get some answer.

As for programming via programming language. There is a python script in “[Example Code and Software](https://www.delta-elektronika.nl/sites/default/files/2022-11/Example%20Code%20and%20Software_5.zip)” archive. I just typed in the ip-address and ran the script.

Irina wanted to have a program, that has following requirements:

- Turn on the power supply with 15V and 5A in CV mode for 1 minute and then turn the power supply off;
- Every 10 seconds while the program is working it should write to some file current output voltage and output current.

I am not familiar with socket programming in Python, so i decided not to use the given script, but to find a Python library, which  hides work with sockets. The library: <https://github.com/keklikyusuf/DeltaElektronika>. It is intended to control the SM15K power supply and not the SM3300. But the command set to control these power supplies is the same for the most part. So the main functions, like setting and measuring voltage and current are the same.

## Problem
So this program kinda works. It correctly set output voltage and current. And correctly measures the output voltage and current. But the value of current is 0. I do not know why, because the electrical circuit is complete (resistor between + and - cords) and the current should be equal to voltage divided by resistance. The same problem occurs with "front" mode. 
