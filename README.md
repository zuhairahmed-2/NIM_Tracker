# NGC NIM Images Tracker

This repository automatically tracks and maintains a list of NVIDIA NIM images using GitHub Actions.

## Overview

The workflow automatically:
- Fetches the latest NIM images from NVIDIA NGC
- Tracks additions and removals of images
- Stores the data in JSON format
- Maintains a historical record of changes

## How it Works

The [GitHub Actions workflow](.github/workflows/ngc-nim-images.yml) runs on:
- Push to main branch
- Pull requests to main branch

### Features

1. **Automated Data Collection**
   - Uses NGC CLI to fetch image information
   - Filters specifically for NVIDIA NIM images
   - Stores results in structured JSON format

2. **Change Tracking**
   - Compares new data with previous version
   - Identifies added and removed images
   - Creates commits only when changes are detected

3. **Data Storage**
   - Images data stored in `data/nim_images.json`
   - Results uploaded as workflow artifacts
   - Historical changes tracked through git history

## Troubleshooting 
Contact Zuhair Ahmed (zuhaira@nvidia.com)
