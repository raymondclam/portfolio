import os

def analyze_html():
    # Find all HTML files in the current directory
    html_files = [f for f in os.listdir('.') if f.endswith('.html')]
    
    print("--- 🤖 AI SITE AUDIT REPORT ---")
    
    for file_path in html_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Count images and alt attributes
            img_count = content.count('<img')
            alt_count = content.count('alt=')
            
            # Count layout sections and buttons for general data
            div_count = content.count('<div')
            btn_count = content.count('<button')
            
            print(f"FILE: {file_path}")
            print(f" • Layout Sections: {div_count}")
            print(f" • Interactive Buttons: {btn_count}")
            print(f" • Images Found: {img_count}")
            print(f" • SEO Alt Tags: {alt_count}")
            
            # SEO Logic Gate
            if img_count > alt_count:
                print(f" ⚠️  SEO WARNING: Missing {img_count - alt_count} alt tags!")
            elif img_count > 0:
                print(" ✅ SEO STATUS: Excellent (All images tagged)")
            else:
                print(" ℹ️  SEO STATUS: No images found to audit")
            
            print("-" * 35)

    print("Status: Multi-page AI Audit complete!")
    print("-----------------------------------")

if __name__ == "__main__":
    analyze_html()