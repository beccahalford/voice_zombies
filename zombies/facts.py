random_facts = [
    'Doctor Edward Richtofen joined the Illuminati on August 30th, 1925',
    'The Ray Gun was the first fictional gun to appear in the Call of Duty series',
    'Groph and Schuster develop the Wave Gun',
    'The 4 statues under pack-a-punch in origins are of the primiss crew',
    'The victus crew are cryogenically frozen in a secret lab under Alcatraz prison',
    'Group 9 3 5 was a scientific research group involved with the creation of most of the Wonder Weapon experiments',
    'Element 1 1 5 is exchanged between players and Doctor Monty as liquid divinium; its real name is Ununpentium',
    'In Call of Duty: Black Ops 3, all wall clocks found in zombies maps have stopped at 1:15',
    'The zombies eye colour corresponds to who is controlling them on the map',
    'Der Reese is a real location found in Poland that was used by Nazi scientists during the war'
]

map_facts = {
    'nacht': [],
    'shi_no_numa': [],
    'verruckt': [],
    'der_riese': [
        'Der Reese is a real location found in Poland that was used by Nazi scientists during the war'
    ],
    'five': [
        'A portrait of Richtofen can be found in the pack a punch room on 5',
        'The Winter\'s Howl can be found on a table on the third floor'
    ],
    'town': []
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
    # '': [],
}

