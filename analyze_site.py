import os

def analyze_html():
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    print("--- 🤖 AI SITE AUDIT REPORT ---")
    for file_path in html_files:
        with open(file_path, 'r') as f:
            content = f.read()
            img_count = content.count('<img')
            alt_count = content.count('alt=')
            
            print(f"File: {file_path}")
            print(f" - Images found: {img_count}")
            print(f" - SEO-Friendly Alts: {alt_count}")
            
            if img_count > alt_count:
                print(f" ⚠️ WARNING: Missing {img_count - alt_count} alt tags!")
            else:
                print(" ✅ SEO Status: Excellent")
            print("-" * 30)

if __name__ == "__main__":
    analyze_html()