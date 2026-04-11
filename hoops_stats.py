# Basketball Player Efficiency Calculator
# Formula: (PTS + REB + AST + STL + BLK) - (Missed FG + Missed FT + TO)

def calculate_efficiency(name, pts, reb, ast, stl, blk, fga, fgm, fta, ftm, to):
    # Calculate misses
    missed_fg = fga - fgm
    missed_ft = fta - ftm
    
    # Standard NBA Efficiency Formula
    efficiency = (pts + reb + ast + stl + blk) - (missed_fg + missed_ft + to)
    
    print(f"--- {name}'s Game Report ---")
    print(f"Total Efficiency Score: {efficiency}")
    return efficiency

# Test it with some sample data
calculate_efficiency(
    name="Player 1", 
    pts=25, reb=10, ast=5, stl=2, blk=1, 
    fga=15, fgm=8, fta=6, ftm=5, to=3
)