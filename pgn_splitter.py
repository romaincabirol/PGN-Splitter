import re

def split_pgn_file(file_path, max_games=None):
    with open(file_path, 'r') as file:
        content = file.read()

    # Regular expression to match the start of each game
    game_start_pattern = re.compile(r'(\[Event ".*?"])', re.DOTALL)
    matches = list(game_start_pattern.finditer(content))

    games = []
    for i in range(len(matches)):
        if max_games is not None and len(games) == max_games:
            break
        start = matches[i].start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        games.append(content[start:end].strip())

    # Save each game to a separate file
    for i, game in enumerate(games):
        game_filename = f"game_{i+1}.pgn"
        with open(game_filename, 'w') as game_file:
            game_file.write(game)

    return games

file_path = '../PGN_Splitter/ArchivesChunk1/chunk_1.pgn' # PGN file you want to split
max_games = 100  # Specify the maximum number of games to create, or use None to indicate all games should be split
pgn_games = split_pgn_file(file_path, max_games)

print(f"Total games created: {len(pgn_games)}")