map_perk_locations = {
    'verruckt': {
        'quick_revive': 'Can be located in the American\'s side of the starting room',
        'juggernog':    'is In the starting room next to the book shelf (German side)',
        'speed_cola':   'is In the room between the right balcony and the kitchen',
        'double_tap':   'can be found Next to the MP40 purchase on the German side',
        'mule_kick':    'can be found In the corner of the first cell blocks, next to the stairs',

    },
    'shi_no_numa': {
        'quick_revive': 'in black ops 3 will spawn in the starting room, to the left of the Sheiva. In Black Ops it randomly spawns in one of the huts',
        'juggernog': 'Randomly spawns in one of the huts',
        'speed_cola': 'Will spawn randomly in one of the four huts',
        'double_tap': 'Will randomly spawn in one of the four huts',
        'mule_kick': 'is available In the starting room, to the left of the Gewehr 43. Or via Der Wunderfizz machine, Perkaholic or On the House GobbleGum (Black Ops 3 Only)',
        'stamin-up': 'is available via Der Wunderfizz machine, Perkaholic or On the House GobbleGum (Black Ops 3 Only)',
        'deadshot': 'is available via Der Wunderfizz machine, Perkaholic or On the House GobbleGum (Black Ops 3 Only)',
        'widows_wine': 'is available via Der Wunderfizz machine, Perkaholic or On the House GobbleGum (Black Ops 3 Only)'
    },
    'der_riese': {
        'quick_revive': 'may be found To the right of the entrance of the room of the teleporter Z-C, in Dr Maxis\' office',
        'juggernog': 'is In a small hallway to the left of the staircase when going towards the Power Switch from the animal testing area',
        'speed_cola': 'is In the second courtyard, where the FG42 can be purchased',
        'double_tap': 'is On the second floor of the automobile garage near the bridge',
        'mule_kick': 'is Below the path leading towards the teleporter in the automobile garage, next to the box location'
    },
    'kino': {
        'quick_revive': 'can be found the starting room by the bar',
        'juggernog': 'is Located in the theater on the left side through the main doors, next to the Bowie Knife',
        'speed_cola': 'is In the foyer, close to the MP40/kuda wall buy',
        'double_tap': 'is located the southern part of the alleyway next to a barrier',
        'mule_kick': 'can be Found in the portrrate room, next to the door to the foyer',
        'stamin-up': 'is available via Der Wunderfizz machine, Perkaholic or On the House GobbleGum (Black Ops 3 Only)',
        'deadshot': 'is available via Der Wunderfizz machine, Perkaholic or On the House GobbleGum (Black Ops 3 Only)',
        'widows_wine': 'is available via Der Wunderfizz machine, Perkaholic or On the House GobbleGum (Black Ops 3 Only)'
    },
    'five': {
        'quick_revive': 'can be found in the starting room in the corridor.',
        'juggernog':    'is Downstairs in the war room, next to the door that leads to the Pack-a-Punch Machine room.',
        'speed_cola':   'is Next to the starting room, near the elevator.',
        'double_tap':   'will be found In the War Room next to the first elevator.',
        'mule_kick':    'located In the war room, across the Mystery Box location.'
    },
    'ascension': {
        'quick_revive': 'is in the starting room, on Centrifuge Floor 1.',
        'juggernog':    'Down the second staircase after buying the door that leads to the MPL/VMP(BO3) room. The '
                        'entrance is right next to the PM63/Vesper(BO3). Can be obtained from a Random Perk Bottle by '
                        'finishing a Space Monkey round without having them attack the Perk Machines.',
        'speed_cola':   'Near the Lunar Lander closest to the rocket and the Pack-a-Punch Machine; located near the top'
                        ' of the stairs where the M16/M8A7 and the Sickle are. Can also be obtained from a Random Perk '
                        'Bottle by finishing a Space Monkey round without having a perk machine attacked.',
        'double_tap':   'Available in black ops 3 only. Can only be obtained from the Random Perk Bottle, Der '
                        'Wunderfizz machine or the Perkaholic or On the House GobbleGum.',
        'mule_kick':    'Underneath the Speed Cola room, next to a barrier.',
        'stamin-up':    'Located past the gates to the left of the upper spawn door. It is in the back of the alleyway '
                        'past the door leading to the launch pad near the AK-74u and next to a spawn point of the '
                        'Mystery Box on the left.',
        'deadshot':     '',
        'widows_wine':  '',
        'phd_flopper':  'Black ops 1 only. In the room by Lunar Lander (closest to MP5K), with the grenades available '
                        'to purchase off the nearby wall. Can also be obtained from a Random Perk Bottle by finishing '
                        'a Space Monkey round without having any machines attacked.'
    },
    'call_of_the_dead': {
        'quick_revive': 'is found in the starting area, connected to the courtyard of the lighthouse.',
        'juggernog':    'is located In the hull of the ship, nearby one of the Pack-a-Punch\'s many spawn locations. '
                        'Can be obtained from a Random Perk Bottle by killing Romero whether or not the player has '
                        'finished the easter egg.',
        'speed_cola':   'is located Behind the lighthouse, at the end of the Ice Slide. Can also be obtained from a '
                        'Random Perk Bottle by killing Romero.',
        'double_tap':   'Located on the deck on the right after getting on the boat.',
        'mule_kick':    'At the back of the ship, right across the Mystery Box location.',
        'stamin-up':    'Behind the lighthouse and inside an abandoned house.',
        'deadshot':     '',
        'phd_flopper':  'In the abandoned second floor of the multi-story building that branches off of the lighthouse.'
                        ' Can also be obtained from a Random Perk Bottle by killing George A. Romero.'
    },
    'shangri_la': {
        'quick_revive': 'can be found in the starting area, along the middle wall.',
        'juggernog':    'is found Outside the temple next to a pillar by the MPL/VMP or on the bridge on the side of '
                        'the mud pit (Changes the position with Speed Cola). Can be obtained from a Random Perk Bottle '
                        'by killing a Zombie Monkey as it cycles the power-up.',
        'speed_cola':   'Near the wooden bridge and the Mud-Pit Maze, or near to the MPL (changes the spawn place with '
                        'Juggernog). Can also be obtained from a Random Perk Bottle by killing a Zombie Monkey as it '
                        'cycles the power-up it stole.',
        'double_tap':   'Will spawn randomly in the mines (changes spawn with Deadshot Daiquiri, PhD Flopper, and '
                        'Stamin-Up).',
        'mule_kick':    'In the waterfall area near the box location. Can also be obtained from the Perkaholic or On '
                        'the House GobbleGum.',
        'stamin-up':    'Will spawn randomly in one of the rooms underground (changes spawn with PhD Flopper, Double '
                        'Tap Root Beer and Deadshot Daiquiri).',
        'deadshot':     '',
        'widows_wine':  '',
        'phd_flopper':  'Black ops 1 only. Will spawn randomly in the mines. (changes spawn with Stamin-Up, Double '
                        'Tap and Deadshot Daiquiri). Can also be obtained from a Random Perk Bottle by killing a '
                        'zombie monkey as it cycles the power-up after it steals one.'
    },
    'moon': {
        'quick_revive': 'is located in the Receiving Area on the Moon.',
        'juggernog':    'may be found In Area 51 by the teleporter. Changes places with Speed Cola every time the '
                        'player returns to Area 51. It can also be obtained from a Random Perk Bottle by either '
                        'jumping multiple times on the bounce pads or spawning it with a QED. ',
        'speed_cola':   'may be found In Area 51. Changes places with Juggernog every time the player returns to Area '
                        '51. Can also be obtained from a Random Perk Bottle by either repeatedly jumping on the bounce '
                        'pads or spawning it with a QED.',
        'double_tap':   'Located on the first floor of the laboratories. Can also be obtained from the Perkaholic or '
                        'On the House GobbleGum. (Black ops 3)',
        'mule_kick':    'Outside, near the teleporter to Area 51, and where the AK-74u can be purchased. Can also be '
                        'obtained from the Perkaholic or On the House GobbleGum.',
        'stamin-up':    'In the second room of Tunnel 11, to the left of the Semtex.',
        'deadshot':     '',
        'widows_wine':  '',
        'phd_flopper':  'Black ops 1 only. Spawns on the far right side in the Bio-Dome near the Mystery Box spawn. '
                        'Can also be obtained from a Random Perk Bottle by either jumping multiple times on the bounce '
                        'pads or spawning one with a QED.'
    },
    'tranzit': {
        'quick_revive': 'can be found inside the starting area in the bus depot.',
        'juggernog':    'is found On the second floor near a corner in the building across from the bank in the town.',
        'speed_cola':   'is found in the North Highway Diner, against a wall near the door and MP5.',
        'double_tap':   'Located on the second floor of the barn in Farm.',
        'stamin-up':    'Inside the bar, right next to the Jet Gun crafting table.',
        'tombstone':    'Located inside the Power Station after the power is turned on or the door is opened by a '
                        'Turbine.'
    },
    'town': {
        'quick_revive': 'can be found on the 2nd floor of the bar in the corner near the Mystery Box spawn.',
        'juggernog':    'is found On the second floor near a corner in the building across from the bank in the town.',
        'speed_cola':   'is found Inside the city hall/bank, in front of some teller windows.',
        'double_tap':   'Next to the mystery box spawn across from the Semtex location.',
        'stamin-up':    'Outside the bar, across the road from the Bank and the M14.',
        'tombstone':    'Located on the street leading to the Mystery Box spawn and Double Tap Root Beer'
    },
    'nuketown': {
        'quick_revive': 'may be found in any perk spawn in the first room when playing solo. Spawns as an air drop '
                        'anywhere on the map during co-op mode.',
        'juggernog':    'Will spawn randomly with all other perks.',
        'speed_cola':   'Spawns randomly along with the other perks.',
        'double_tap':   'Spawns randomly along with the other perks every five rounds (starting on 1, with the '
                        'exception of solo, then 5, then 10) on stacks of crates.'
    },
    'die_rise': {
        'quick_revive': 'will always spawn in the elevator shaft closest to the purchasable door in the starting area, '
                        'near the M14 and Trample Steam work table.',
        'juggernog':    'Spawns randomly in one of the four elevator shafts in the building with the power switch. It '
                        'trades these positions between games with Double Tap Root Beer, Mule Kick and the Pack-a-Punch'
                        ' Machine.',
        'speed_cola':   'Spawns randomly in one of the two elevator shafts either down the hall from the initial spawn,'
                        ' or in the room two stories below where the Trample Steam is constructed, accessed by removing'
                        ' a couch obstacle. It shares these positions between games with Who\'s Who. Can also be '
                        'obtained from a Random Perk Bottle by finishing a Jumping Jack round with 100% accuracy.',
        'double_tap':   'Randomly spawns in one of the four elevator shafts in the building with the power switch. It '
                        'trades these positions between games with Juggernog, Mule Kick and the Pack-a-Punch Machine.',
        'mule_kick':    'Randomly spawns in one of the four elevator shafts in the building with the power switch. It '
                        'trades these positions between games with Juggernog, Double Tap Root Beer and the Pack-a-Punch'
                        ' Machine.',
        'phd_flopper':  'Unobtainable Easter Egg in the first elevator shaft from the spawn room.',
        'whos_who':     'is located in one of two elevator shafts once the power is turned on. Either the shaft down '
                        'the hall from the initial spawning area, or in another down below.',
    },
    'mob': {
        'quick_revive': 'is not available in mob of the dead, use afterlife mode instead',
        'juggernog':    'is Down near the Cerberus spawn and Gondola on the docks.',
        'speed_cola':   'is found In the back of the Warden\'s Office.',
        'double_tap':   'In the Citadel Tunnels, near the door that leads up to the Warden\'s Office area.',
        'mule_kick':    'Found on a boat across from the docks along with PhD Flopper as an unobtainable Easter egg.',
        'deadshot':     '',
        'phd_flopper':  'Found on a small boat along with Mule Kick near the dock area as an unobtainable Easter Egg.',
        'electric_cherry': ''
    },
    'buried': {
        'quick_revive': 'can be found on the left side of the very first room upon descending from the surface into '
                        'the underground town.',
        'juggernog':    'Behind some debris right next to the Giant\'s cell in a small alley, which needs to be '
                        'destroyed by him before players can access the machine.',
        'speed_cola':   'In the second floor of the courthouse. Can also be obtained from a Random Perk Bottle by '
                        'killing all the Ghosts after traversing through the mansion.',
        'double_tap':   'In the room next the entrance to the mansion, near the teddy bear location.',
        'mule_kick':    'Found on top of the Gunsmith shop, in front of a Mystery Box spawn.',
        'stamin-up':    'At the end of the hedge maze, at the stop of the stairs that lead to the Pack-a-Punch Machine.',
        'phd_flopper':  'Available as one of the Persistent Upgrades by taking a sufficient amount of fall damage '
                        'repeatedly (Note that it does not protect the player from over-cooked grenades or fall '
                        'damage). Not physically available nor is obtained from a Random Perk Bottle, which is '
                        'achieved by killing all the Ghosts after traversing trough the mansion.',
        'vulture_aid':  ''
    },
    'origins': {
        'quick_revive': 'is next to Generator 1 in the spawn room',
        'juggernog':    'is next to Generator 4 and a Der Wunderfizz spawn.',
        'speed_cola':   'is found in Across a small wooden platform near Generator 3 inside of the giant robot\'s '
                        'footprint. It is advised to be conscientious of the robots when purchasing this perk. Can '
                        'also be obtained at Der Wunderfizz.',
        'double_tap':   'Not physically present in the map. Can only be obtained through the Der Wunderfizz machine '
                        'and the Rituals of the Ancients.',
        'mule_kick':    'Found inside the excavation site, across from the staffs. Also purchasable by using the Der '
                        'Wunderfizz machine.',
        'stamin-up':    'Directly next to Generator 5 in a corner.',
        'deadshot':     '',
        'widows_wine':  '',
        'phd_flopper':  'Obtained via the Der Wunderfizz machine. Not physically available.',
        'electric_cherry': ''
    },
    'shadows': {
        'quick_revive': 'can be located in the starting area, to the right of the RK5.',
        'juggernog':    'Spawns randomly in one of the districts with Speed Cola and Double Tap Root Beer. A Red '
                        'bottles appear near the district\'s door which tell if the machine is in that district.',
        'speed_cola':   'Spawns randomly at one of the three perk spawn locations. it shares position with Juggernog '
                        'and Double Tap.',
        'double_tap':   'Randomly switches places with Speed Cola and Juggernog randomly through the districts. A '
                        'yellow bottle marks its location.',
        'mule_kick':    'In the Broken-down subway, near Widow\'s Wine.',
        'stamin-up':    'Outside of the spawn room, to the left of the Ice Cream store.',
        'widows_wine':  '',
    },
    'the_giant': {
        'quick_revive': 'is spawned randomly at any of the Perk-a-Cola machine locations, aside from the hidden machine',
        'juggernog':    'Spawns randomly at any of the Perk-a-Cola machine locations, aside from the hidden machine.',
        'speed_cola':   'Spawns randomly at any of the Perk-a-Cola machine locations, aside from the hidden machine.',
        'double_tap':   'Spawns randomly at any of the Perk-a-Cola machine locations, aside from the hidden machine.',
        'mule_kick':    'Spawns randomly at any of the Perk-a-Cola machine locations, aside from the hidden machine.',
        'stamin-up':    'In the left hallway, on small area covered by snow. It can only be received by throwing a '
                        'Monkey Bomb into each teleporter and teleporting them to the mainframe. Even if the steps are '
                        'followed, there\'s a chance of getting Deadshot Daiquiri instead of this Perk-a-Cola.',
        'deadshot':     '',
        'widows_wine':  '',
        'electric_cherry': ''
    },
    'der_eisendrache':  {
        'quick_revive': 'may be located in the starting room, near the RK5.',
        'juggernog':    'is located in the room that connects the starting room to the pyramid room, next to the KN-44.',
        'speed_cola':   'spawns Inside the church, to the left right beside the staircase heading to the pyramid room.',
        'double_tap':   'Located to the right of the castle entrance, right under the bridge looking out.',
        'mule_kick':    'Found in the corridor next to the big open hole below the room where the fire arrow can be '
                        'acquired.',
        'stamin-up':    'In the same room as the Power switch, to the right of the switch as the player enters the '
                        'room. Can also be obtained from the Der Wunderfizz machine or the Perkaholic or On the House '
                        'GobbleGum.',
        'deadshot':     '',
        'widows_wine':  '',
        'electric_cherry': ''
    },
    'zetsubou': {
        'quick_revive': 'is Located on the other side of the bunker door in co-op. Dropped via airplane at the start of'
                        ' round 2 in solo, opposite side of the Trials of the Ancients of by the main gate to Lab A.',
        'juggernog':    'Will spawn randomly via airplane on round 2 or round 6. Located on the other side of the '
                        'bunker door in solo.',
        'speed_cola':   'Switches between the entrance to Lab A, Next to the spider boss entrance and Lab B (Next to '
                        'the wall-buy for the ICR-1) with Double Tap.',
        'double_tap':   'Switches between Lab A (Next to the spider boss entrance) and Lab B (Next to the wall-buy for '
                        'the ICR-1) with Speed Cola.',
        'mule_kick':    'In the room before the underwater tunnels where the plant part for the KT-4 and the wheel '
                        'part for the Pack-a-Punch Machine can be found.',
        'stamin-up':    'Randomizes locations with the other perks except Mule Kick. Can also be obtained from the '
                        'Perkaholic or On the House GobbleGum.',
        'deadshot':     '',
        'widows_wine':  '',
        'electric_cherry': ''
    },
    'gorod_krovi': {
        'quick_revive': 'will be found In Belinski Square, to the left of the first door.',
        'juggernog':    'can be found On the second floor of the Department Store, to the right of the staircase '
                        'leading down towards the Operations Bunker.',
        'speed_cola':   'is In the balcony of the Supply Depot building.',
        'double_tap':   'In the first room of the Tank Factory, near its entrance.',
        'mule_kick':    'Near the entrance to the Operations Bunker coming from the Department Store.',
        'stamin-up':    'In the Infirmary. Can also be obtained from the Der Wunderfizz machine or the Perkaholic or '
                        'On the House GobbleGum.',
        'deadshot':     '',
        'widows_wine':  '',
        'electric_cherry': ''
    },
    'revelations': {
        'quick_revive': 'can be found In the starting room, directly in front of The House.',
        'juggernog':    'may be found On the second floor of the Nacht der Untoten section of the map, in front of the '
                        'stairs from the old starting room.',
        'speed_cola':   'is In Verruckt in the room straight forward from the corruption engine.',
        'double_tap':   'on the Origins Side of the map by the power generator to the right of the mystery box location',
        'mule_kick':    'Inside the cafeteria in Mob of the Dead, where Deadshot Daiquiri would be in Cell Block.',
        'stamin-up':    'On the Shangri-La island, where Quick Revive was originally found. Can also be obtained from '
                        'the Der Wunderfizz machine or the Perkaholic or On the House GobbleGum.',
        'deadshot':     '',
        'widows_wine':  '',
        'electric_cherry': ''
    },
    'spaceland': {},
    'redwoods': {},
    'shaolin': {},
    'radioactive': {},
    'beast': {},
    'prologue': {},
    'final_reich': {},
    'haus': {},
    'darkest_shore': {},
    'shadowed_throne': {}
}

