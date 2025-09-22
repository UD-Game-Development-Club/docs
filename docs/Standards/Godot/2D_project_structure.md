# Project Structure

For Godot, the approach that we are taking for project structure is to place assets as close as possible to the object that is using it

Below is an example that showcases this principle:

```txt
res://
└── entities/
    ├── player_character/
    │   ├── movement.gd
    │   ├── sprite.png
    │   └── walk_anim.png
    ├── enemy_1/
    │   ├── ai.gd
    │   ├── sprite.png
    │   └── attack_anim.png
    └── character.gd
```

## Outline

The following is a general outline of the GDC project structure for a 2D Godot Project:

```txt
res://
├── addons/
│   └── ...
├── assets/
│   ├── backgrounds/
│   │   └── ...
│   └── tiles/
│       └── ...
├── entities/
│   └── ...
├── scenes/
│   └── ...
└── sounds/
    ├── bgm/
    │   └── ...
    └── sfx/
        └── ...
```

| Folder            | Explanation                                                                                                          |
| ----------------- | -------------------------------------------------------------------------------------------------------------------- |
| res://            | The root of the Godot project. Please try to avoid adding anything new here.                                         |
| addons/           | A folder containing all imported 3rd-party files. The only exception to this is game assets used for for characters  |
| assets/           | A folder containing general assets for the game. DO NOT ADD INDIVIDUAL FILES, please create sub-folders as needed    |
| assets/background | A folder containing background art for the game                                                                      |
| assets/tiles      | A folder containing all tiles and tilesets used in the game                                                          |
| entities/         | A folder containing all npc, enemies, and player characters within the game                                          |
| scenes/           | A folder containing all of the `.scn` files for the game                                                             |
| sounds/           | A folder containing all of the sounds for the game. DO NOT ADD INDIVIDUAL FILES, please create sub-folders as needed |
| sounds/bgm        | A folder containing all background music for the game                                                                |
| sounds/sfx        | A folder containing all general sfx for the game                                                                     |
