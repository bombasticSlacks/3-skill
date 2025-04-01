---
layout: default
title: Effects
parent: How To Play
nav_order: 0
---
# Effects
{: .no_toc }
Effects are temporary things that can be applied to a character. They will effect your [Action](Terminology#Action) and the [Action](Terminology#Action) of others.

---
## Stunned
A stunned character cannot perform [Action](Terminology#Action) or [Movement](Game/Core/Movement).

### Removing
{: no_toc }
* After missing an [Action](Game/Core/Terminology#Action) during combat or when narratively appropriate.

---

## Unconscious
*You are out cold, you cannot respond to external stimuli of any kind.*
* You cannot perform [Action](Terminology#Action) or [Movement](Game/Core/Movement).

### Removing
{: no_toc }
* Someone must spend time waking you.
* Potentially at the end of the [Scene](Terminology#Scene).

---

## On Fire
*Your character or their clothing is currently burning.* 
* Whenever you act, you suffer 2 [Heat](Game/Core/Injury#Heat) damage, if this causes [Injury Damage](Game/Core/Injury#Injury%20Damage), you take an additional 2 [Heat](Game/Core/Injury#Heat) damage the next time this occurs.
* Whenever you would perform an [Action](Game/Core/Terminology#Action) make an [Volition](Spirit#Volition) [Fixed Difficulty](Skills#Fixed%20Difficulty)(0) skill test, if you fail you may only perform actions to remove this effect.


### Removing
{: .no_toc }
* To put yourself out is an [Application](Intelligence#Application) [Fixed Difficulty](Skills#Fixed%20Difficulty)(0). If you succeed, you are no longer on fire. 

---

## Prone
*You have been knocked to the ground.* 
* You suffer a -2 to all [Physique](Strength#Physique) skill tests.
* Cannot perform [Reaction](Terminology#Reaction).

### Removing
{: .no_toc }
perform a [Coordination](Agility#Coordination) [Fixed Difficulty(0)](Skills#Fixed%20Difficulty):
* If you succeed, you may stand as a [Free Action](Terminology#Free%20Action).
* If you fail, you will need to spend your [Action](Terminology#Action) to remove prone.

---

## Slowed
A slowed character can only move up to [Close](Movement#Close) on their next turn.

### Removing
{: .no_toc }
Will be removed with time.

---

## In Melee
*Your character moves around and connects weapons with combatants.*
* If a character in melee moves to something further than in [Reach](Movement#Reach), others may perform [Attack of Opportunity](Reacting#Attack%20of%20Opportunity) against them.
* Characters in melee suffer a negative to [Ranged Attack](Terminology#Ranged%20Attack) equal to the greatest [Threat](Attributes#Threat) among [Opponent](Terminology#Opponent) within [Reach](Movement#Reach) and also in melee.
* Characters in melee effect being [Outnumbered](Attack-Bonuses#Outnumbered).

### Removing
{: .no_toc }
There must be no other combatants in melee within [Reach](Movement#Reach).

---

## In Cover
*You are partially, or totally, obfuscated from your opponent.*
* A [Character](Terminology#Character) further than [Reach](Movement#Reach) from you suffers (-2) to all [attacks](Terminology#Attack) targeting you.
* You may suffer a (-4) on all [Action](Terminology#Action) to make it impossible for people outside [Reach](Movement#Reach) to target you with [Attacks](Attacks) until your next [Action](Game/Core/Terminology#Action).

### Removing
{: .no_toc }
* You cannot be in cover if you are [In Melee](#In%20Melee).
* If you move away from whatever is providing you with cover.

---

## Defeated
*You have collapsed, either dead or incapacitated, unable to aid your allies further. This might consist of having to put pressure on wounds, being in shock, actually being unconscious, or any number of narrative appropriate scenarios.*
* Your character can no longer perform [Actions](Terminology#Action) or [Movement](Game/Core/Movement).
* Your character has a [Threat](Attributes#Threat) of 0. 

### Removing
{: .no_toc }
* Anyone can do a basic stabilization of a defeated [Character](Terminology#Character). This is a very basic test to make sure they are no longer bleeding, their burns have been covered, etc. This is a [Application](Intelligence#Application) [Fixed Difficulty](Skills#Fixed%20Difficulty)(0). No matter the result of the skill test, the person is no longer at risk of immediately dying, but if you fail they get an additional -1 to their [Long Term Injury](#Long%20Term%20Injury) penalty. 

---
## Wounded
*Your character has suffered a meaningful injury, there is only so much longer they can keep fighting.*
* After you perform an [Action](Game/Core/Terminology#Action), you become [Defeated](Game/Core/Effects#Defeated). (This can be resisted with [Endurance](Game/Core/Strength#Endurance)).

### Removing
{: .no_toc }
* Can be removed with [Gear](Gear).
* Removed if you become [Defeated](#Defeated).
* Removed at the end of [Combat](Game/Core/Combat).

---

## Long Term Injury
*Your character has suffered a meaningful injury. The discomfort causes them difficulty when performing actions.*
* If you are wounded, after combat you will take a penalty to all [Action](Terminology#Action) equal to the highest amount of [Injury](Game/Core/Injury).

### Removing
{: .no_toc }
* Removed with adequate time or healing.
* Removed with [Gear](Gear).

---

## Disoriented
*You have difficulty focusing and moving, everything feels like it is under water.*
* (-2) to all [Actions](Terminology#Action).

### Removing
{: .no_toc }
* Goes away on its own at the end of the [Scene](Terminology#Scene).
* Can perform [Endurance](Strength#Endurance) [Fixed Difficulty](Skills#Fixed%20Difficulty)(0) as an [Action](Terminology#Action) to remove.

---
## Restrained
*Something is keeping you from acting or moving.*
* You cannot perform [Action](Terminology#Action) or [Movement](Game/Core/Movement).

### Removing
{: no_toc }
* Whatever is restraining you must be removed.


---
## Stuck
*Something is keeping you from moving.*
* You cannot do any [Movement](Game/Core/Movement).

### Removing
{: no_toc }
* Whatever has made you stuck, you must be separated from.


---

## Temporarily Blind
*You can't see.*
* You cannot do anything relying on your sight.
* You cannot attack outside of [Reach](Game/Core/Movement#Reach).
* Attacking is at a (-3).

### Removing
{: no_toc }
* Last until the end of the [Scene](Game/Core/Terminology#Scene). 

---

## Temporarily Deaf
*You can't hear.*
* You cannot do anything relying on your ears.
* You count as [Disoriented](Game/Core/Effects#Disoriented).

### Removing
{: no_toc }
* Last until the end of the [Scene](Game/Core/Terminology#Scene).

---

## Fearless
*You cannot become afraid no matter the horrors you see.*
* You cannot gain [Stress](Game/Stress).
* You automatically pass all [Volition](Game/Core/Spirit#Volition) [Skill Test](Game/Core/Terminology#Skill%20Test) related to fear and panic.
### Removing
{: no_toc }
* Last until the end of the [Scene](Game/Core/Terminology#Scene).

---

## Exerted
*You have been pushed to the limit and will need a minute to regain full strength.*
* You cannot perform any [Action](Game/Core/Terminology#Action) that would cause you to become exerted.
### Removing
{: no_toc }
* Removed at the end of your next [Action](Game/Core/Terminology#Action).

---

## Brittle
*Materials protecting you have stopped behaving as they are supposed to.*
* Your [Resistance](Game/Core/Armour#Weakness%20and%20Resistance) no longer reduces incoming damage.
### Removing
{: no_toc }
* Removed at the end of the scene.
* Removed with repairs or other intervention.