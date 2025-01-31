# Project Structure

The following is a general outline of the GDC project structure for a Unity `Assets` directory:

```txt
Assets/
├── Scenes/
│   └── ...
├── Plugins/
│   └── ...
├── Prefabs/
│   └── ...
├── Imported/
│   └── ...
├── Scripts/
│   └── Global/
│       └── ...
├── Audio/
│   ├── Music/
│   │   └── ...
│   ├── Effects/
│   │   └── ...
│   └── Mixers/
│       └── ...
└── Visual/
    ├── Textures/
    │   └── ...
    ├── Materials/
    │   └── ...
    ├── Meshes/
    │   └── ...
    └── Sprites/
        └── ...
```

| Folder                      | Explanation                                                                                                                                                                |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Assets                      | The root of the Unity project. Please try to avoid adding anything new here.                                                                                               |
| Assets / Scenes             | A folder containing all of the `.unity` scene files in the project.                                                                                                        |
| Assets / Plugins            | Any 3rd party (asset store or otherwise) editor plugins, or tools. For example, something like [Unity Hot Reload](https://hotreload.net/) would be imported here.          |
| Assets / Prefabs            | This folder stores prefabs used in the project, but should ideally contain many subfolders to compartmentalize them. Please do not just throw ***everything*** into this!  |
| Assets / Imported           | Sometimes, you want to import something from the asset store, but you're too lazy to categorize it; that goes here. Please try to avoid using this as much as possible :_) |
| Assets / Scripts            | The top level of the scripts directory, feel free to add any new sub-folders here, but try not to put scripts in this top level directory.                                 |
| Assets / Scripts / Global   | This is an example of a sub-folder for scripts, which could be used for any systems that affect the entire game (ex: a pause screen controller script).                    |
| Assets / Audio              | Do not put loose files into this, please create sub-directories as needed.                                                                                                 |
| Assets / Audio / Music      | Music!                                                                                                                                                                     |
| Assets / Audio / Effects    | Sound Effects!                                                                                                                                                             |
| Assets / Audio / Mixers     | Any audio mixers used throughout the game.                                                                                                                                 |
| Assets / Visual / Textures  | Textures! (Loose image files)                                                                                                                                              |
| Assets / Visual / Materials | Materials!                                                                                                                                                                 |
| Assets / Visual / Meshes    | 3D Meshes                                                                                                                                                                  |
| Assets / Visual / Sprites   | Any 2D sprites used in the game.                                                                                                                                           |

## But what if this isn't enough???

I'm glad you asked! Feel free to addend new categories or sub-categories as needed; so long as you aren't making a mess of things!

Please try to keep the structure as clean and readable as possible. Ideally, it should be intuitive to find any resource in the project. If things start getting confusing, it's probably time to re-evaluate your approach!
