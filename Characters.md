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

All characters that aren't a [Player Character](Game/Core/Terminology#Player%20Character), still need rules for the players to engage with. Non player characters are generally just a collection of actions, traits, traits and some default details.

## NPC Attributes
### Move
How far the enemy can move, one of [Distance Increments](Game/Core/Movement#Distance%20Increments).
### Integrity
How much harm an enemy can take before suffering injury or being defeated. Works like [Armour Integrity](Game/Core/Armour#Armour%20Integrity).
### Action Bonus
The dice value this character adds to [Action](Game/Core/Terminology#Action). GM may apply bonuses or negatives to this value as relevant.
### Hit Modifier
The penalty or bonus that [Attack](Game/Core/Terminology#Attack) against this character suffer. Usually (+3) to (-3)
### Avoid Modifier
The penalty or bonus that [Reacting](Game/Core/Reacting) against this character suffer. Usually (+1) to (-5)
### Weakness
Identical to [Weakness and Resistance](Game/Core/Armour#Weakness%20and%20Resistance) on armour, including [Critical Weakness](Game/Core/Armour#Critical%20Weakness).
### Resistance
Identical to [Weakness and Resistance](Game/Core/Armour#Weakness%20and%20Resistance) on armour.
### Actions
Clear actions the creature can do, should specify:
* Targets (Otherwise assume to be 1 [Character](Game/Core/Terminology#Character))
* Mention any costs like [Exerted](Game/Core/Effects#Exerted), or damaging self
* [Damage](Game/Core/Terminology#Damage) (with [Types of Damage](Game/Core/Injury#Types%20of%20Damage)), [Effects](Game/Core/Effects), and other outcomes.
* Range (otherwise assume [Reach](Game/Core/Movement#Reach)).
* A description of what happens.

> 6 rending as you swing cleavers.
> 4 impact within close as you summon an undead and throw it.
> Everyone within earshot, suffer [Temporarily Deaf](Game/Core/Effects#Temporarily%20Deaf) as you scream.

### Traits
Notable things this character additionally has, examples can be found in [Character-Traits](Game/Core/Character-Traits).

### Traps
Events that will occur when [Character](Game/Core/Terminology#Character) interact with this NPC, should specify:
* The event that triggers it, in the format "When X".
* What happens when the event occurs.

> When an enemy enters line of site, [Attack](Game/Core/Terminology#Attack) them.

Some examples are found in [Character-Traps](Game/Core/Character-Traps)

## NPC Types
Easy to build, simplification of character design. Instead of using skills, these characters have specific actions and traps they can perform, as well as a smaller selection of traits. There are three tiers of simple NPC, mostly designed for direct party challenges: [Fodder](#Fodder), [Elites](#Elites), [Bosses](#Bosses).

### Fodder
Weak characters, they should have: 
* 1-2 [Actions](#Actions) they can perform.
* Maybe some [Traits](#Traits)
* 0 [Integrity](#Integrity), any amount of damage will defeat them.

### Elites
Characters similarly powerful to the player characters with multiple interesting things they can do. They should have:
* Fully populated [NPC Attributes](#NPC%20Attributes).
* Multiple [Actions](#Actions).
* Any number of [Traits](#Traits).
* Potentially a few [Traps](#Traps).
* When Elites go to 0 [Integrity](#Integrity) they are defeated.

### Bosses
Characters that could occupy multiple party members with lots of things they can do. They should have:
* Fully populated [NPC Attributes](#NPC%20Attributes).
* Multiple [Actions](#Actions).
* Any number of [Traps](#Traps).
* Any number of [Traits](#Traits).
* The [Boss](Game/Core/Blocks/Boss) trait.

