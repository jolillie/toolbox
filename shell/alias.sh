# ALIASES
alias cd..="cd .."
alias gc="git clone"
alias ghc="gh repo clone"
alias open_iterm="open -a Iterm ."
alias get-pub-key="cat ~/.ssh/id_ed25519.pub | tee >(pbcopy)"
alias get-rsa-pub-key="cat ~/.ssh/id_rsa.pub | tee >(pbcopy)"
alias git-cleanup="git-cleanup.sh"
alias cd-work="cd ~/code/__work"
alias cat='bat --paging=never'
alias tf="terraform"
alias p3="python3"

# FUNCTIONS
function gcvs() { # Git Clone Repo
  git clone $1 && cd $(basename $_ .git) && code .
}

function wgcvs() { # Git Clone Repo to work dir
  cd-work
  git clone $1 && cd $(basename $_ .git) && code .
}

function ghcvs() { # Github Clone Repo
  gh repo clone $1 && cd $(basename $_ .git) && code .
}