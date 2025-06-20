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
* [Damage](Game/Core/Terminology#Damage) (with [Types of Damage](Game/Core/Injury#Types%20of%20Damage)), [Effects](Game/Core/Effects), and other outcomes.
* Range (otherwise assume [Reach](Game/Core/Movement#Reach)).
* A description of what happens.

> 6 rending as you swing cleavers.
> 4 impact within close as you summon an undead and throw it.
> Everyone within earshot, suffer [Temporarily Deaf](Game/Core/Effects#Temporarily%20Deaf) as you scream.

### Traits
Notable things this character additionally has, examples can be found in [Character-Traits](Game/Core/Character-Traits).

### Traps
#TODO

## NPC Types
Easy to build, simplification of character design. Instead of using skills, these characters have specific actions and traps they can perform, as well as a smaller selection of traits. There are three tiers of simple NPC, mostly designed for direct party challenges: [Fodder](#Fodder), [Elites](#Elites), [Bosses](#Bosses).

### Fodder
Weak characters, they should have 1-2 actions they can perform, and no integrity. any amount of damage will defeat them.

### Elites
Characters similarly powerful to the player characters. They should have [Armour Integrity](Armour#Armour%20Integrity), be capable of [Reacting](Game/Core/Reacting), and have multiple [Action](Terminology#Action). If an elite enemy is [Wounded](Effects#Wounded) they are immediately [Defeated](Effects#Defeated).

### Bosses
#TODOCombat
Characters that could occupy multiple party members. They are capable of [Reacting](Game/Core/Reacting), and should be incapable of suffering [Overwhelming Odds](Game/Core/Combat#Overwhelming%20Odds). They should also have [Resistance(X)](Character-Actions#Resistance(X)) allowing them to survive potentially lethal strikes like a player character. 