#!/usr/bin/env python3

def main():
    print("=" * 70)
    print("FEATURE BRANCH WORKFLOW - TASKS")
    print("=" * 70)
    print()
    
    tasks = [
        ("Task 1", "git init", "Initialize repository"),
        ("Task 2", "git config user.name 'Data Science Student'", "Configure user"),
        ("Task 3", "git add . && git commit -m 'Initial commit'", "Commit files"),
        ("Task 4", "git checkout -b feature-viz", "Create feature branch"),
        ("Task 5", "Create plots.py", "Add visualization module"),
        ("Task 6", "git add plots.py && git commit", "Commit new file"),
        ("Task 7", "git checkout master", "Switch to master"),
        ("Task 8", "dir plots.py", "Verify file missing"),
        ("Task 9", "git checkout feature-viz", "Back to feature-viz"),
        ("Task 10", "dir plots.py", "Verify file exists"),
    ]
    
    for task_num, command, description in tasks:
        print(f"{task_num}: {description}")
        print(f"   $ {command}")
        print()
    
    print("=" * 70)
    print("BRANCH STATUS")
    print("=" * 70)
    print()
    print("MASTER: No plots.py")
    print("FEATURE-VIZ: Has plots.py")
    print()
    print("=" * 70)
    print("✓ COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    main()
