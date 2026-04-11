import sqlite3

# 1. Connect
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# 2. Add a NEW Skill (Write)
# Let's add your Technical Writing skill for your Seattle City Light application!
new_skill = ('Technical Writing', 'Professional', 3)
cursor.execute("INSERT INTO tech_skills (skill_name, proficiency, years_exp) VALUES (?, ?, ?)", new_skill)

# 3. Save the change (CRUCIAL STEP)
connection.commit()

# 4. Pull all data to see the update (Read)
cursor.execute("SELECT skill_name, proficiency, years_exp FROM tech_skills")
rows = cursor.fetchall()

print("--- UPDATED TECH PORTFOLIO ---")
for row in rows:
    print(f"Skill: {row[0]} | Level: {row[1]} | Experience: {row[2]} years")

import sqlite3

# 1. Connect to your database
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# 2. Pull data sorted by Category and then Experience
cursor.execute("SELECT category, skill_name, proficiency, years_exp FROM tech_skills ORDER BY category, years_exp DESC")
rows = cursor.fetchall()

# 3. Print a Professional Header with the new Category column
print(f"{'CATEGORY':<15} | {'SKILL NAME':<25} | {'EXP (YRS)':<10}")
print("-" * 60)

# 4. Loop through and display the enriched data
for row in rows:
    # row[0] is Category, row[1] is Skill Name, row[3] is Years Exp
    print(f"{str(row[0]):<15} | {row[1]:<25} | {row[3]:<10}")

connection.close()

connection.close()