gobblegum_data = {
    'always_done_swiftly': {
        'description': 'Walk faster when aiming, and Raise and lower your weapon to aim more quickly.'
                       'Activates Immediately, Lasts 3 Rounds',
        'type': 'classic'
    },
    'arms_grace': {
        'description': 'Respawn with the guns the player had when they bled out. '
                       'Activates Immediately, Lasts until next respawn',
        'type': 'classic'
    },
    'coagulant': {
        'description': 'Longer bleedout time. Activates Immediately, Lasts 20 minutes',
        'type': 'classic'
    },
    'plain_sight': {
        'description': 'All zombies ignore the player. Activated, 2x Activations, 10 seconds each',
        'type': 'classic'
    },
    'stock_option': {
        'description': 'Ammo is taken from the player\'s stockpile instead of their weapon\'s magazine. '
                       'This allows the player to "spam" single-round weapons such as the XM-53 or Apothicon Servant.'
                       'Activates Immediately, Last 2.5 minutes',
        'type': 'classic'
    },
    'impatient': {
        'description': 'Respawn near the end of the current round instead of at the start of the next round.'
                       'Activates Immediately, Lasts until bleed out',
        'type': 'classic'
    },
    'sword_flay': {
        'description': 'Melee attacks and any melee weapon will inflict 5x more damage on zombies.'
                       'Activates Immediately, Lasts 2.5 minutes',
        'type': 'classic'
    },
    'anywhere_but_here': {
        'description': 'Instantly teleport to a random location. A concussive blast knocks away any nearby zombies, '
                       'keeping the player safe. Activated, 2x Activations',
        'type': 'classic'
    },
    'danger_closest': {
        'description': 'Zero explosive damage, similar to PhD Flopper. Damage can still be taken by Insanity '
                       'Elementals. Activates Immediately, Lasts 3 full rounds',
        'type': 'classic'
    },
    'armamental': {
        'description': 'Switch weapons and recover from performing melee attacks faster. Reload and use items more '
                       'quickly. Similar to Fast Hands from Multiplayer but does not increase reload speed.'
                       'Activates Immediately, Lasts 3 full rounds',
        'type': 'classic'
    },
    'firing_cylinders': {
        'description': 'Can fire while sprinting. Similar to the Gung-Ho perk from Multiplayer. Activates Immediately, '
                       'Lasts 3 full rounds',
        'type': 'classic'
    },
    'arsenal_accelerator': {
        'description': ' Charge the player\'s special weapon faster. Affects the Apothicon Swords, the Annihilator, '
                       'the Ragnarok DG-4, the Skull of Nan-Sapwe, and the Gauntlet of Seigfried. Activates Immediately, '
                       'Lasts 10 minutes',
        'type': 'classic'
    },
    'lucky_crit': {
        'description': 'Improves your chances of activating an Alternate Ammo Type, like Turned, Dead Wire, etc.'
                       'Activates Immediately, Lasts 1 full round',
        'type': 'classic'
    },
    'now_you_see': {
        'description': 'All zombies will chase the player. Activated, 2x Activations, 10 seconds each',
        'type': 'classic'
    },
    'alchemical': {
        'description': 'Every 10 points earned is instead awarded 1 ammo in the stock of the current weapon. Affects '
                       'all weapons. Any points gained including points from power ups will give the player one round '
                       'in their reserve ammunition for every 10 points earned. Note that the points will not be awarded'
                       'if this GobbleGum is active. Activated, 2x Activations, 60 seconds each',
        'type': 'classic'
    },
    'projectile': {
        'description': 'Zombies you kill with grenades or other large projectiles vomit uncontrollably. Activates '
                       'Immediately, Lasts 5 full rounds',
        'type': 'whimsical'
    },
    'newtonian': {
        'description': 'Zombies killed fall straight up. Activates Immediately, Lasts 25 minutes',
        'type': 'whimsical'
    },
    'eye_candy': {
        'description': 'Overrides the colors you see. Creates color overlay that highlights zombies (and some non-zombie'
                       ' enemies) in a color that can be changed by reactivating. Colors include blue, green, yellow, '
                       'and red. Activating a 5th time will deactivate the Gum. Activated, 4 Activations',
        'type': 'whimsical'
    },
    'tone_death': {
        'description': 'A set of random silly zombie sounds and death sounds are played instead of the normal ones. '
                       'Activates Immediately, activates each tenth zombie kill',
        'type': 'whimsical'
    },
    'aftertaste': {
        'description': 'Keep all Perks after being revived. This will not keep the player\'s Quick Revive in solo.'
                       'Activates Immediately, Lasts 3 Rounds',
        'type': 'mega common'
    },
    'burned_out': {
        'description': 'The next time the player takes damage, nearby zombies burst into fire. Activates Immediately, '
                       'Lasts 2 Hits',
        'type': 'mega_common'
    },
    'nuclear_winter': {
        'description': 'Spawns a Nuke Power-Up. 2 activations',
        'type': 'mega_common'
    },
    'ephemeral_enhancement': {
        'description': 'Turns the weapon in the player\'s hands into the Pack-A-Punched version. Players should be '
                       'careful to remember that it only lasts for 60 seconds. 2 Activations, 60 Seconds Each',
        'type': 'mega_common'
    },
    'feeling_lucky': {
        'description': 'Spawns a random Power-Up in the map. 2 activations',
        'type': 'mega_common'
    },
    'immolation': {
        'description': 'Spawns a Fire Sale Power-Up. 3 activations',
        'type': 'mega_common'
    },
    'licensed_contractor': {
        'description': 'Spawns a Carpenter Power-Up. 3 activations',
        'type': 'mega_common'
    },
    'phoenix_up': {
        'description': 'Revives all teammates. Teammates keep all of their Perks. 1 activation',
        'type': 'mega_common'
    },
    'pop_shocks': {
        'description': 'Melee attacks trigger an electrostatic discharge, electrocuting nearby Zombies. Auto-Activates '
                       'when attacking Zombies, 5 Activations',
        'type': 'mega_common'
    },
    'respin_cycle': {
        'description': 'Re-spins the weapons in the Mystery Box after it has been activated. 2 activations',
        'type': 'mega_common'
    },
    'unquenchable': {
        'description': 'Can buy an extra Perk-a-Cola. The perk slot will be lost should the player go down. (Auto'
                       ' activates when the player has 4 perks.)',
        'type': 'mega_common'
    },
    'keeping_score': {
        'description': 'Spawns a Double Points Power-Up. 2 activations',
        'type': 'mega_common'
    },
    'fatal_contraption': {
        'description': 'Spawns a Death Machine Power-Up. 2 activations',
        'type': 'mega_common'
    },
    'crawl_space': {
        'description': 'All nearby zombies become crawlers. 5 activations',
        'type': 'mega_common'
    },
    'unbearable': {
        'description': 'Auto-activates when a teddy bear appears in the Mystery box. The Mystery box re-spins'
                       'automatically. The Mystery box will not move for several more uses.',
        'type': 'mega_common'
    },
    'disorderly_combat': {
        'description': 'Gives a random gun every 10 seconds. It should be noted that if the player uses this while '
                       'holding a Pack-a-Punched weapon, all subsequent weapons will be Pack-a-Punched as well. '
                       'Activates Immediately, Last for 5 minutes',
        'type': 'mega_common'
    },
    'slaughter_slide': {
        'description': 'Create 2 lethal explosions by sliding. Auto-activates when sliding, 6x Activations',
        'type': 'mega_common'
    },
    'mind_blown': {
        'description': 'Gib the heads of all the zombies you can see, killing them. 3 activations',
        'type': 'mega_common'
    },
    'board_games': {
        'description': 'Fixing one board at a barrier fixes all the boards at that barrier. You only get the points '
                       'from the first board repaired. Activates Immediately lasting 5 rounds',
        'type': 'mega_common'
    },
    'flavor_hexed': {
        'description': 'Selects a random Mega Gobblegum of any rarity that is not in the player\'s loadout and awards '
                       'it to the player. If the player doesn\'t bleed out or purchase another GobbleGum, then this '
                       'will repeat a second time once the first gum has been used. Activates Immediately',
        'type': 'mega_common'
    },
    'idle_eyes': {
        'description': 'All zombies ignore all players and stand idle.  3 30 seconds activations',
        'type': 'mega_common'
    },
    'board_death': {
        'description': 'Zombies within 15 feet of a repaired board are killed. Does not work for bosses. Activates '
                       'Immediately, Lasts 5 minutes',
        'type': 'mega_common'
    },
    'cache_back': {
        'description': 'Spawns a Max Ammo Power-Up. 1 Activation',
        'type': 'mega_rare'
    },
    'kill_joy': {
        'description': 'Spawns an Insta-Kill Power-Up. 2 activations',
        'type': 'mega_rare'
    },
    'on_the_house': {
        'description': 'Spawns a Random Perk Bottle Power Up. 1 activation',
        'type': 'mega_rare'
    },
    'wall_power': {
        'description': 'The next wall weapon purchased becomes Pack-a-Punched. (Activates Immediately, Lasts until the '
                       'player\'s next wall-buy gun purchase)',
        'type': 'mega_rare'
    },
    'undead_man_walking': {
        'description': 'Slow down all zombies to shambling speed. (Activates Immediately, Lasts 4 minutes)',
        'type': 'mega_rare'
    },
    'fear_headlights': {
        'description': 'Zombies seen by the player will not move. Players should remember this will not affect zombies '
                       'that are behind them. 1 Activation lasting 2 minutes',
        'type': 'mega_rare'
    },
    'temporal_gift': {
        'description': 'Power ups last longer (extra 30 seconds). Activated immediately, lasts one round',
        'type': 'mega_rare'
    },
    'crate_power': {
        'description': 'The next gun taken from the magic box comes Pack-a-Punched. (Auto-activates next time you take '
                       'a gun from the magic box)',
        'type': 'mega_rare'
    },
    'bullet_boost': {
        'description': 'Re-Pack your current Pack-a-Punched gun (if supported). 2 activations',
        'type': 'mega_rare'
    },
    'extra_credit': {
        'description': 'Spawns a Personal Points Power-Up worth 1,250 points (2500 points if Double Points is active).'
                       '4 Activations',
        'type': 'mega_rare'
    },
    'soda_fountain': {
        'description': 'Perk purchase limit is ignored. Every perk you buy, a random perk is awarded along with the '
                       'perk you bought. (Auto-activates when buying a perk, 5 Activations)',
        'type': 'mega_rare'
    },
    'killing_time': {
        'description': 'All zombies freeze in place for 20 seconds. If they are shot they will be annihilated when the '
                       'time is up. 1 activation',
        'type': 'mega_ultra_rare'
    },
    'perkaholic': {
        'description': 'Gives the player all Perk-a-Colas in the map. 1 activation',
        'type': 'mega_ultra_rare'
    },
    'head_drama': {
        'description': 'Any bullet which hits a zombie will damage its head. Activates Immediately, Lasts for the '
                       'Remainder of the Round',
        'type': 'mega_ultra_rare'
    },
    'secret_shopper': {
        'description': 'Any gun wall-buy can be used to buy ammo for any gun. (Note that you cannot buy ammo for '
                       'Wonder Weapons.) Activated Immediately, Lasts 10 minutes',
        'type': 'mega_ultra_rare'
    },
    'shopping_free': {
        'description': 'All purchases are free for one minute. Activates Immediately',
        'type': 'mega_ultra_rare'
    },
    'near_death': {
        'description': 'Revive, or be revived simply by being near other players. Revived players keep all their perks, '
                       'including Quick Revive. Activates Immediately, Lasts 3 full rounds',
        'type': 'mega_ultra_rare'
    },
    'profit_sharing': {
        'description': 'Points you earn are also recieved by nearby players and vice versa. Activates Immediately, '
                       'Lasts 10 minutes',
        'type': 'mega_ultra_rare'
    },
    'round_robbin': {
        'description': 'Ends the current round. All players gain 1600 points. This GobbleGum cannot be used in Area 51 '
                       '(Spawn area on Moon), it will simply fail to be used - this will not consume the GobbleGum.'
                       '1 activation',
        'type': 'mega_ultra_rare'
    },
    'self_medication': {
        'description': 'Auto revive yourself. Keep all your perks. This includes Quick Revive. Auto-activates by '
                       'getting a kill in last stand, 3x Activations',
        'type': 'mega_ultra_rare'
    },
    'power_vacuum': {
        'description': 'Power-Ups spawn more often. The drop chance is greatly increased, the normal cap of only 4 '
                       'drops per round is ignored. Activates Immediately, Lasts 4 rounds',
        'type': 'mega_ultra_rare'
    },
    'reign_drops': {
        'description': 'Spawns all the core power-ups at once (Nuke, Double Points, Fire Sale, Insta-Kill, Random Perk '
                       'Bottle, Max Ammo, Death Machine, Carpenter, Personal Points). 2 activations',
        'type': 'mega_ultra_rare'
    }
}