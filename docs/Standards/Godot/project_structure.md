# 2D Game Project Structure

For Godot, the approach that we are taking for project structure is to place assets as close as possible to the object that is using it. This makes the project much more scalable.

Below is an example that showcases this principle:

```txt
res://
├── entities/
│   ├── player_character/
│   │   ├── controller.gd
│   │   │   ├── sprites/
│   │   │   │   ├── idle/
│   │   │   │   │   └── idle.png
│   │   ├── sprite.png
│   │   └── walk_anim.png
│   ├── enemy_1/
│   │   ├── ai.gd
│   │   │   ├── sprites/
│   │   │   │   ├── idle/
│   │   │   │   │   └── idle.png
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
├── components/
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
| addons/           | A folder containing all imported 3rd-party files. The only exception to this is game assets                          |
| assets/           | A folder containing general assets for the game. DO NOT ADD INDIVIDUAL FILES, please create sub-folders as needed    |
| assets/background | A folder containing background art for the game                                                                      |
| assets/tiles      | A folder containing all tiles and tilesets used in the game                                                          |
| entities/         | A folder containing all characters and general objects within the game                                               |
| scenes/           | A folder containing all of the levels and the objects that make up that level                                        |
| sounds/           | A folder containing all of the sounds for the game. DO NOT ADD INDIVIDUAL FILES, please create sub-folders as needed |
| sounds/bgm        | A folder containing all background music for the game                                                                |
| sounds/sfx        | A folder containing all general sfx for the game                                                                     |
