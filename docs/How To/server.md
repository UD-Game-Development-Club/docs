# Use The GDC Server

The GDC maintains a VM in the University of Dayton Cyber Range (Thanks to John Wolfe!) where we host our git LFS objects. This enables us to use GitHub collaboratively with a large amount of files, without needing to pay for the hosting. The downside to this, is that there is a little bit more setup needed for our repositories.

The following article will walk you through installing wireguard, and using it to clone the media library from the GDC server.

## Dependencies

Please install the following:

- [wiregaurd](https://www.wireguard.com/)
- [git](https://git-scm.com/downloads)
- [git lfs](https://git-lfs.com/)

You will need a command line version of git. This comes by default on many linux/unix systems, but if youre on windows I reccomend installing [git bash](https://git-scm.com/downloads) (or using git through the CLI, assuming it's in your PATH).

!!! warning
    Please note, GitHub desktop (and likely other git clients) will not work for this configuration, due to some TLS issues.

## Wiregaurd setup

Please reach out to an officer for a wiregaurd config file. Once obtained, you will be able to add a tunnel through the wiregaurd GUI.

After adding the wiregaurd tunnel, you can click on the tunnel and "activate" or "deactivate" it.

![Wiregaurd GUI](/docs/assets/wiregaurd.png)

In order to push or pull from the GDC server, you will _always_ need to be connected through wiregaurd first.

## GitHub PAT

To reach GitHub, you will need to generate a GitHub PAT (Personal Access Token) for authentication.

Visit <https://github.com/settings/tokens> (or Settings > Developer Settings > Tokens), and create a new PAT with the repo scope.

![GitHub PAT Generation](/docs/assets/PAT.png)

Scroll to the bottom, and click "Generate Token". You will then see a new token in your token list. Copy this new token, and save it somewhere (text file, password manager, etc), you will need it later!

## Cloning Example

Now, we'll show how to clone a GDC repo. Make sure you've followed all of the above steps and connected to wiregaurd!

Thankfully, it's super simple to go from base GitHub to GDC GitHub! Just replace `github.com` in any of your urls with `172.16.248.22:5000`. Additionally, switch the protocol from `https` to `http`.

The GDC media library is `https://github.com/UD-Game-Development-Club/library.git`, so it becomes `http://172.16.248.22:5000/UD-Game-Development-Club/library.git`.

In order to clone the media library, you can run the following git command (through the CLI):

```txt
git clone http://172.16.248.22:5000/UD-Game-Development-Club/library.git
```

After running, you will be asked for a username and password. The username is your GitHub username, and the password will be your PAT from earlier.

## GitHub CLI

For our configuration, you ***must*** use the CLI to interact with git, due to popular frontends like GitHub Desktop not liking our http/tls setup. This means that you must learn how to use the git CLI!

Thankfully, it's very simple. Have a look at some of the below resources:

- <https://git-scm.com/docs/git>
- <https://rogerdudler.github.io/git-guide/>
- <https://education.github.com/git-cheat-sheet-education.pdf>

## Additional Considerations

If you have downloaded the repo correctly, you will not have to make any additional changes in order to push.

If you recieve a message that says "Remote origin does not support the LFS locking API. Consider disabling it", you will need to run the following:

```txt
git config lfs.locksverify false
```
