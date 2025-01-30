# Unity Project Structure Standards

This document will go over the structure of your assets folder inside your unity project.

### Simpliefied Version:
- Plugins
- Prefabs
- Resources
  - Imported
  - Materials
    - Skybox
    - Sprites
  - Models
  - Particles
  - Shaders
  - Audio
    - AudioMixers
    - Music
    - SoundEffects
- Scenes
- Scripts
  - Enemy
  - Enviroment
  - Interfaces
  - Managers
  - Player
- Settings


### Detailed Version:
- Plugins
  > Any plugins or extra utilities you add to the unity project go here.
- Prefabs
  > Prefabs that need to be used frequently, are summoned a lot of times, or are very important should be stored here. (Ex: SoundFXManager, GamePlayManager, Bullet, Enemy)
- Resources
  - Imported
    > Any asset bundles you import as a group go in this folder. If you are importing a single asset, store it in a more appropriate Resources folder
  - Materials
    > Where you store any non-specific mat files. If you have a mataterial to only be used on one object, like a person, then store it with the model.
    - Skybox
      > Skybox materials separated to here for easy access.
    - Sprites
      > Any 2D images or sprites get stored here.
  - Models
    > All models go here, each model group gets a separate folder with all its neccesary files. For example, a car would go in one folder and then any material that belong with it would join it. If multiple models can use the same material, then you can put multiple models in 1 folder. For example, a model for a barrel and a box could possibly use the same material.
  - Particles
    > Any particles made with the unity particle system get stored here.
  - Shaders
    > All shaders get stored here, if a shader needs multiple files then create a folder for it.
  - Audio
    - AudioMixers
      > Audio mixers and managers go here.
    - Music
      > All Music or jingles goes here.
    - SoundEffects
      > Separate sound effects based on use. For example, a "FordF150SoundEffects" folder would have all sounds a Ford F150 would make. A "RyuSoundEffects" folder would have all sounds that the fighting characeter Ryu would make.
- Scenes
  > Any Scenes needed for the game go here.
- Scripts
  > Scripts folders may change depending on your game, you may not need an enemy folder, and you may need other scripts such as vehicle folder, or an item folder.
  - Enemy
    > Scripts for the enemies of the game, could be enemie AI for example.
  - Enviroment
    > Scripts for Enviromental objects
  - Interfaces
    > Scripts for interfaces which could include things like your UI
  - Managers
    > Scripts for manager objects such as a GamePlayManager or SoundFXManager
  - Player
    > Scripts directly involving the player.
- Settings
  > Stores unity settings and such, be careful about storing anything in this folder, leave it mostly for Unity to autopopulate.
