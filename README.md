# NGC NIM Images Workflow

This repository contains a **GitHub Actions** workflow that automatically **fetches a daily snapshot** of [NVIDIA NIM](https://docs.nvidia.com/ai-enterprise/ngc-overview/index.html) images from the **NGC container registry**, stores them in the `data/` folder, and **logs any changes** compared to previous runs (1 day and 7 days).

## What It Does

1. **Fetches NIM Data**: Uses the [NGC CLI](https://ngc.nvidia.com/setup/cli) to list all registry images labeled “NVIDIA NIM.”  
2. **Daily Scheduling**: Runs **every day at midnight UTC**, plus manual triggers if needed.  
3. **Archives Each Snapshot**: Saves a daily JSON file named `YYYY-MM-DD.json` in `data/archive/`.  
4. **Generates a Diff**: A single `data/nim_diff.txt` shows what changed since yesterday and since 7 days ago (NIMs added or removed).  
5. **Commits & Pushes**: Any changes get committed back to the `main` branch automatically.

## Files Generated

- **`data/archive/YYYY-MM-DD.json`**: The daily snapshot of NIM images (one for each day).  
- **`data/nim_images.json`**: The “latest” snapshot of NIM images from the most recent run.  
- **`data/nim_diff.txt`**: A text file summarizing which NIMs were **added** or **removed** in the past day and over the last 7 days.

## How to View Changes

1. **Git Commits**: After each run, if changes occur, a commit is made to the `main` branch. Check the **Commits** tab or the **History** of the `data/` folder to see when data changed.  
2. **`nim_diff.txt`**: Open the `data/nim_diff.txt` file to see which NIMs were newly added or removed.  
3. **`data/archive/`**: Explore older snapshots to see historical states day by day.

## Contributing

1. Fork the repository and make your changes on a branch.  
2. Create a pull request to merge your changes.  
3. GitHub Actions will run automatically and show if everything is passing.

## License

This repository is licensed under the [Apache License 2.0](LICENSE).

## Troubleshooting / Request for Enhancements 

Contact: Zuhair Ahmed (zuhaira@nvidia.com)
