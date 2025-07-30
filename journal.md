# **Nap-Pad 🛌**
a 60% keyboard with rgb and a rotery encoder. Made for sleepers, by sleepers. It is portable, and very sleepy. Made with KiCAD and Fusion 360 and by Shayaan.is.sleep//The_Duck🦆 (me)

## Day 1 - june 11 10:00 pm
So the plan is to start the full size project today, and than ill try to finish this by the weekend. I did the HackPad so i do have some experience behind my belt but i never used materials or an oled screen so i'm a bit worried about that. What i plan to do is that ill have around 61 keys all connected into a grid and that into the pico. Ill also have a rotery encoder and sm rgb. Ill scrap the rgb if i run out of time.
- Started making the grid for the switches and started to plan out my pins for the pico
- finshed the keys but they are too big. Im looking at other submitions but my grid thign i have my keys ina re way to big. They like thake up more than half the sheet so i goot find a solutioon for that. But overall it was a nice productive 2 hours.

## Day 2 - June 15 5:00am
so i kinda procastanated too much and i didnt do it for like3 days. its rly erly inthe morning and i js finsihded the rgbs. I was going to do it so each swich will have tis own led, but to save cost, ill have 10-20 leds, around the board, and transperent key caps to make some sort of backlight. I looked as sm guides to understand how to wire them and yea. 
![Screenshot 2025-06-15 042730](https://github.com/user-attachments/assets/18774635-9bae-4fa1-a434-80ccb6124f04)

## Day 3 - June 20 3:00 pm
So Sry for the long break, i had to finish school. I still have 1 final left. So td im gonna work on the wireing the tags to the chipset for the schematic, and try to start on the wiring of the pcb. So i finshed the schematic, but i had to solve this weird prob. Firsrly, the led iw as using was rly bad, and was too big for my build (WBS1821) so i had to switch over to SK6812-MINI-E. There was no footprint for SK6812-MINI-E, so i had to make my own. This took quite some time, as i needed to orenent that corretly (Like DIN to pin 4, and DOUT to pin 2, VDD to pin 1 and VSS to pin 3). I have also finshed wireing everythig int he schamatic. So next steps is to do the pbc and CAD files, and i want to try to add a touch pad or add the full ammout of the switches ![image](https://github.com/user-attachments/assets/377487ba-7ccc-42ee-9681-0ea5b08beca9)

## Day 4 - July 28 2:00 pm
ok so tbh after fidnished the schematic i got rly confused with the footprints so i kinda rage quit and started to work on my other projects. until a few days ago i had the urge to finsh all my projects as i have been told that the ending date for sudmittions is july 31. I finshed the footprint issue after i asked a freind i have on Slack. He told be i needed to use Khali mx sw. So after donloading and fidning them, i finshed all that. I even got to place all my switchwes and diods and leds. <img width="1497" height="483" alt="image" src="https://github.com/user-attachments/assets/6c9bf94b-39f4-42ff-9212-38122fcb2164" />


## Day 5 - July 29 9:00 am
Ok so i want to be done with everything today so i started wires everything. My frind (same one that told me about the footprints) gave me adive on how and why should i set a ground pour. This is baciclya big bloack that will all be ground or 5Volts. This will hopefully lessen the ammount of wires. After i finahed all that, i thought i was done but it turns out the ground pour could be cut off and i had like 20 huger holes in my ground pour. I sped the next 3 hours connecting and moving wires so evenrythign gets connected. After soo long, at 10:30 pm, i have finshed the whole and even ran the DRC and everything went good! I even got the time to clean up my schematic.
<img width="1304" height="457" alt="image" src="https://github.com/user-attachments/assets/b43450dd-94b8-4d48-a97e-fca0b5fad4d4" />
<img width="1004" height="753" alt="image" src="https://github.com/user-attachments/assets/cec4439c-536b-452d-9153-60fdccc4bec1" />

