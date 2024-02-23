
# PGN Splitter

## Overview
This Python script is designed to split a single PGN (Portable Game Notation) file, containing multiple chess games, into individual PGN files for each game.

## Features
- **Splitting PGN Files**: The script can take a large PGN file and split it into separate files, each containing a single game.
- **Custom Game Limit**: Users can specify the maximum number of games to extract, allowing for partial splits of very large files.

## Requirements
- Python 3.x
- The script requires no external libraries beyond the Python Standard Library.

## Usage

1. **Prepare Your PGN File**: Ensure your PGN file is in an accessible location. This file should contain one or more chess games in PGN format.

2. **Set the File Path and Maximum Games (Optional)**: Before running the script, set the file_path variable to the location of your PGN file. Optionally, you can also set the max_games variable to limit the number of games to split.

    ```python
    file_path = 'Games.pgn'  # PGN file you want to split
    max_games = None  # Specify the maximum number of games to create (optional), set None to extract all games
    

3. **Run the Script**: Execute the script. It will read the specified PGN file, split it into individual games, and save each game as a separate PGN file named `game_1.pgn`, `game_2.pgn`, etc., in the script's directory.

4. **Check the Output**: After the script finishes running, it will print the total number of games created. You can find the individual PGN files in the same directory as the script.

## Limitations
- The script currently does not support extracting games based on specific criteria beyond the maximum number of games.
- Large PGN files may require significant memory and processing time.