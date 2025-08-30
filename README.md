# MyPythonProjects
all of the small python projects that I do while learning things



if the sync error happens put this in the terminal


# 0) Save any uncommitted work (optional but wise if you have changes)
git status
# If you have modified files you don't want to commit yet:
# git stash -u

# 1) Make sure we're on main
git switch main

# 2) Fetch latest (including tags if you want them)
git fetch origin --tags

# 3) Rebase your local commits on top of origin/main
git pull --rebase origin main
# If there are conflicts:
#   - fix files that show <<<<<<< ======= >>>>>> markers
#   - git add <fixed-file>
#   - git rebase --continue
#   - repeat until done

# 4) Push the rebased branch (history changed, so use --force-with-lease)
git push --force-with-lease origin main

# 5) (Optional) Make rebase the default for future pulls in this repo
git config pull.rebase true
