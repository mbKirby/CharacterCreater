# CharacterCreator

## Project Overview
***
The purpose of this application is to allow the user to create a Dungeons & Dragons character and display the
character information on a charactersheet that is easily updated.

### Libraries & Frameworks

#### Frontend

- Vue.js
- Bootstrap
- Axios

#### Backend

- Django

## Features
***

### Must Haves

- Make Account
- Create Character
- Display Character Sheet

### Should Haves

- Allow user to edit character sheet
- Give detailed information on spells 

### Can Haves

- Allow user to prepare spells use spells and tell how many spell slots character has 
- Allow user to take notes for character 
- Incorporate api to generate random names
- Allow user to roll dice for ability checks 

### Won't Haves

- Allow user to create own original aspects of character such as homebrewed race or backgrounds 


## User Stories
***

### Creation
As a user, I want to be able to create a character with all information, save it, and access character sheet.

### Creation Tasks
- Create character object in database to populate character sheet.

### Charactrer Sheet
As a user, I want to be able to update my character sheet to display current information of character.

### Charactrer Sheet Tasks
- Allow user to update character sheet such as level, experience, equpiment, spell slots
- Allow user to select spells for each level spell slot 
- Allow user to click on spells for more information on each spell.

### Rolls
As a user be able to roll dice for skills checks and damage 

### Rolls Tasks
- Allow user to roll dice for each type of die 
- Allow user to roll checks by clicking on ability inside character sheet

## Data Model
***

### User

- Username (string)
- First Name (string)
- Last Name (string)

### PC
- User (Forign Key)
- Race (Select)
- SubRace // Draconic Ancestry (Select)
- Class (Select)
- SubClass (Select)
- Ability Scores (STR DEX CON INT WIS CHA) (Int)
- Feats (CheckboxSelectMultiple)
- Alignment (String)
- Background (Text)
- Proficiency (CheckboxSelectMultiple)
- Language / Tool Proficiencies (CheckboxSelectMultiple)
- Cantrips (CheckboxSelectMultiple)
- Equipment (Select)
- Name (String)
- Age (Int)
- Sex (Radio)
- Height (Int)
- Weight (Int)
- Hair, Eye, Skin Color (String)
- Backstory (Text)
- Armor Class (Int)
- Hit Points (Int)
- Speed(Int)
- Passive perception (Int)
- Darkvision (Int)

## Schedule
***

### Week 1

- create models
- create index and create character views
- create vue app and create users

### Week 2

- get character creation data from api
- link all vue data to django models
- add minimal css

### Week 3

- create edit character view
- create rolls functionality
- responsive design 

### Week 4

- refine css
- test and debug
