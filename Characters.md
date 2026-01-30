---
layout: default
title: Characters
grand_parent: 
nav_order: 0
has_children: true
parent: Running The Game
---
# Characters
{: .no_toc }

All characters that aren't a [[Terminology#Player Character]], still need rules for the players to engage with. Non player characters are generally just a collection of actions, traits, traits and some default details.

## NPC Attributes
### Move
How far the enemy can move, one of [[Movement#Distance Increments]].
### Integrity
How much harm an enemy can take before suffering injury or being defeated. Works like [[Armour#Armour Integrity]].
### Action Bonus
The dice value this character adds to [[Terminology#Action]]. GM may apply bonuses or negatives to this value as relevant.
### Melee Modifier
The penalty or bonus that [[Terminology#Attack]] against this character suffer within reach. Usually (+3) to (-3).
### Range Modifier
The penalty or bonus that [[Terminology#Attack]] against this character suffer outside of reach. Usually (+3) to (-3).
### Avoid Modifier
The penalty or bonus that [[Combat#Defending]] against this character suffer. Usually (+1) to (-5).
### Weakness
Identical to [[Armour#Weakness and Resistance]] on armour, including [[Armour#Critical Weakness]].
### Resistance
Identical to [[Armour#Weakness and Resistance]] on armour.
### Actions
Clear actions the creature can do, should specify:
* Targets (Otherwise assume to be 1 [[Terminology#Character]])
* Mention any costs like [[Exerted]], or damaging self
* [[Terminology#Damage]] (with [[Injury#Types of Damage]]), [[Effects]], and other outcomes.
* Range (otherwise assume [[Movement#Reach]]).
* A description of what happens.

> 6 rending as you swing cleavers.
> 4 impact within close as you summon an undead and throw it.
> Everyone within earshot, suffer [[Deafened]] as you scream.

### Traits
Notable things this character additionally has, examples can be found in [[Character-Traits]].

### Traps
Events that will occur when [[Terminology#Character]] interact with this NPC, should specify:
* The event that triggers it, in the format "When X".
* What happens when the event occurs.

> When an enemy enters line of site, [[Terminology#Attack]] them.

Some examples are found in [[Character-Traps]]

## NPC Types
Easy to build, simplification of character design. Instead of using skills, these characters have specific actions and traps they can perform, as well as a smaller selection of traits. There are three tiers of simple NPC, mostly designed for direct party challenges: [[#Fodder|Fodder]], [[#Elites|Elites]], [[#Bosses|Bosses]].

### Fodder
Weak characters, they should have: 
* 1-2 [[#Actions|Actions]] they can perform.
* Maybe some [[#Traits|Traits]]
* 0 [[#Integrity|Integrity]], any amount of damage will defeat them.

### Elites
Characters similarly powerful to the player characters with multiple interesting things they can do. They should have:
* Fully populated [[#NPC Attributes|NPC Attributes]].
* Multiple [[#Actions|Actions]].
* Any number of [[#Traits|Traits]].
* Potentially a few [[#Traps|Traps]].
* When Elites go to 0 [[#Integrity|Integrity]] they are defeated.

### Bosses
Characters that could occupy multiple party members with lots of things they can do. They should have:
* Fully populated [[#NPC Attributes|NPC Attributes]].
* Multiple [[#Actions|Actions]].
* Any number of [[#Traps|Traps]].
* Any number of [[#Traits|Traits]].
* The [[Boss]] trait.

