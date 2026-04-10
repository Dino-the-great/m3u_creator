rm -rf test/

# Normal multi-disc game - should succeed
mkdir -p "test/Legend of Dragoon"
touch "test/Legend of Dragoon/Legend of Dragoon, The (USA) (Disc 1).chd"
touch "test/Legend of Dragoon/Legend of Dragoon, The (USA) (Disc 2).chd"
touch "test/Legend of Dragoon/Legend of Dragoon, The (USA) (Disc 3).chd"
touch "test/Legend of Dragoon/Legend of Dragoon, The (USA) (Disc 4).chd"

# Single disc game - should skip
mkdir -p "test/Tetris"
touch "test/Tetris/Tetris (USA).chd"

# Unorderable files - should warn
mkdir -p "test/Unknown Game"
touch "test/Unknown Game/randomfile.chd"
touch "test/Unknown Game/anotherfile.chd"

# Mixed .chd and other files - should only count .chd
mkdir -p "test/Final Fantasy VII"
touch "test/Final Fantasy VII/Final Fantasy VII (USA) (Disc 1).chd"
touch "test/Final Fantasy VII/Final Fantasy VII (USA) (Disc 2).chd"
touch "test/Final Fantasy VII/Final Fantasy VII (USA) (Disc 3).chd"
touch "test/Final Fantasy VII/extras.txt"

# Disc numbering with CD instead of Disc
mkdir -p "test/Sonic Game"
touch "test/Sonic Game/Sonic Game (USA) (CD1).chd"
touch "test/Sonic Game/Sonic Game (USA) (CD2).chd"