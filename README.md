# blytz #

## Install ##

First, install bacon.

### Install bacon ###

```
mkdir ~/test/bacon-bits
cd ~/test/bacon-bits && git clone https://github.com/jaderigby/bacon.git
scp ~/test/bacon-bits/bacon/.baconrc ~/test/bacon-bits
```

Add this line to your .bash_profile or .zshrc file:

```
source ~/Documents/bacon-bits/.baconrc
```

### Install blytz ###

```
cd ~/Documents/bacon-bits && git clone https://github.com/jadeblytz/blytz.git
bacon alias && bacon set
```

Now, you can run `blytz` and you should see the available blytz commands.

__You're all set!__

#### Install VSCode Segments Code Snippet: ####

Run `blytz snippets`, and follow instructions.