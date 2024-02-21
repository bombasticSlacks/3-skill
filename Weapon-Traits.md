---
layout: default
title: Weapon Traits
parent: Weapons
grand_parent: Equipment
nav_order: 2
---
# [Weapon](Weapons) Traits
{: .no_toc }

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Special Traits
These are weapon traits that can't be selected, either being [Default Traits](Designing-Weapons#Default%20Traits), or obtained some other way.
### Strength
This weapon adds [Strength](Strength) to [Damage Bonus](Weapons#Damage%20Bonus).

### Spirit
This weapon adds [Spirit](Game/Core/Spirit) to [Damage Bonus](Game/Core/Weapons#Damage%20Bonus).

### Size Matters
This weapon adds $size \times 2$ to [Damage Bonus](Weapons#Damage%20Bonus).

### Striking
This weapon [Attacks](Game/Core/Attacks) using the [Strike](Game/Core/Strength#Strike) skill.

### Targeted
This weapon [Attacks](Game/Core/Attacks) using the [Accuracy](Game/Core/Agility#Accuracy) skill.

### Mind Over Matter
This weapon [Attacks](Game/Core/Attacks) using the [Will](Game/Core/Spirit#Will) skill.

### Thrown
This weapon [Attacks](Game/Core/Attacks) using the [Athletics](Game/Core/Strength#Athletics) skill.

### One Handed
This weapon requires one free hand to wield effectively.

### Two Handed
This weapon requires two free hands to wield effectively.

### Exotic
This weapon requires additional training to be used effectively but has additional traits available.

### Advanced
This weapon requires sophisticated systems to work and can be dissrupted by external tools and processes.

### Basic
This weapon is made of simple materials, its [Damage Bonus](Weapons#Damage%20Bonus) is reduced by 1.

### Impossibly Large
This weapon cannot be wielded by an average-sized [Character](Terminology#Character).

### Capacity(X, Type)
The number and types of things that this item can be [Loaded](#Loading(X)) with. Usually written as Capacity (X, Type), which means it can be used X times, and is loaded with Y item.

> So a weapon described as having Capacity 12([Ammunition](Example-Gear#Ammunition)) would hold 12 generic ammo.

### Loading(X)
Some weapons and equipment will require a certain amount of time to be ready for use. This is the loading time. Loading time is specified as (X) where X is the number of rounds, or 0 for [Free Action](#Free%20Action).

If something can be loaded as a [Free Action](Terminology#Free%20Action), immediately using it puts the action at a (-1).

### Airborne
* This weapon only affects those that need to breathe.

### Handless
* This weapon doesn't require free hands to be used.

### Controlling
* This weapon allows you to perform any [Special-Combat-Actions](Game/Core/Special-Combat-Actions) that would normally require being within [Reach](Game/Core/Movement#Reach) using its [Range](Game/Core/Weapons#Range).

### Magical Attack
* This weapon performs [Magical-Attacks](Game/Core/Magical-Attacks).

### Devouring
*This otherworldly weapon feeds off those it destroys.*
* When this weapon causes [Defeated](Game/Core/Effects#Defeated) or kills an enemy, it refreshes all [Capacity](#Capacity(X,%20Type)) if it has any, otherwise the defeated [Characters](Game/Core/Terminology#Character) life force is stored within the weapon for other uses.

## 1 Cost Traits

### Balanced
+1 to defensive skill tests using this weapon.

### Black Powder
*Your weapon fires balls of lead propelled by incendiary powder.*
* Loses the [Strength](#Strength) trait.
* +6 [Damage Bonus](Weapons#Damage%20Bonus). 
* [Loading](#Loading(X))(2).
* Range of [Far](Movement#Far).
* [Capacity](#Capacity(X, Type)) 1([Ammunition](Example-Gear#Ammunition)).

### Bow
*This weapon fires arrows.* 
* Loses the [Strength](#Strength) trait.
* You can add [Strength](Strength) to damage *only* up to a maximum of the size of the weapon. 
* [Loading](#Loading(X))(0).
* Range of [Short](Movement#Short).
* [Capacity](#Capacity(X, Type)) 1([Ammunition](Example-Gear#Ammunition)).
* Gains [Salvageable](#Salvageable).

### Crossbow
*Your weapon fires bolts of metal.*
* Loses the [Strength](#Strength) trait.
* Add size to [Damage Bonus](Weapons#Damage%20Bonus) (in addition to [Size Matters](#Size%20Matters)).
* [Loading](#Loading(X))(1).
* Range of [Short](Movement#Short).
* [Capacity](#Capacity(X, Type)) 1([Ammunition](Example-Gear#Ammunition)).
* Gains [Salvageable](#Salvageable).

### Deadly Draw
This weapon is [Penetrating](#Penetrating) for your first attack in any combat.

### Disguised
This does not appear to be a weapon but has -1 [Damage Bonus](Weapons#Damage%20Bonus).

### Ensnaring
This weapon deals -2 damage, on [Non-mitigated Attack](Terminology#Non-mitigated%20Attack) it causes the enemy to be [Grappled](Special-Combat-Actions#grapple). You need to maintain hold of the ensnaring weapon to maintain the [Grapple](Special-Combat-Actions#grapple).

### Fast Reloading
If your weapon requires [Loading](#Loading(X)), it takes half the time. [Loading](#Loading(X)) that normally takes an action is instead a [Free Action](Terminology#Free%20Action).

### Hand and a Half
If this weapon is otherwise usable in one hand, the weapon counts as 1 size larger while wielded in two hands.

### Inscribed
This weapon counts as a Focus for [Will](Spirit#Will) skill tests.    

### Lethal
This weapon has 1 additional [Damage Bonus](Weapons#Damage%20Bonus).

### Momentum
Whenever you attack with this weapon and don’t strike anything (either miss or the attack is dodged) your next [Attack](Terminology#Attack) gains (+1), this stacks. 

### Multiple Damage Types
This weapon has an additional combat profile with the default traits and a different [Types of Damage](Injury#Types%20of%20Damage). When you attack, select one of the two types.       

### Multiple Shots
If your weapon has [Capacity](#Capacity(X, Type)) it has 3 additional.   

### On Line
* While wielded you suffer a (-1) to [Reactions](Terminology#Reaction). 
* You can make [Melee Attack](Terminology#Melee%20Attack) with this weapon at a range of [Close](Movement#Close), you cannot attack further, taking a [Distance Penalty](Attack-Bonuses#Distance%20Penalty).

### Reach
Performing [Melee Attack](Terminology#Melee%20Attack) doesn't put you [In Melee](Effects#In%20Melee). You contribute to [Outnumbered](Attack-Bonuses#Outnumbered) for anyone in [Reach](Movement#Reach).

### Salvageable
[Munitions](Comestibles#Munitions) spent by this weapon, if resulting in a [Mitigated Attack](Terminology#Mitigated%20Attack), the [Munitions](Comestibles#Munitions) are only destroyed if the [Skill Test](Terminology#Skill%20Test) results in [Doubles](Skills#Doubles).

### Shield(X)
* This weapon counts as additional [Armour](Armour) protecting you with X [Armour Integrity](Game/Core/Armour#Armour%20Integrity), that can only be used against [Ranged Attack](Terminology#Ranged%20Attack).
* This weapon provides a (+2) to [Avoid](Reacting#Avoid) skill tests when wielded.
### Shield
#TODOTemplate
* This weapon deals 1 [Impact](Injury#Impact) [Damage](Terminology#Damage).
* Provides [Shield(X)](#Shield(X)) where X is the the weapon size.


### Sling
*This weapon aids with throwing things long distances.*
* [Loading](#Loading(X))(0).
* [Capacity](#Capacity(X, Type)) 1([Throwables](Comestibles#Throwables)).
* Size 1-2 range of [Close](Movement#Close).
* Size 3+ range of [Short](Movement#Short).
* The result of attacks with this weapon are equivalent to what it is loaded with.
* If the loaded [Throwable](Comestibles#Throwables) adds [Strength](Strength) to [Damage Bonus](Weapons#Damage%20Bonus), it has the [Size Matters](#Size%20Matters) trait.

### Throwable
This weapon is balanced for throwing, you receive no penalties for throwing it.  

### Close Quarters
*Small enough to handle close encounters.*
* This weapon can be used [In Melee](Effects#In%20Melee) with no penalty.

### Shotgun
*Extra projectiles means more damage, or less, depends on how close you want to be.*
* This only effects weapons with a range greater than [Reach](Movement#Reach). 
* This weapon deals (+1) damage within [Reach](Movement#Reach)
* This weapon deals (-1) damage if outside the [Attack Range](Attacks#Attack%20Range).

### Launcher
*This weapon can assist in firing [Throwables](Comestibles#Throwables) using its inherent mechanical advantage*.
* Use [Accuracy](Agility#Accuracy) for [Attack](Terminology#Attack).
* Throwing can be done at a distance equal to this weapons [Range](Weapons#Range).

### Spraying
*This weapon can be rapid fired to cause additional harm.*
* If this weapon has [Capacity(X, Type)](#Capacity(X,%20Type)) you can expend up to 3 additional [Munitions](Comestibles#Munitions) and for each expended you receive a (+1) to [Attack](Terminology#Attack) and (+1) to [Damage Bonus](Weapons#Damage%20Bonus).


## 2 Cost Traits

### Folding
This weapon counts as two separate sizes. When stored, it is considered the smaller size. As an action, you may change which size it counts as, or at the end of any attack action you can change the size. Aside from folding the weapon can count as having a single separate [1 Cost Traits](#1%20Cost%20Traits) in each form.

### Overweight
This weapon has (-1) to [Actions](Terminology#Action) made with it and +3 [Damage Bonus](Weapons#Damage%20Bonus). 

### Penetrating
This weapon ignores [Resistance](Armour#Weakness%20and%20Resistance) of armour.

### Sundering
* If the [Opponent](Terminology#Opponent) of an attack has any remaining [Armour Integrity](Armour#Armour%20Integrity), this weapon deals (+1) [Damage](Terminology#Damage).

### Perfect
* (+1) to [Actions](Terminology#Action) made with this weapon.
* (+1) to [Damage Bonus](Weapons#Damage%20Bonus).

### Area
* This weapon affects everyone within [Reach](Movement#Reach) of the target (everyone gets a reaction).

### Explosion
* This weapon affects everyone in [Eye Line](Game/Core/Terminology#Eye%20Line) and [Close](Game/Core/Movement#Close) to the target (everyone gets a reaction).

### Massive Explosion
* This weapon affects everyone in [Eye Line](Game/Core/Terminology#Eye%20Line) and within a [Short](Game/Core/Movement#Short) distance from the target (everyone gets a reaction).

### Burning
* This weapon on a [Successful Attack](Terminology#Successful%20Attack) causes the [Opponent](Game/Core/Terminology#Opponent) to be [On Fire](Effects#On%20Fire).

### Stunning
* This weapon on a [Successful Attack](Game/Core/Terminology#Successful%20Attack) causes the [Opponent](Game/Core/Terminology#Opponent) to be [Stunned](Game/Core/Effects#Stunned).

### Disorienting
* This weapon on a [Successful Attack](Game/Core/Terminology#Successful%20Attack) causes the [Opponent](Game/Core/Terminology#Opponent) to be [Disoriented](Game/Core/Effects#Disoriented).

### Powerful Stunning
* This weapon on a [Successful Attack](Game/Core/Terminology#Successful%20Attack) causes the [Opponent](Game/Core/Terminology#Opponent) to be [Stunned](Game/Core/Effects#Stunned). 
* This weapon causes any targeted [Opponent](Game/Core/Terminology#Opponent) to be [Disoriented](Game/Core/Effects#Disoriented).

### Lingering
* This weapons attack results in a lingering effect. For a few minutes narratively, or the remainder of combat anyone remaining in the area at the end of their [Combat-Turn](Game/Core/Combat-Turn) suffers the attacks [Damage](Game/Core/Terminology#Damage) and [Effects](Game/Core/Effects) again. 

### Impaling
*This weapon embeds in enemies.*
* After a [Successful Attack](Game/Core/Terminology#Successful%20Attack) your enemy is [Stuck](Game/Core/Effects#Stuck).
* They must make a [Application](Game/Core/Intelligence#Application) [Fixed Difficulty](Game/Core/Skills#Fixed%20Difficulty)(0) test to remove this effect.

### Pulling
*This weapon pulls its target closer to you.*
* After a [Successful Attack](Game/Core/Terminology#Successful%20Attack) until the end of your next [Combat-Turn](Game/Core/Combat-Turn) you may as a [Free Action](Game/Core/Terminology#Free%20Action) move your [Opponent](Game/Core/Terminology#Opponent) within [Reach](Game/Core/Movement#Reach) of you and cause them to go [Prone](Game/Core/Effects#Prone).

### Precision
*This weapon is predominately used for accurate lethal attacks.*
* When performing a [Heavy Strike](Game/Core/Attacks#Heavy%20Strike) this attack does an additional [Damage](Game/Core/Terminology#Damage).

### Light Source
*A glowing source of light for any wielding it.*
* This weapon illuminates the user and everything [Close](Game/Core/Movement#Close).

### Eradicating
*This weapons attacks are so grim it leaves behind no evidence.*
* Anyone killed by this weapon or its injuries is eradicated, there remains no trace of them.

### Paired
*This weapon is actually a set of one-handed weapons designed to be used together.*
* This weapon can be used in only one hand, but you receive (-2) [Damage Bonus](Game/Core/Weapons#Damage%20Bonus) and a (-1) to [Attack](Game/Core/Terminology#Attack).

### Bound
*This weapon is connected to its user and is always on hand and ready for use.*
* The owner of this weapon may always draw it as though it were on their person, even if they are destroyed, or otherwise misplaced. They may still only exist in one place at any time, however.

### Silenced
*This weapon is perfectly quiet making no noise as it attacks.*
* This weapon makes no noise when used.